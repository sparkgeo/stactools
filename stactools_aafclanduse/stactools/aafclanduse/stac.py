from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import pytz
import json
import logging
from stactools.aafclanduse.constants import (
    LANDUSE_ID,
    LANDUSE_EPSG,
    LANDUSE_TITLE,
    DESCRIPTION,
    LANDUSE_PROVIDER,
    LICENSE,
    LICENSE_LINK,
)

import pystac
import rasterio
from rasterio.warp import transform_bounds
from shapely import geometry

logger = logging.getLogger(__name__)


def create_item(metadata: dict, metadata_url: str, cog_href: str) -> pystac.Item:
    """Creates a STAC item for a 1990, 2000 and 2010 Canada Land Use dataset.

    Args:
        metadata_url (str): Path to provider metadata.
        cog_href (str): Path to COG asset.

    Returns:
        pystac.Item: STAC Item object.
    """

    item_id = '.'.join(cog_href.split(".")[:-1]).split("/")[-1]

    title = item_id
    description = metadata.get("description_metadata").get("dct:description")

    utc = pytz.utc

    year = re.search("\d{4}", item_id).group()
    dataset_datetime = utc.localize(datetime.strptime(year, "%Y"))

    end_datetime = dataset_datetime + relativedelta(months=12)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    src = rasterio.open(cog_href)

    bounds = src.bounds
    bbox = list(transform_bounds(src.crs, "EPSG:4326", *bounds))

    polygon = geometry.box(*bbox, ccw=True)
    coordinates = [list(i) for i in list(polygon.exterior.coords)]

    extent_geometry = {"type": "Polygon", "coordinates": [coordinates]}

    properties = {
        "title": title,
        "description": description,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }

    # Create item
    item = pystac.Item(
        id=item_id,
        geometry=extent_geometry,
        bbox=bbox,
        datetime=dataset_datetime,
        properties=properties,
        stac_extensions=[],
    )

    if start_datetime and end_datetime:
        item.common_metadata.start_datetime = start_datetime
        item.common_metadata.end_datetime = end_datetime

    # item.ext.enable("projection")
    # item.ext.projection.epsg = LANDCOVER_EPSG

    # Create metadata asset
    item.add_asset(
        "metadata",
        pystac.Asset(
            href=metadata_url,
            media_type=pystac.MediaType.JSON,
            roles=["metadata"],
            title="Land Use 1990, 2000 & 2010 metadata",
        ),
    )

    item.add_asset(
        "landuse",
        pystac.Asset(
            href=cog_href,
            media_type=pystac.MediaType.COG,
            roles=["data"],
            title="Land Use 1990, 2000 & 2010 COGs",
        ),
    )

    return item


def create_collection(metadata: dict):
    # Creates a STAC collection for a 1990, 2000 and 2010 Canada Land Use data dataset

    dataset_datetime = pytz.utc.localize(datetime.strptime(1990, "%Y"))

    end_datetime = dataset_datetime + relativedelta(years=10)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    extent_geometry = json.loads(
        metadata.get("geom_metadata").get("locn:geometry")[0].get("@value")
    )
    bbox = geometry.Polygon(extent_geometry.get("coordinates")[0]).bounds

    collection = pystac.Collection(
        id=LANDUSE_ID,
        title=LANDUSE_TITLE,
        description=DESCRIPTION,
        providers=[LANDUSE_PROVIDER],
        license=LICENSE,
        extent=pystac.Extent(
            pystac.SpatialExtent(bbox),
            pystac.TemporalExtent([start_datetime, end_datetime]),
        ),
        catalog_type=pystac.CatalogType.RELATIVE_PUBLISHED,
    )
    collection.add_link(LICENSE_LINK)

    return collection
