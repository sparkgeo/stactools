from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
import json
import logging
from stactools.nrcanlandcover.constants import (LANDCOVER_ID, LANDCOVER_EPSG,
                                                LANDCOVER_CRS, LANDCOVER_TITLE,
                                                DESCRIPTION, NRCAN_PROVIDER,
                                                LICENSE, LICENSE_LINK)
import requests

import pystac
from shapely.geometry import Polygon

logger = logging.getLogger(__name__)


def _get_metadata(metadata_url: str) -> dict:
    """Gets metadata from the various formats published by NRCan.

    Args:
        metadata_url (str): url to get metadata from.

    Returns:
        dict: Land Cover Metadata.
    """
    if metadata_url.endswith(".jsonld"):
        metadata_response = requests.get(metadata_url)
        jsonld_response = metadata_response.json()

        tiff_metadata = [
            i for i in jsonld_response.get("@graph")
            if i.get("dct:format") == "TIFF"
        ][0]
        geom_metadata = [
            i for i in jsonld_response.get("@graph")
            if "locn:geometry" in i.keys()
        ][0]
        geojson_geom = [
            i for i in geom_metadata.get("locn:geometry")
            if "geo+json" in i.get("@type")
        ][0]
        description_metadata = [
            i for i in jsonld_response.get("@graph")
            if "dct:description" in i.keys()
        ][0]

        metadata = {
            "tiff_metadata": tiff_metadata,
            "geom_metadata": geom_metadata,
            "geojson_geom": geojson_geom,
            "description_metadata": description_metadata
        }

        return metadata
    else:
        # only jsonld support.
        raise NotImplementedError()


def create_item(metadata_url: str, cog_href: str = None) -> pystac.Item:
    """Creates a STAC item for a Natural Resources Canada Land Cover dataset.

    Args:
        metadata_url (str): Path to provider metadata.
        cog_href (str, optional): Path to COG asset.

    Returns:
        pystac.Item: STAC Item object.
    """

    metadata = _get_metadata(metadata_url)

    title = metadata.get("tiff_metadata").get("dct:title")
    description = metadata.get("description_metadata").get("dct:description")

    utc = pytz.utc

    year = title.split(" ")[0]
    dataset_datetime = utc.localize(datetime.strptime(year, "%Y"))

    end_datetime = dataset_datetime + relativedelta(years=5)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    id = title.replace(" ", "-")
    geometry = json.loads(metadata.get("geojson_geom").get("@value"))
    bbox = Polygon(geometry.get("coordinates")[0]).bounds
    properties = {
        "title": title,
        "description": description,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }

    # Create item
    item = pystac.Item(
        id=id,
        geometry=geometry,
        bbox=bbox,
        datetime=dataset_datetime,
        properties=properties,
        stac_extensions=[],
    )

    # Create metadata asset
    item.add_asset(
        "json",
        pystac.Asset(
            href=metadata_url,
            media_type=pystac.MediaType.JSON,
            roles=["metadata"],
            title="JSON metadata",
        ),
    )

    if cog_href is not None:
        # Create COG asset if it exists.
        item.add_asset(
            "cog",
            pystac.Asset(
                href=cog_href,
                media_type=pystac.MediaType.COG,
                roles=["data"],
                title=title,
            ),
        )

    return item


def create_collection(metadata_url: str):
    #Creates a STAC collection for a Natural Resources Canada Land Cover dataset

    metadata = _get_metadata(metadata_url)

    title = metadata.get("tiff_metadata").get("dct:title")
    description = metadata.get("description_metadata").get("dct:description")

    utc = pytz.utc
    year = title.split(" ")[0]
    dataset_datetime = utc.localize(datetime.strptime(year, "%Y"))

    end_datetime = dataset_datetime + relativedelta(years=5)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    id = title.replace(" ", "-")
    geometry = json.loads(metadata.get("geojson_geom").get("@value"))
    bbox = Polygon(geometry.get("coordinates")[0]).bounds

    collection = pystac.Collection(
        id=LANDCOVER_ID,
        title=LANDCOVER_TITLE,
        description=DESCRIPTION,
        providers=[NRCAN_PROVIDER],
        license=LICENSE,
        extent=pystac.Extent(
            pystac.SpatialExtent(bbox),
            pystac.TemporalExtent([start_datetime, end_datetime])),
    )
    collection.add_link(LICENSE_LINK)

    return collection
