import click
import logging
from os import listdir

from stactools.nrcanlandcover import stac
from stactools.nrcanlandcover import cog
from stactools.nrcanlandcover import utils

logger = logging.getLogger(__name__)


def create_nrcanlandcover_command(cli):
    """Creates the nrcanlandcover command line utility."""
    @cli.group(
        "nrcanlandcover",
        short_help=(
            "Commands for working with Natural Resources Canada Land Cover data"
        ),
    )
    def nrcanlandcover():
        pass

    @nrcanlandcover.command(
        "create-catalog",
        short_help="Create a STAC catalog for NRCan 2015 Land Cover of Canada.",
    )
    @click.argument("destination")
    @click.option(
        "-s",
        "--source",
        help="The url to the metadata description.",
        default= \
        "https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"  # noqa
    )
    def create_catalog_command(destination: str, source: str):
        """Creates a STAC Catalog from Natural Resources Canada
        Land Cover metadata files.

        Args:
            destination (str): Path to output STAC catalog.
            source (str): Path to NRCan provided metadata - Currently only supports JSON-LD.

        Returns:
            Callable
        """

        json_path = source

        metadata = utils.get_metadata(json_path)

        asset_package_path = utils.download_asset_package(metadata)

        tif_path = [
            i for i in listdir(asset_package_path) if i.endswith(".tif")
        ]

        output_path = destination.replace(".json", "_cog.tif")

        # Create cog asset
        cog_path = cog.create_cog(tif_path, output_path, dry_run=False)

        # Create stac item
        item = stac.create_item(metadata, json_path, cog_path, destination)
        item.collection_id = "nrcan-landcover"

    @nrcanlandcover.command(
        "create-cog",
        short_help="Transform Geotiff to Cloud-Optimized Geotiff.",
    )
    @click.option("--output",
                  required=True,
                  help="The output directory to write the COGs to.")
    def create_cogs(path_to_cogs: str):
        # Fill this in
        return False

    return nrcanlandcover
