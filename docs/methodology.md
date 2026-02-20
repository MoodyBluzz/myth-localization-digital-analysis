### Language Mediation and Translation Bias

This project operates on translated and original texts across different languages.
The *Odyssey* is analyzed in English translation, while *Ulysses* is analyzed in its original English form,
and *Eneida* is analyzed in its Ukrainian burlesque adaptation.

As a result, the lexical comparison does not aim at direct linguistic equivalence,
but at **functional-semantic equivalence** within defined cultural domains
(food, alcohol, ritual, travel, etc.).

The goal is not to compare identical words,
but to compare **how often and how densely each cultural domain is activated**
within each narrative tradition.


# Methodology: Computational Comparative Analysis of Epic and Modernist Semantic Architectures

## 1. Research Design
This project employs a **Digital Humanities (DH)** framework to examine structural and semantic shifts across three pivotal literary works:
* **Ancient Epic:** Homer, *The Odyssey*
* **Burlesque Epic:** Ivan Kotliarevsky, *Eneida*
* **Modernist Prose:** James Joyce, *Ulysses*

The study integrates quantitative linguistics, network science, and hermeneutic interpretation to reveal how "material" categories (food, ritual, travel) are structurally organized within different cultural paradigms.


## 2. Technical Pipeline
The analysis follows a reproducible five-stage pipeline:
1.  **Preprocessing:** Multi-language tokenization and stop-word filtering.
2.  **Lexical Categorization:** Mapping tokens to seven distinct semantic domains (Material Culture, Ritual, Intellectual Space, etc.).
3.  **Statistical Normalization:** Calculating relative frequencies and Z-scores to mitigate corpus size bias.
4.  **Collocational Modeling:** Applying **NPMI** to identify associative strengths.
5.  **Graph Theory Analysis:** Constructing co-occurrence networks and mapping their topology.


## 3. Data Normalization Strategies
Given the significant disparity in text lengths (*Eneida*: ~32k, *Odyssey*: ~127k, *Ulysses*: ~264k tokens), the following normalization techniques were applied:

### 3.1 Frequency Normalization
Instead of raw counts, we use **Relative Frequency ($f_{rel}$)**:
$$f_{rel} = \frac{count(word)}{total\_tokens}$$

To identify statistical dominance across the three texts, **Z-score standardization** is used:
$$z = \frac{x - \mu}{\sigma}$$
*Where $x$ is the relative frequency, $\mu$ is the mean, and $\sigma$ is the standard deviation across the corpus.*

### 3.2 Network Normalization (Fixed-Node Subgraphs)
To ensure that Network Density and Clustering metrics are comparable, we perform **Fixed-Node Normalization**. We extract subgraphs based on the **Top-100** most frequent meaningful words for each text. This prevents smaller texts from appearing artificially denser than larger ones.


## 4. Collocation Modeling (NPMI)
To measure the strength of association between words, we use **Normalized Pointwise Mutual Information (NPMI)**. Unlike raw co-occurrence, NPMI accounts for the individual frequencies of words, reducing bias toward rare terms.

The formula for PMI:
$$PMI(x, y) = \log_2 \left( \frac{p(x, y)}{p(x)p(y)} \right)$$

The formula for NPMI:
$$NPMI(x, y) = \frac{PMI(x, y)}{-\log_2 p(x, y)}$$

*Values range from -1 (never occurring together) to +1 (perfect co-occurrence).*


## 5. Structural Metrics (Graph Theory)
Co-occurrence networks are analyzed using the following metrics:
* **Density:** The ratio of actual connections to all possible connections. Higher density indicates a more integrated, "collective" semantic world.
* **Average Clustering Coefficient:** Measures the tendency of words to form tightly knit groups (cliques).
* **Transitivity:** Reflects the global cohesion of the semantic architecture.


## 6. Semantic Categories (Lexical Fields)
We manually curated seven lexical fields to capture the "materiality" of the texts:
* **Alcohol & Banquets / Food & Meals:** Captures the carnivalesque and ritualized consumption.
* **Clothing & Fashion:** Reflects somatic presence and social status.
* **Sea & Travel:** Maps the spatial mobility of the epic hero.
* **Religion & Myth / Language & Education:** Traces the shift from theocentric to logocentric (intellectual) worlds.


## 7. Methodological Limitations & Transparency
* **No Lemmatization:** To maintain cross-language reproducibility and avoid language-specific NLP bias, we used raw tokens. This captures the "surface" texture of the language.
* **Exploratory Nature:** Given $N=3$ texts, results are interpreted as structural tendencies and "stylistic fingerprints" rather than universal laws.
* **Manual Filtering:** Stop-words and lexical fields were curated manually to ensure cultural relevance, acknowledging the role of the researcher in the DH pipeline.


## 8. Reproducibility
The project is implemented in **Python 3.10+** using:
* `NetworkX` for graph modeling.
* `Pandas` & `NumPy` for data manipulation.
* `Seaborn` & `Matplotlib` for statistical visualization.