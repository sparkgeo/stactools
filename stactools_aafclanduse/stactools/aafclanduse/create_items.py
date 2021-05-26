# Dataset-specific ETL code for aafc-land-use
from dataclasses import dataclass
import logging
import os
from typing import Union

# TODO: contribute stactools submodule
from .tmp_stactools.aafclanduse import stac
from .tmp_stactools.aafclanduse import cog

from etlcommon.datasets import AAFC_LAND_USE, DATASETS, DatasetConfig
from etlcommon.error_records import ErrorRecord
from etlcommon.storage import Storage
from etltask.core.commands.create.items import BaseCreateItemCommand, ItemCreationResult


logger = logging.getLogger(__name__)


@dataclass
class MissingFile(ErrorRecord):
    @classmethod
    def create(cls, file_path: str, name: str) -> "MissingFile":
        logger.info(f" -- ErrorRecord: {ErrorRecord}")
        return cls(record_id=file_path, reason=f"MISSING_{name.upper()}")


class AafclanduseCreateItemCommand(BaseCreateItemCommand):
    """Creates items from AAFC Land Use json metadata paths.

    This logic will also generate COG assets for tif files
    within asset storage. Asset storage will need to have
    authentication to read and write to the asset container.
    """

    @classmethod
    def get_dataset_config(cls) -> DatasetConfig:
        return DATASETS[AAFC_LAND_USE]

    @classmethod
    def create_item(
        cls, chunk_line: str, asset_storage: Storage
    ) -> Union[ItemCreationResult, ErrorRecord]:
        """Creates a COG asset and STAC item from AAFC Land Use json metadata

        Args:
            chunk_line (str): Path to provider json metadata.
            asset_storage (Storage): The storage object containing
                the input tif and output COG.

        Returns:
            Union[ItemCreationResult, ErrorRecord]: Item creation result or error
        """
        logger.info(f" -- chunk_line: {chunk_line}")

        tif_path = chunk_line
        cog_path = tif_path.replace(".tif", "_cog.tif")

        # Create cog asset
        cog_path = cog.create_cog(tif_path, cog_path, asset_storage, dry_run=False)

        # Create stac item
        item = stac.create_item(chunk_line, cog_path, asset_storage)
        item.collection_id = AAFC_LAND_USE

        return ItemCreationResult(item=item, item_path=tif_path.replace(".tif", ""))