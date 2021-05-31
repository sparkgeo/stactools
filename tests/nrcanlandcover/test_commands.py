import os.path
from tempfile import TemporaryDirectory

import pystac

from stactools.nrcanlandcover.commands import create_nrcanlandcover_command
from tests.utils import CliTestCase, TestData


class CreateCollectionTest(CliTestCase):
    def create_subcommand_functions(self):
        return [create_nrcanlandcover_command]

    def test_create_collection(self):
        pass