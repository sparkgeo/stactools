import click
import logging
import os

from stactools.nalcms import stac
from stactools.nalcms import cog

logger = logging.getLogger(__name__)

def create_nalcms_command(cli):
    """Creates the nalcms command line utility."""
    @cli.group(
        "nalcms",
        short_help=(
            "Commands for working with North American Land Change Monitoring System data"
        ),
    )
    def nalcms():
        pass

    @nalcms.command(
        "create-cog",
        short_help="Transform Geotiff to Cloud-Optimized Geotiff.",
    )
    @click.option("--output",
                  required=True,
                  help="The output directory to write the COGs to.")
    def create_cogs(path_to_cogs: str):
        # Fill this in
        return False

    return nalcms
