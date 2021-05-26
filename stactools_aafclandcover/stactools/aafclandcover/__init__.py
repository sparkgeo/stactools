# flake8: noqa

import stactools.core

stactools.core.use_fsspec()


def register_plugin(registry):
    # Register subcommands

    from stactools.aafclandcover import commands

    registry.register_subcommand(commands.create_aafclandcover_command)
