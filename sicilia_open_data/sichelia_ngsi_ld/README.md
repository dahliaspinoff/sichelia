# Sichelia NGSI-LD Assets

This folder contains the semantic infrastructure and the output of the data transformation process for the Sichelia project.

##  Contents

### 1. JSON-LD Contexts
* **`context_sichelia.jsonld`**: The primary context file for this project. It defines the mapping between local terms (e.g., `nativeName`, `historical_note`) and global URIs from **DBpedia**, **Schema.org**, and **FOAF**.
* **Remote Reference**: This project also aligns with the official [DataHighway Context](https://raw.githubusercontent.com/netsensesrl/datahighway-opendata/main/ngsi_ld/context.jsonld).


##  Data Modeling Details

The entities in this folder follow the NGSI-LD standard, characterized by:
- **Unique URNs**: Identifiers follow the pattern `urn:ngsi-ld:[Type]:[UUID]`.
- **Semantic Mapping**: 
    - Categories are mapped to **DBpedia classes** (e.g., `http://dbpedia.org/resource/Festival`).
    - Properties are mapped to **Ontology terms** (e.g., `description` -> `http://schema.org/description`).
- **Geo-Properties**: Location data is stored using the `GeoProperty` type with GeoJSON `Point` coordinates.
- **Relationships**: Geographical hierarchy is maintained via `isLocatedAt` (linking to City entities) and `hasProvince` (linking to Province entities).

##  How to Use the Context
To resolve the semantics of the generated entities, ensure that your NGSI-LD client or Context Broker points to the `context_sichelia.jsonld` file provided here.
