# flake8: noqa

from pyproj import CRS
from pystac import Provider
from pystac import Link

LANDUSE_ID = "aafc-landuse"
LANDUSE_EPSG = 3978
LANDUSE_CRS = CRS.from_epsg(LANDUSE_EPSG)
LANDUSE_TITLE = "Land Use 1990, 2000 & 2010"
LICENSE = "proprietary"
LICENSE_LINK = Link(
    rel="license",
    target="https://open.canada.ca/en/open-government-licence-canada",
    title="Open Government Licence - Canada",
)

DESCRIPTION = """The 1990, 2000 and 2010 Land Use (LU) maps cover all areas of Canada south of 600N at a spatial resolution of 30 metres. The LU classes follow the protocol of the Intergovernmental Panel on Climate Change (IPCC) and consist of: Forest, Water, Cropland, Grassland, Settlement and Otherland."""

LANDUSE_PROVIDER = Provider(
    name="Natural Resources Canada | Ressources naturelles Canada",
    roles=["producer", "processor", "host"],
    url="https://open.canada.ca/data/en/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec",
)

LANDUSE_FTP = "https://www.agr.gc.ca/atlas/data_donnees/lcv/aafcLand_Use/tif/"

# Provided by Open Canada data metadata repository
# https://open.canada.ca/data/en/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec.jsonld
METADATA_JSONLD = '{"@context": {"adms": "http://www.w3.org/ns/adms#", "dcat": "http://www.w3.org/ns/dcat#", "dct": "http://purl.org/dc/terms/", "foaf": "http://xmlns.com/foaf/0.1/", "gsp": "http://www.opengis.net/ont/geosparql#", "locn": "http://www.w3.org/ns/locn#", "owl": "http://www.w3.org/2002/07/owl#", "rdf": "http://schema.org/item", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "schema": "http://schema.org/", "skos": "http://www.w3.org/2004/02/skos/core#", "time": "http://www.w3.org/2006/time", "vcard": "http://www.w3.org/2006/vcard/ns#", "xsd": "http://www.w3.org/2001/XMLSchema#"}, "@graph": [{"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/83ed2485-2c1f-4284-aa53-07a45f0ec345", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/imageservices/landuse_2000/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "en", "dct:title": "Land Use 2000 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/organization/2ABCCA59-6C57-4886-99E7-85EC6C719218", "foaf:name": "Agriculture and Agri-Food Canada | Agriculture et Agroalimentaire Canada", "schema:itemtype": {"@id": "foaf:Organization"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/78547bec-cce9-4dea-b651-27cf48e938d0", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/imageservices/landuse_1990/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "en", "dct:title": "Land Use 1990 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/dc924de3-3e3e-4553-9310-83df0bb7a947", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/servicesimage/utilisation_des_terres_1990/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "fr", "dct:title": "Land Use 1990 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/9a5a8ada-20a7-4b37-bc00-53432445be54", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/landu"}, "dct:format": "HTML", "dct:language": "en", "dct:title": "AAFC Land Use 1990, 2000, 2010", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/cff5f7e3-f885-46ed-a24a-5a24a096a0d6", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/supportdocument_documentdesupport/aafcLand_Use/landUse_classification_utilisationDesTerres.zip"}, "dct:format": "XLS", "dct:language": ["en", "fr"], "dct:title": "Land Use Classifications", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/1cb10ff9-7750-4b79-8d79-d3ae72c9eea4", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/servicesimage/utilisation_des_terres_2000/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "fr", "dct:title": "Land Use 2000 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/80e9031f-202e-4668-89a5-ede6b9c02402", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/data_donnees/lcv/aafcLand_Use/tif/"}, "dct:format": "GeoTIF", "dct:language": "zxx", "dct:title": "Pre-packaged GeoTIF files", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "_:N75c3f9687b48427bb171379f22d64d35", "locn:geometry": [{"@type": "gsp:wktLiteral", "@value": "POLYGON ((-132.0000 36.0000, -60.0000 36.0000, -60.0000 60.0000, -132.0000 60.0000, -132.0000 36.0000))"}, {"@type": "https://www.iana.org/assignments/media-types/application/vnd.geo+json", "@value": "{\\"type\\": \\"Polygon\\", \\"coordinates\\": [[[-132, 36], [-60, 36], [-60, 60], [-132, 60], [-132, 36]]]}"}], "schema:itemtype": {"@id": "dct:Location"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/0d4ecfc8-c398-480c-9bbc-584da0b539f8", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/supportdocument_documentdesupport/aafcLand_Use/en/ISO_19131_Land_Use_1990__2000_2010_Data_Product_Specifications.pdf"}, "dct:format": "PDF", "dct:language": "en", "dct:title": "Data Product Specification (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/404f8028-ebf7-43bb-a51a-ee545ebc960a", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/supportdocument_documentdesupport/aafcLand_Use/fr/Utilisation_des_terres_en_1990_%202000_%202010_ISO19131.pdf"}, "dct:format": "PDF", "dct:language": "fr", "dct:title": "Data Product Specification (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/6dc39d60-332c-47b7-a900-721d718271dd", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/servicesimage/utilisation_des_terres_1990/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "fr", "dct:title": "Land Use 1990 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec", "dcat:contactPoint": {"@id": "_:Nb21887aa392342c8b20367198e365b91"}, "dcat:distribution": [{"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/7a51cfb7-8059-4fd0-93a8-5945f9f99fa5"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/6dc39d60-332c-47b7-a900-721d718271dd"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/404f8028-ebf7-43bb-a51a-ee545ebc960a"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/cff5f7e3-f885-46ed-a24a-5a24a096a0d6"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/a720c726-433f-494a-98ee-22219a67ceb6"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/78547bec-cce9-4dea-b651-27cf48e938d0"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/17b255c4-d315-4886-9588-d65d210d6879"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/0d4ecfc8-c398-480c-9bbc-584da0b539f8"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/80e9031f-202e-4668-89a5-ede6b9c02402"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/db0f1db6-d207-4ce6-95cb-eae5f697c286"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/7fd6499b-9aab-45fd-b0e5-5356d7abd0a7"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/9a5a8ada-20a7-4b37-bc00-53432445be54"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/c5e5f5e6-625d-4874-8d81-5448719c4bf1"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/5ef8aea1-b13a-4088-bf3c-9836b00bba37"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/1cb10ff9-7750-4b79-8d79-d3ae72c9eea4"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/c1d5c3cf-9bdd-4704-a806-0dafb92becb3"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/83ed2485-2c1f-4284-aa53-07a45f0ec345"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/dc924de3-3e3e-4553-9310-83df0bb7a947"}], "dcat:landingPage": {"@id": "{u\'fr\': u\'http://www.agr.gc.ca/\', u\'en\': u\'http://www.agr.gc.ca/\'}"}, "dct:accrualPeriodicity": "not_planned", "dct:description": "The 1990, 2000 and 2010 Land Use (LU) maps cover all areas of Canada south of 600N at a spatial resolution of 30 metres. The LU classes follow the protocol of the Intergovernmental Panel on Climate Change (IPCC) and consist of: Forest, Water, Cropland, Grassland, Settlement and Otherland.   \\n  \\n    \\n  \\n  The 1990, 2000 and 2010 Land Use (LU) maps were developed in response to a need for explicit, high-accuracy, high-resolution land use data to meet AAFC\\u2019s commitments in international reporting, especially for the annual National Inventory Report (NIR) to the United Nations Framework Convention on Climate Change (UNFCCC), the Agri-Environmental program of the Organization for Economic Co-operation and Development (OECD) and the FAOSTAT component of the Food and Agriculture Organization of the United Nations (FAO).", "dct:identifier": "18e3ef1a-497c-40c6-8326-aac1a34a0dec", "dct:issued": {"@type": "xsd:dateTime", "@value": "2016-09-24T03:50:50.956909"}, "dct:modified": {"@type": "xsd:dateTime", "@value": "2020-12-09T19:55:02.520715"}, "dct:publisher": {"@id": "https://open.canada.ca/organization/2ABCCA59-6C57-4886-99E7-85EC6C719218"}, "dct:spatial": {"@id": "_:N75c3f9687b48427bb171379f22d64d35"}, "dct:title": "Land Use 1990, 2000 & 2010", "schema:itemtype": {"@id": "dcat:Dataset"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/7fd6499b-9aab-45fd-b0e5-5356d7abd0a7", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/imageservices/landuse_1990/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "en", "dct:title": "Land Use 1990 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/a720c726-433f-494a-98ee-22219a67ceb6", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/servicesimage/utilisation_des_terres_2010/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "fr", "dct:title": "Land Use 2010 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "_:Nb21887aa392342c8b20367198e365b91", "schema:itemtype": {"@id": "vcard:Organization"}, "vcard:hasEmail": "agri-geomatics-agrog@agr.gc.ca"}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/db0f1db6-d207-4ce6-95cb-eae5f697c286", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/imageservices/landuse_2010/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "en", "dct:title": "Land Use 2010 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/c5e5f5e6-625d-4874-8d81-5448719c4bf1", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/servicesimage/utilisation_des_terres_2010/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "fr", "dct:title": "Land Use 2010 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/5ef8aea1-b13a-4088-bf3c-9836b00bba37", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/rest/services/imageservices/landuse_2000/ImageServer"}, "dct:format": "ESRI REST", "dct:language": "en", "dct:title": "Land Use 2000 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/17b255c4-d315-4886-9588-d65d210d6879", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/servicesimage/utilisation_des_terres_2000/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "fr", "dct:title": "Land Use 2000 (French)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/c1d5c3cf-9bdd-4704-a806-0dafb92becb3", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/services/imageservices/landuse_2010/ImageServer/WMSServer?request=GetCapabilities&service=WMS"}, "dct:format": "WMS", "dct:language": "en", "dct:title": "Land Use 2010 (English)", "schema:itemtype": {"@id": "dcat:Distribution"}}, {"@id": "https://open.canada.ca/dataset/18e3ef1a-497c-40c6-8326-aac1a34a0dec/resource/7a51cfb7-8059-4fd0-93a8-5945f9f99fa5", "dcat:accessURL": {"@id": "https://www.agr.gc.ca/atlas/uterre"}, "dct:format": "HTML", "dct:language": "fr", "dct:title": "AAFC Land Use 1990, 2000, 2010", "schema:itemtype": {"@id": "dcat:Distribution"}}]}'
