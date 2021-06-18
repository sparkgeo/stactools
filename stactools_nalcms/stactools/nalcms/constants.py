# flake8: noqa

from pyproj import CRS
from pystac import Provider
from pystac import Link

ID = "nalcms"
# EPSG = 3978
# CRS = CRS.from_epsg(EPSG)
TITLE = "North American Land Change Monitoring System data"
LICENSE = "proprietary"

# Cant find a license link for this dataset
# LICENSE_LINK = Link(
#     rel="license",
#     target="",
#     title="",
# )

DESCRIPTION = """This Land Cover change map shows class transitions from 2010 to 2015 
over Canada, Alaska, the conterminous United States and Mexico. Changes 
have been assessed from Land Cover maps at 30 meters resolution
"""

PROVIDER = Provider(
    name="Natural Resources Canada/ Canada Centre Mapping and Earth Observation",
    roles=["producer", "processor", "host"],
    url=
    "https://www.nrcan.gc.ca/maps-tools-publications/satellite-imagery-air-photos/application-development/land-cover-products/21759"
)


