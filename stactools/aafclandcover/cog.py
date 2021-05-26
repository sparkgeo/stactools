import logging

from etlcommon.storage import Storage

import os
from tempfile import TemporaryDirectory
from subprocess import CalledProcessError, check_output
from uuid import uuid1

logger = logging.getLogger(__name__)


def create_cog(
    input_path: str,
    output_path: str,
    asset_storage: Storage,
    raise_on_fail: bool = True,
    dry_run: bool = False,
) -> str:
    """Create COG from a tif

    Args:
        input_path (str): Path to the AAFC Land cover data.
        output_path (str): The path to which the COG will be written.
        asset_storage (Storage): The storage object containing
            the input tif and output COG.
        raise_on_fail (bool, optional): Whether to raise error on failure.
            Defaults to True.
        dry_run (bool, optional): Run without downloading tif, creating COG,
            and writing COG. Defaults to False.

    Returns:
        str: The path to the output COG.
    """

    if not asset_storage.file_exists(input_path):
        raise Exception(f"{input_path} does not exist in {asset_storage}")
    else:
        logger.info(f"Found file {input_path} in {asset_storage}")

    with TemporaryDirectory() as tmp_dir:
        output = None
        try:
            if dry_run:
                logger.info("Would have downloaded TIF, created COG, and written COG")
            else:
                tmp_id = str(uuid1())
                local_path = os.path.join(tmp_dir, f"{tmp_id}.tif")
                asset_storage.download_file(input_path, local_path)
                tmp_output_path = os.path.join(tmp_dir, f"{tmp_id}-out.tif")

                cmd = [
                    "gdal_translate",
                    "-of",
                    "COG",
                    "-co",
                    "BLOCKSIZE=512",
                    "-co",
                    "compress=deflate",
                    "-co",
                    "predictor=yes",
                    "-co",
                    "OVERVIEWS=IGNORE_EXISTING",
                    local_path,
                    tmp_output_path,
                ]

                try:
                    output = check_output(cmd)
                except CalledProcessError as e:
                    output = e.output
                    raise
                finally:
                    logger.info(f"output: {str(output)}")

                asset_storage.upload_file(tmp_output_path, output_path)
        except Exception:
            logger.error("Failed to process {}".format(output_path))
            failed_blob = os.path.join("etl/fix-cog/failed/", output_path)
            logger.error("Writing {}...".format(failed_blob))

            if raise_on_fail:
                raise

    return output_path
