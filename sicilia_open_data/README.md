# Sichelia Datasets: Sicilian Region Open Data

This repository describes data from the Sicilian Region's Open Data portal to map and enhance the cultural, enogastronomic, and intangible heritage of the territory. The primary datasets used as sources are described below.

---

##  Data Sources

The source data was selected to cover three fundamental pillars of Sicilian identity: **places**, **products**, and **traditions**.

| Dataset | Description | Portal Link |
| :--- | :--- | :--- |
| **Luoghi Siciliani del Gusto (LSG)** | A georeferenced collection of the main locations where essences, foods, and traditional Sicilian products are made. | [🔗 LSG Data](https://dati.regione.sicilia.it/catalogo/2e14f4a7-3c8a-4269-a885-7ed1257cc28e) |
| **Prodotti Agroalimentari Tradizionali (PAT)** | A list of Sicilian products included in the national PAT registry, recognized for established methods of processing, preservation, and aging. | [🔗 PAT Data](https://dati.regione.sicilia.it/catalogo/prodotti-agroalimentari-tradizionali) |
| **Registro delle Eredità Immateriali (REI)** | Data from the Regional Register of Intangible Heritage of Sicily (R.E.I.S.), including celebrations, knowledge, oral expressions, and symbolic spaces. | [🔗 REI Data](https://dati.regione.sicilia.it/catalogo/33a33ca5-a7d3-46f4-8b62-a0f3457765bb) |

---

##  Dataset Details

###  Luoghi Siciliani del Gusto (LSG) / Sicilian Places of Taste
Provides the geographical foundation for mapping local excellence. It contains information on businesses and production sites, enabling the spatial visualization of agrifood supply chains.

###  Prodotti Agroalimentari Tradizionali (PAT) / Traditional Agrifood Products
Represents the catalog of agricultural tradition and biodiversity. These products are considered expressions of local cultural heritage, categorized according to the regulations of the Ministry of Agriculture.

###  Registro delle Eredità Immateriali (REI) / Register of Intangible Heritage
Documents "living heritage." It focuses on the intangible elements fundamental to regional identity:
* **Book of Knowledge (Libro dei Saperi):** Craft techniques and traditional recipes.
* **Book of Celebrations (Libro delle Celebrazioni):** Rites, festivals, and anniversaries.
* **Book of Expressions (Libro delle Espressioni):** Oral traditions and dialects.
* **Book of Living Human Treasures (Libro dei Tesori Umani Viventi):** Individuals who are repositories of unique traditional knowledge.

---

##  Data Processing

The original files were processed for:
1.  **Normalization:** Text cleaning and format standardization.
2.  **Enrichment:** Integration with geographic coordinates and semantic links to **DBpedia** , **WikiData**, etc..
3.  **Conversion:** Transformation into **NGSI-LD** format to ensure semantic interoperability.

---

>  **Note**: The data is released by the Sicilian Region under the **Creative Commons Attribution (CC BY)** license. Users must provide appropriate credit to the original source (Regione Siciliana) when using or redistributing this data. For specific terms of use, please refer to the official portal links provided above.
