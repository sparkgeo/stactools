import datetime
import unittest

from stactools.nrcanlandcover import stac
from stactools.nrcanlandcover import utils


class CreateItemTest(unittest.TestCase):
    def test_create_item(self):
        metadata_url = "https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"  # noqa

        metadata = utils.get_metadata(metadata_url)

        item = stac.create_item(metadata, metadata_url)

        self.assertEqual(item.id, "2015-Land-Cover-of-Canada")
        self.assertTrue(item.geometry is not None)
        self.assertTrue(item.bbox is not None)
        self.assertEqual(
            item.datetime,
            datetime.datetime(2015,
                              1,
                              1,
                              0,
                              0,
                              0,
                              tzinfo=datetime.timezone.utc))
        self.assertEqual(
            item.common_metadata.start_datetime,
            datetime.datetime(2015,
                              1,
                              1,
                              0,
                              0,
                              0,
                              tzinfo=datetime.timezone.utc))
        self.assertEqual(
            item.common_metadata.end_datetime,
            datetime.datetime(2020,
                              1,
                              1,
                              0,
                              0,
                              0,
                              tzinfo=datetime.timezone.utc))

        data = item.assets["json"]
        self.assertEqual(data.href, (
            "https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"
        ))
        self.assertEqual(data.title, "JSON metadata")
        self.assertTrue(data.description is None)
        self.assertEqual(data.media_type, "application/json")
        self.assertEqual(data.roles, ["metadata"])

        item.ext.enable("projection")
        self.assertEqual(item.ext.projection.epsg, 3978)

        item.validate()


class CreateCollectionTest(unittest.TestCase):
    def test_create_collection(self):
        metadata_url = "https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6.jsonld"  # noqa

        metadata = utils.get_metadata(metadata_url)

        collection = stac.create_collection(metadata)

        self.assertEqual(collection.id, "nrcan-landcover")
        self.assertTrue(collection.description is not None)
        self.assertTrue(collection.title is not None)
        self.assertEqual(len(collection.extent.spatial.bboxes[0]), 4)
        self.assertEqual(len(collection.extent.temporal.intervals[0]), 2)
        self.assertEqual(collection.license, "proprietary")
