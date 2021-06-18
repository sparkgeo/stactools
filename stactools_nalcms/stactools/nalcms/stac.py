from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
import json
import logging
from stactools.nalcms.constants import (ID, TITLE, DESCRIPTION,PROVIDER, LICENSE)
import re
import shapely.geometry
import pystac

logger = logging.getLogger(__name__)


def create_item(cog_href: str) -> pystac.Item:
    """Creates a STAC item for a "North American Land Change Monitoring System dataset.

    Args:
        cog_href (str, optional): Path to COG asset.

    Returns:
        pystac.Item: STAC Item object.
    """

    item_id = cog_href.split(".")[0].split("/")[-1]
    title = re.search("(?<=30m_).*",cog_href).group().replace("_"," ").title()

    utc = pytz.utc

    year = 2010
    dataset_datetime = utc.localize(datetime.strptime(year, "%Y"))

    end_datetime = dataset_datetime + relativedelta(years=5)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    bbox = [-170,14,-50,84] # from metadata file
    
    polygon = shapely.geometry.box(*bbox, ccw=True)
    coordinates = [list(i) for i in list(polygon.exterior.coords)]

    geometry = {
                "type":"Polygon",
                "coordinates": [coordinates]
                }

    properties = {
       "title": title,
       "description": description,
       "start_datetime": start_datetime,
       "end_datetime": end_datetime,
    }

    # Create item
    item = pystac.Item(
        id=item_id,
        geometry=geometry,
        bbox=bbox,
        datetime=dataset_datetime,
        properties=properties,
        stac_extensions=[],
    )

    # item.ext.enable("projection")
    # item.ext.projection.epsg = EPSG

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


def create_collection(metadata: dict):
    # Creates a STAC collection for a Natural Resources Canada Land Cover dataset

    title = metadata.get("tiff_metadata").get("dct:title")

    utc = pytz.utc
    year = 2010
    dataset_datetime = utc.localize(datetime.strptime(year, "%Y"))

    end_datetime = dataset_datetime + relativedelta(years=5)

    start_datetime = dataset_datetime
    end_datetime = end_datetime

    bbox = [-170,14,-50,84] # from metadata file
    
    polygon = shapely.geometry.box(*bbox, ccw=True)
    coordinates = [list(i) for i in list(polygon.exterior.coords)]

    geometry = {
                "type":"Polygon",
                "coordinates": [coordinates]
                }

    collection = pystac.Collection(
        id=ID,
        title=TITLE,
        description=DESCRIPTION,
        providers=[PROVIDER],
        license=LICENSE,
        extent=pystac.Extent(
            pystac.SpatialExtent(bbox),
            pystac.TemporalExtent([start_datetime, end_datetime])),
        catalog_type=pystac.CatalogType.RELATIVE_PUBLISHED,
    )

    # Don't have a license link yet
    # collection.add_link(LICENSE_LINK)

    return collection
