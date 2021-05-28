import stactools.core
stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.nrcanlandcover import commands
    registry.register_subcommand(commands.create_nrcanlandcover_command)
