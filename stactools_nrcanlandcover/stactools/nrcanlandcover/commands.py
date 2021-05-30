import click
import logging

from stactools.nrcanlandcover import stac
from stactools.nrcanlandcover import cog

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
        default="https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"
    )    
    def create_catalog_command(destination: str, source: str):
        """Creates a STAC Catalog from Natural Resources Canada
        Land Cover metadata files.

        Args:
            source (str): Path to NRCan provided metadata - Currently only supports JSON-LD.
            output (str): Path to output STAC catalog.

        Returns:
            Callable
        """

        json_path = source

        item = stac.create_item(source)

        # tif_path = json_path.replace(".json", ".tif")
        # output_path = json_path.replace(".json", "_cog.tif")

        # Create cog asset
        # cog_path = cog.create_cog(tif_path, output_path, output, dry_run=False)

        # Create stac item
        # item = stac.create_item(json_path, cog_path, output)
        # item.collection_id = "nrcan-landcover"



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
