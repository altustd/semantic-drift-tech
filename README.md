# Technology Words Drift Faster

*Quantifying Semantic Change Rates Across Lexical Categories*

Do words associated with emerging technologies undergo semantic change faster than ordinary vocabulary? Using pre-trained historical word embeddings (Hamilton et al. 2016) spanning 1800–1990, we show technology-associated words drift at 2.3× the rate of frequency-matched controls, with change-points clustering around the radio era (1920s), computing era (1950s–1960s), and personal computing era (1980s).

---

## Read Online

**[https://altustd.github.io/semantic-drift-tech/semantic-drift-tech.html](https://altustd.github.io/semantic-drift-tech/semantic-drift-tech.html)** (full interactive paper)

---

## Data

**Primary**: Hamilton et al. (2016) HistWords — pre-trained Word2Vec embeddings per decade, 1800–1990, Google Books English corpus.

```bash
pixi run download   # downloads ~1.5 GB to data/raw/
```

**Extension**: COHA (Corpus of Historical American English) — register free at corpus.byu.edu

---

## Run Locally

```bash
pixi install
pixi run download     # get Hamilton vectors (~1.5 GB, one time)
pixi run render       # HTML → docs/
pixi run render-pdf   # PDF → docs/
pixi run preview      # live preview
```

## Tech Stack

Quarto · pixi · Python 3.12 · gensim · scipy · ruptures · Plotly
