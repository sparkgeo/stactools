import datetime
import json
import logging
import requests

import pystac
from etlcommon.storage import Storage
from shapely.geometry import Polygon
import rasterio
from rasterio.warp import transform_bounds
import shapely.geometry

logger = logging.getLogger(__name__)


def create_item(chunk: str, cog_path: str, asset_storage: Storage) -> pystac.Item:
    """Creates a STAC item for an AAFC Land Use dataset.

    Args:
        json_href (str): Path to provider json metadata.
        cog_href (str): Path to COG asset.
        asset_storage (Storage): The storage object containing
            the input tif and output COG.

    Returns:
        pystac.Item: STAC Item object.
    """
    
    meta_data_url = asset_storage.get_url("metadata.json")
    json_response = requests.get(meta_data_url)
    json_metadata = json_response.json()

    id = chunk.split(".")[0].split("/")[-1]
    title = json_metadata["@graph"][4]["dct:title"]
    description = json_metadata["@graph"][14]['dct:description'].strip('\n')

    if "1990" in id:
        dataset_datetime,start_datetime,end_datetime = start_end_datetime("1990")
    elif "2000" in id:
        dataset_datetime,start_datetime,end_datetime =start_end_datetime("2000")
    else:
        dataset_datetime,start_datetime,end_datetime =start_end_datetime("2010")

    cog_href=asset_storage.get_url(cog_path)
    src = rasterio.open(cog_href)

    bounds = src.bounds
    bbox = list(transform_bounds(src.crs, "EPSG:4326", *bounds))
    
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
        id=id,
        geometry=geometry,
        bbox=bbox,
        datetime=dataset_datetime,
        properties=properties,
        stac_extensions=[],
    )

    # Create COG asset
    item.add_asset(
        "cog",
        pystac.Asset(
            href=asset_storage.get_url(cog_href),
            media_type=pystac.MediaType.COG,
            roles=["data"],
            title=title,
        ),
    )

    return item


def start_end_datetime(year):
    dataset_datetime = datetime.datetime.strptime(year, "%Y")
    start_datetime = f"{year}-01-01T00:00:00"
    end_datetime = f"{year}-12-31T00:00:00"

    return dataset_datetime, start_datetime, end_datetime