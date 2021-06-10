import os
import unittest

from tempfile import TemporaryDirectory
from tests.utils import TestData, validate_cloud_optimized_geotiff
from stactools.nrcanlandcover import cog


class CreateCogTest(unittest.TestCase):
    def test_create_cog(self):
        tif_path = TestData.get_path(
            "data-files/nrcanlandcover/CAN_LC_2015_CAL.tif")

        with TemporaryDirectory() as directory:
            output_path = f"{directory}/output_cog.tif"
            outfile = cog.create_cog(tif_path, output_path, dry_run=False)

            self.assertTrue(os.path.exists(outfile))
            warnings, errors, _ = validate_cloud_optimized_geotiff.validate(
                outfile, full_check=True)
            self.assertEqual(len(warnings), 0)
            self.assertEqual(len(errors), 0)
