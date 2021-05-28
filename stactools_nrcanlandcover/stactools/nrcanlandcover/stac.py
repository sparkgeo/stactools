import datetime
import json
import logging
import requests

import pystac
from shapely.geometry import Polygon

logger = logging.getLogger(__name__)


def create_item(json_href: str, cog_href: str) -> pystac.Item:
    """Creates a STAC item for a Natural Resources Canada Land Cover dataset.

    Args:
        json_href (str): Path to provider json metadata.
        cog_href (str): Path to COG asset.

    Returns:
        pystac.Item: STAC Item object.
    """
    json_response = requests.get(json_href)
    json_metadata = json_response.json()

    tiff_metadata = [
        i for i in json_metadata.get("@graph") if i.get("dct:format") == "TIFF"
    ][0]
    geom_metadata = [
        i for i in json_metadata.get("@graph") if "locn:geometry" in i.keys()
    ][0]
    geojson_geom = [
        i for i in geom_metadata.get("locn:geometry")
        if "geo+json" in i.get("@type")
    ][0]
    description_metadata = [
        i for i in json_metadata.get("@graph")
        if "dct:description" in i.keys()
    ][0]

    title = tiff_metadata.get("dct:title")
    description = description_metadata.get("dct:description")
    dataset_datetime = datetime.datetime.strptime(title.split(" ")[0], "%Y")
    start_datetime = dataset_datetime.isoformat()
    end_datetime = datetime.datetime.strptime(
        str(int(title.split(" ")[0]) + 5), "%Y").isoformat()

    id = title.replace(" ", "-")
    geometry = json.loads(geojson_geom.get("@value"))
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
            href=json_href,
            media_type=pystac.MediaType.JSON,
            roles=["metadata"],
            title="JSON metadata",
        ),
    )

    # Create COG asset
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
