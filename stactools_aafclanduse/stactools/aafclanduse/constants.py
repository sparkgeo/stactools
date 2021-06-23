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
METADATA_JSONLD = """{
  "@context": {
    "adms": "http://www.w3.org/ns/adms#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "gsp": "http://www.opengis.net/ont/geosparql#",
    "locn": "http://www.w3.org/ns/locn#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://schema.org/item",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "time": "http://www.w3.org/2006/time",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/c5531a14-33dc-48b5-86cf-e2e374638ffc",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/uterre"
      },
      "dct:format": "HTML",
      "dct:language": "fr",
      "dct:title": "Land Use 1990, 2000, 2010(French)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/3263d6f6-db72-41b5-8ddf-1a19a47fed16",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/supportdocument_documentdesupport/aafcLand_Use/fr/Utilisation_des_terres_en_1990_%202000_%202010_ISO19131.pdf"
      },
      "dct:format": "PDF",
      "dct:language": "fr",
      "dct:title": "Data Product Specification (French)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/f23a69a5-d7eb-4649-85c4-f5d4d148a6d9",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/landu"
      },
      "dct:format": "HTML",
      "dct:language": "en",
      "dct:title": "Land Use 1990, 2000, 2010 (English)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/3927d990-1cee-4413-b8a5-7fa1d9648b28",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/services/imageservices/landuse_2010/ImageServer/WMSServer?request=GetCapabilities&service=WMS&layers=0&legend_format=image/png"
      },
      "dct:format": "WMS",
      "dct:language": "en",
      "dct:title": "Land Use 2010",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/b35fc700-20cc-4b70-ba32-6d721a07cc21",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/agrimap"
      },
      "dct:format": "HTML",
      "dct:language": "en",
      "dct:title": "AgriMap (English)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "_:N90bf26748c3a4de4855df5a37f584606",
      "schema:itemtype": {
        "@id": "vcard:Organization"
      },
      "vcard:hasEmail": "agri-geomatics-agrog@agr.gc.ca"
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/9143db93-c242-46b2-96ce-4dcd8ddbb895",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/data_donnees/lcv/aafcLand_Use/tif/2010/"
      },
      "dct:format": "GeoTIF",
      "dct:language": "zxx",
      "dct:title": "Pre-packaged GeoTIF files (No linguistic component)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/64dcbc70-34cf-4df2-886c-0e05b5be2d7c",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/rest/services/servicesimage/utilisation_des_terres_2010/ImageServer"
      },
      "dct:format": "ESRI REST",
      "dct:language": "fr",
      "dct:title": "Land Use 2010",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/5d8e2a94-f90c-4fc1-bdf7-9a0d037b149c",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/rest/services/imageservices/landuse_2010/ImageServer"
      },
      "dct:format": "ESRI REST",
      "dct:language": "en",
      "dct:title": "Land Use 2010",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "_:Ncc1bc847945040909a0e482f3908700f",
      "locn:geometry": [
        {
          "@type": "gsp:wktLiteral",
          "@value": "POLYGON ((-132.0000 36.0000, -60.0000 36.0000, -60.0000 60.0000, -132.0000 60.0000, -132.0000 36.0000))"
        },
        {
          "@type": "https://www.iana.org/assignments/media-types/application/vnd.geo+json",
          "@value": "{\"type\": \"Polygon\", \"coordinates\": [[[-132.0, 36.0], [-60.0, 36.0], [-60.0, 60.0], [-132.0, 60.0], [-132.0, 36.0]]]}"
        }
      ],
      "schema:itemtype": {
        "@id": "dct:Location"
      }
    },
    {
      "@id": "https://open.canada.ca/organization/2ABCCA59-6C57-4886-99E7-85EC6C719218",
      "foaf:name": "Agriculture and Agri-Food Canada | Agriculture et Agroalimentaire Canada",
      "schema:itemtype": {
        "@id": "foaf:Organization"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/2c2a5c8d-e16d-45be-936d-012d08bf9930",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/agricarte"
      },
      "dct:format": "HTML",
      "dct:language": "fr",
      "dct:title": "AgriMap (French)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf",
      "dcat:contactPoint": {
        "@id": "_:N90bf26748c3a4de4855df5a37f584606"
      },
      "dcat:distribution": [
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/5d8e2a94-f90c-4fc1-bdf7-9a0d037b149c"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/3927d990-1cee-4413-b8a5-7fa1d9648b28"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/9143db93-c242-46b2-96ce-4dcd8ddbb895"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/eca5551a-0622-4a40-9391-ca17f830684c"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/b35fc700-20cc-4b70-ba32-6d721a07cc21"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/64dcbc70-34cf-4df2-886c-0e05b5be2d7c"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/2c2a5c8d-e16d-45be-936d-012d08bf9930"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/c5531a14-33dc-48b5-86cf-e2e374638ffc"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/0e1ac539-bab1-47fe-b6fa-69a453b40db2"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/3263d6f6-db72-41b5-8ddf-1a19a47fed16"
        },
        {
          "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/f23a69a5-d7eb-4649-85c4-f5d4d148a6d9"
        }
      ],
      "dcat:landingPage": {
        "@id": "{u'fr': u'http://www.agr.gc.ca/', u'en': u'http://www.agr.gc.ca/'}"
      },
      "dct:accrualPeriodicity": "not_planned",
      "dct:description": "The 2010 Land Use (LU) maps cover all areas of Canada south of 600N at a spatial resolution of 30 metres. The LU classes follow the protocol of the Intergovernmental Panel on Climate Change (IPCC) and consist of: Forest, Water, Cropland, Grassland, Settlement and Otherland.   \n  \n    \n  \n  The 2010 Land Use (LU) maps were developed in response to a need for explicit, high-accuracy, high-resolution land use data to meet AAFC’s commitments in international reporting, especially for the annual National Inventory Report (NIR) to the United Nations Framework Convention on Climate Change (UNFCCC), the Agri-Environmental program of the Organization for Economic Co-operation and Development (OECD) and the FAOSTAT component of the Food and Agriculture Organization of the United Nations (FAO).",
      "dct:identifier": "9e1efe92-e5a3-4f70-b313-68fb1283eadf",
      "dct:issued": {
        "@type": "xsd:dateTime",
        "@value": "2016-09-25T02:38:53.048255"
      },
      "dct:modified": {
        "@type": "xsd:dateTime",
        "@value": "2020-12-09T18:40:13.020579"
      },
      "dct:publisher": {
        "@id": "https://open.canada.ca/organization/2ABCCA59-6C57-4886-99E7-85EC6C719218"
      },
      "dct:spatial": {
        "@id": "_:Ncc1bc847945040909a0e482f3908700f"
      },
      "dct:title": "Land Use 2010",
      "schema:itemtype": {
        "@id": "dcat:Dataset"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/eca5551a-0622-4a40-9391-ca17f830684c",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/services/servicesimage/utilisation_des_terres_2010/ImageServer/WMSServer?request=GetCapabilities&service=WMS&layers=0&legend_format=image/png"
      },
      "dct:format": "WMS",
      "dct:language": "fr",
      "dct:title": "Land Use 2010",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    },
    {
      "@id": "https://open.canada.ca/dataset/9e1efe92-e5a3-4f70-b313-68fb1283eadf/resource/0e1ac539-bab1-47fe-b6fa-69a453b40db2",
      "dcat:accessURL": {
        "@id": "https://www.agr.gc.ca/atlas/supportdocument_documentdesupport/aafcLand_Use/en/ISO_19131_Land_Use_1990__2000_2010_Data_Product_Specifications.pdf"
      },
      "dct:format": "PDF",
      "dct:language": "en",
      "dct:title": "Data Product Specification (English)",
      "schema:itemtype": {
        "@id": "dcat:Distribution"
      }
    }
  ]
}"""
