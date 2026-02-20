# Myth Localization and Everyday Culture: A Digital Humanities Project

This project explores how everyday material and bodily practices (food, alcohol, music, clothing, rituals) function as cultural markers in the transformation of the Homeric epic tradition. 

By applying computational text analysis to **James Joyce’s *Ulysses* (1922)**, **Homer’s *Odyssey***, and **Ivan Kotliarevsky’s *Eneida* (1808)**, the study examines strategies of myth localization in Irish modernism and Ukrainian early modern literature.

## Key Research Questions
* **RQ1-3 (Lexical Patterns):** How do material categories (banquets, clothing, travel) dominate the semantic space of each text?
* **RQ4 (Cultural Semantics):** What are the strongest culturally specific collocations for these markers?
* **RQ5-6 (Structural Evolution):** How does the network architecture of semantic markers evolve from epic coherence to modernist fragmentation?

## Tech Stack & Methodology
* **Language:** Python 3.10+
* **Libraries:** `pandas`, `numpy` (Data Processing), `networkx` (Graph Theory), `seaborn`, `matplotlib` (Visualization).
* **Techniques:**
    * **NPMI (Normalized Pointwise Mutual Information):** For associative strength between cultural markers.
    * **Z-score Normalization:** For statistical comparison of category dominance across unequal corpus sizes.
    * **Graph Topology Mapping:** Using Density, Clustering, and Transitivity to identify "structural fingerprints" of literary traditions.

## Key Findings (Step 5: Comparative Analysis)
* **The "Warm" Collective Core:** *Eneida* exhibits the highest semantic density (Density $\approx 0.72$), reflecting a tightly integrated folk-burlesque world centered on communal ritual (food and alcohol).
* **Theocentric Modularity:** *The Odyssey* presents an ordered, modular structure where maritime travel is intrinsically linked to divine agency.
* **Modernist Rhizome:** *Ulysses* demonstrates significant semantic de-centralization. The network is fragmented, reflecting the modern shift from communal myth to individual, somatic experience.



## Visualizations
The project generates several types of analytical plots:
1. **Statistical Dominance Heatmaps:** Z-scores for lexical categories.
2. **Structural Scatterplots:** Mapping Density vs. Cohesion.
3. **NPMI Collocation Tables:** Identifying unique associative pairs.