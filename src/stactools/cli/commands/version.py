from click import echo

import pystac
from pystac.version import get_stac_version

from stactools.core import __version__


def create_version_command(cli):
    @cli.command('version', short_help='Display version info.')
    def version_command():
        """Display version info
        """
        echo(f"stactools version {__version__}")
        echo(f"PySTAC version {pystac.__version__}")
        echo(f"STAC version {get_stac_version()}")

    return version_command
