# Text Summarization Tool

CLI utility that produces concise multi‑sentence summaries using an LSA (Latent Semantic Analysis) extractive algorithm from the Sumy library.

## Features
- LSA summarization (`sumy.summarizers.lsa.LsaSummarizer`)
- Automatic NLTK resource download (`punkt`, `stopwords`)
- Simple interactive console prompt
- Configurable number of sentences (parameter in `summarize` function)
- Lightweight, single‑file implementation

## How It Works
1. User supplies a paragraph via standard input.
2. (Current version) Text is sent directly to Sumy without custom preprocessing.
3. Sumy parses and tokenizes the text, builds a term–sentence matrix, performs LSA, and selects top sentences.
4. Selected sentences are printed in order.
5. (Optional) A `preprocess` helper exists (lowercasing, punctuation removal, stopword filtering) but is not yet integrated into the pipeline—you can wire it in before calling `summarize`.

## Requirements

### Prerequisites
- Python 3.13+
- Internet access on first run to download NLTK data (unless pre‑downloaded)

### Key Dependencies
- sumy
- nltk

## Installation
```bash
cd Text-Summarization-Tool
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate
uv pip install -r requirements.txt   # or: uv pip install .
```

(Offline prep, optional):
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## Usage
```bash
python main.py
```
When prompted, paste or type a paragraph, then press Enter. Tool returns a default 3‑sentence summary.

To change summary length, modify the call:
```python
summary = summarize(input_text, num_sentences=5)
```

## Example
```
=== Text Summarizer ===
Enter a paragraph:

<your text>

Summary:
1. First extracted sentence.
2. Second extracted sentence.
3. Third extracted sentence.
```

## Project Structure
```
Text-Summarization-Tool/
├── main.py
├── pyproject.toml
├── README.md
└── (optional) uv.lock
```

## Extending
- Integrate `preprocess` before `summarize` for normalization.
- Add CLI args (`argparse`) for input file, sentence count.
- Provide multiple algorithms (e.g., LexRank, Luhn via Sumy).
- Add language selection (tokenizer + stopwords for other locales).
- Wrap as a Streamlit or FastAPI service.

## Limitations
- Extractive only (no paraphrasing).
- Quality depends on input sentence segmentation.
- Current version ignores the `preprocess` output (can reduce performance on noisy text).

## License
MIT (see repository root).

## Contributions
PRs and issues welcome.

## Acknowledgements
- Sumy for summarization algorithms
- NLTK