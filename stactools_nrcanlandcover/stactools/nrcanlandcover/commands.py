import click
import logging

from stactools.nrcanlandcover import stac
from stactools.nrcanlandcover import cog

logger = logging.getLogger(__name__)


def create_nrcanlandcover_command(cli):
    """Creates items from Natural Resources Canada Land Cover
    json metadata paths.

    This logic will also generate COG assets for tif files
    within asset storage.
    """
    @cli.group(
        "nrcanlandcover",
        short_help=(
            "Commands for working with Natural Resources Canada Land Cover data"
        ),
    )
    def nrcanlandcover():
        pass

    @nrcanlandcover.command(
        "create-item",
        short_help=
        "Generates COGs and STAC items from Natural Resources Canada Land Cover tifs.",
    )
    @click.option("--json_path",
                  required=True,
                  help="HREF to the provider json metadata file")
    @click.option(
        "--output",
        required=True,
        help="The output directory to write the COGs and STAC items to.",
    )
    def create_item(json_path: str, output: str):
        """Creates a COG asset and STAC item from Natural Resources Canada
         Land Cover json metadata

        Args:
            json_path (str): Path to provider json metadata.
            output (str): The storage object containing
                the input tif and output COG.

        Returns:
            Callable
        """
        # TODO: Refactor create_cog/create_item to use output directory instead of the etcommon.Storage class

        tif_path = json_path.replace(".json", ".tif")
        output_path = json_path.replace(".json", "_cog.tif")

        # Create cog asset
        cog_path = cog.create_cog(tif_path, output_path, output, dry_run=False)

        # Create stac item
        item = stac.create_item(json_path, cog_path, output)
        item.collection_id = "nrcan-landcover"

    return nrcanlandcover
