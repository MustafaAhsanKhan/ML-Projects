# Named Entity Recognition (NER) System

Minimal spaCy-based utility for extracting named entities (text span, label, character offsets) using the lightweight `en_core_web_sm` model.

## Features
- Uses pre-trained `en_core_web_sm`
- Returns entity text, type label, start & end character offsets
- Simple callable `extract_entities(text)` function
- Tiny demo block when run as a script

## How It Works
1. Loads the spaCy pipeline once at import: `spacy.load("en_core_web_sm")`
2. Processes input text into a `Doc`
3. Iterates `doc.ents` returning tuples: `(ent.text, ent.label_, ent.start_char, ent.end_char)`

## Requirements
### Prerequisites
- Python 3.13+
- spaCy installed
- Model downloaded:
```bash
python -m spacy download en_core_web_sm
```

## Installation
```bash
cd NER-System
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate
uv pip install -r requirements.txt   # or: uv pip install .
python -m spacy download en_core_web_sm
```

## Usage (Library)
```python
from ner_infer import extract_entities

text = "OpenAI is headquartered in San Francisco and was co-founded by Sam Altman."
entities = extract_entities(text)
for span, label, start, end in entities:
    print(span, label, start, end)
```

## CLI / Script Demo
```bash
python ner_infer.py
```
Outputs sample entities for the hardcoded sentence.

## Example Output
```
Sundar Pichai → PERSON [0:13]
Google → ORG [31:37]
California → GPE [53:63]
```

## Project Structure
```
NER-System/
├── ner_infer.py
├── pyproject.toml
├── README.md
└── (optional) uv.lock
```

## Extending
- Add CLI argument parsing for input text or file
- Support batch processing
- Expose JSON / CSV export
- Swap to larger model (`en_core_web_trf`) for improved accuracy

## Limitations
- Small model (reduced accuracy vs. larger pipelines)
- English-only (current configuration)
- No custom domain adaptation

## License
MIT (see root LICENSE if present).

## Acknowledgements
- spaCy core developers