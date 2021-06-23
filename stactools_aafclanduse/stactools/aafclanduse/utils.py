import json
from stactools.aafclanduse.constants import METADATA_JSONLD

def get_metadata() -> dict:
    """Gets metadata from the an accompanying jsonld file

    Returns:
        dict: AAFC Land Use Metadata.
    """
    jsonld = json.loads(METADATA_JSONLD)
    geom_metadata = [
        i for i in jsonld.get("@graph") if "locn:geometry" in i.keys()
    ][0]
    description_metadata = [
        i for i in jsonld.get("@graph") if "dct:description" in i.keys()
    ][0]

    metadata = {
        "geom_metadata": geom_metadata,
        "description_metadata": description_metadata,
    }

    return metadata
