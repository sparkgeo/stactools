import stactools.core

from stactools.nrcanlandcover.stac import create_item
from stactools.nrcanlandcover.cog import create_cog

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.nrcanlandcover import commands
    registry.register_subcommand(commands.create_nrcanlandcover_command)
