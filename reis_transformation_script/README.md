# Data Transformation: Intangible Heritage in NGSI-LD

This repository contains the Python script for transforming and enriching data related to **Intangible Cultural Heritage** (e.g., festivals, rituals, traditional crafts) into the **NGSI-LD** standard format.

---

## Script

The **ETL** (Extract, Transform, Load) process performs the following operations:

| Feature | Description |
|---------|-------------|
| **Semantic Mapping** | Converts local categories into standard DBpedia ontological classes (e.g., `Festival`, `Craft`, `Ritual`). |
| **Automatic Geolocation** | Cross-references municipality data with an external geographic entities API to assign coordinates (Longitude/Latitude) and hierarchical relationships with Provinces. |
| **Metadata Enrichment** | Extracts and normalizes information on bibliography, discography, historical notes, and temporal occurrences. |
| **JSON-LD Context Management** | Generates and updates a local context file (`context_local.jsonld`). Maps specific properties to standard vocabularies such as *Schema.org*, *DBpedia Ontology*, and *FOAF*. |
| **NGSI-LD Compliant Output** | Produces a JSON-LD file ready to be loaded into a Context Broker (e.g., Orion-LD), complete with `Relationships` and `GeoProperties`. |

---

##  Requirements

- **Python 3.x**
- Required libraries:

```bash
pip install requests pydbpedia SPARQLWrapper
```

## Usage

1. Configure the file paths and your **API Key** in the script's initial variables.
2. Ensure the source JSON file is present in the specified folder.
3. Run the script:

```bash
python transform_immateriali.py
```

## Output - Data Structure

The produced entity follows the **NGSI-LD** model, including:

| Field | Description |
|-------|-------------|
| **Unique Identifier** | Based on UUID and DBpedia type |
| **Location** | GeoJSON geographic point |
| **Relationships** | Links to `City` and `Province` entities through the `isLocatedAt` attribute |
| **Properties** | Textual and temporal attributes semantically mapped |

---

> **Note**: This project is part of an initiative for the openness and interoperability of Sicilian cultural data.
