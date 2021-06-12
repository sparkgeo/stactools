import os
import unittest

from tempfile import TemporaryDirectory
from tests.utils import TestData, validate_cloud_optimized_geotiff
from stactools.nrcanlandcover import cog
from stactools.nrcanlandcover import utils


class CreateCogTest(unittest.TestCase):
    def test_create_cog(self):
        zip_path = TestData.get_path(
            "data-files/nrcanlandcover/CanadaLandcover2015.zip")

        with TemporaryDirectory() as directory:
            asset_package_path = utils._unzip_dir(zip_path, directory)
            tif_path = os.path.join(asset_package_path, [
                i for i in os.listdir(asset_package_path) if i.endswith(".tif")
            ][0])

            output_path = f"{directory}/output_cog.tif"
            outfile = cog.create_cog(tif_path, output_path, dry_run=False)

            self.assertTrue(os.path.exists(outfile))
            warnings, errors, _ = validate_cloud_optimized_geotiff.validate(
                outfile, full_check=True)
            self.assertEqual(len(warnings), 0)
            self.assertEqual(len(errors), 0)
