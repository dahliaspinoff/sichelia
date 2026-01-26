# Patronal Festivals JSON-LD
This folder contains a JSON-LD file with an extraction of Patronal Festival entities and their related data.
The dataset has been retrieved from an NGSI-LD compliant context broker and includes structured information about local patronal festivals, such as urn identifiers, official Italian names and local names in Sicilian dialect, locations and coordinates, description, type of event and other associated attributes.

The file is provided in JSON-LD format and uses a custom @context to ensure semantic interoperability and compatibility with linked data tools.

## Contents

PatronalFestival_output.jsonld – JSON-LD file containing the extracted Patronal Festival entities and their attributes.

## Format

Standard: JSON-LD

Data model: NGSI-LD

## Context
Custom JSON-LD [context_sichelia.jsonld](https://github.com/dahliaspinoff/sichelia/tree/main/sicilia_open_data/sichelia_ngsi_ld)


### Data Retrieval 
To retrieve the **Patronal Festival** entities in JSON-LD format from the NGSI-LD broker, use the following HTTP request:

```bash
curl -X GET "https://datahighway.netsenseweb.com/federation/sichelia/ngsi-ld/v1/entities?type=PatronalFestival" \
  -H "Accept: application/ld+json" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Link: <https://raw.githubusercontent.com/dahliaspinoff/sichelia/refs/heads/main/sicilia_open_data/sichelia_ngsi_ld/context_sichelia.jsonld>; \
rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\""

____________________________________________________________________________________
### Notes

Some attributes may be optional or missing depending on the original data source.

### Extraction Date

The data was extracted on: 2026-01-26.
