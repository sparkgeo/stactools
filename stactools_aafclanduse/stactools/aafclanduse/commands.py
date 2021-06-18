import click
import logging
import os

from stactools.aafclanuse import stac
from stactools.aafclanuse import cog
from stactools.aafclanuse import utils
from stactools.aafclanuse.constants import LANDUSE_ID

logger = logging.getLogger(__name__)


def create_aafclanduse_command(cli):
    """Creates the aafclanduse command line utility."""
    @cli.group(
        "aafclanduse",
        short_help=(
            "Commands for working with 1990, 2000 and 2010 Canada Land Use data"
        ),
    )
    def aafclanduse():
        pass

    @aafclanduse.command(
        "create-cog",
        short_help="Transform Geotiff to Cloud-Optimized Geotiff.",
    )
    @click.option("--output",
                  required=True,
                  help="The output directory to write the COGs to.")
    def create_cogs(path_to_cogs: str):
        # Fill this in
        return False

    return aafclanduse
