import os
import unittest

from tests.utils import TestData
from stactools.nrcanlandcover import utils


class UtilsTest(unittest.TestCase):
    def test_get_metadata(self):
        metadata_path = TestData.get_path(
            "data-files/nrcanlandcover/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"
        )

        metadata = utils.get_metadata(metadata_path)

        self.assertTrue(metadata.get("tiff_metadata") is not None)
        self.assertTrue(metadata.get("geom_metadata") is not None)
        self.assertTrue(metadata.get("geojson_geom") is not None)
        self.assertTrue(metadata.get("description_metadata") is not None)
        self.assertTrue(metadata.get("tiff_metadata") is not None)

    def test_download_asset_package(self):
        metadata_path = TestData.get_path(
            "data-files/nrcanlandcover/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"
        )

        metadata = utils.get_metadata(metadata_path)

        asset_package_path = utils.download_asset_package(metadata)
        self.assertTrue(os.path.exists(asset_package_path))

        utils.remove_asset_package(asset_package_path)
        self.assertFalse(os.path.exists(asset_package_path))
