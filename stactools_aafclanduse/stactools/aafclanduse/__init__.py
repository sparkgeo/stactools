import stactools.core

from stactools.aafclanduse.stac import create_item
from stactools.aafclanduse.cog import create_cog

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.aafclanduse import commands
    registry.register_subcommand(commands.create_aafclanduse_command)
