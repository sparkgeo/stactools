import click

from etltask.aafclanduse.cli import dataset_cmd
from testutils import integration


class IntegrationTest(integration.DatasetIntegrationTestCase):
    """Integration tests that test ETL processing end to end"""

    def get_dataset_command(self) -> click.Command:
        return dataset_cmd

    def get_test_chunk_lines(self) -> integration.TestChunkLines:
        return integration.TestChunkLines(
            chunk_lines=[""],  # noqa
            fail_chunk_lines=['images/nonexistant.hdf.xml'],
            error_record_lines=None,
        )

