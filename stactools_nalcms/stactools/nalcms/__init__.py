import stactools.core

from stactools.nalcms.stac import create_item
from stactools.nalcms.cog import create_cog

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.nalcms import commands
    registry.register_subcommand(commands.create_nalcms_command)
