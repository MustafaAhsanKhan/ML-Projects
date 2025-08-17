# Rule Based Chatbot

Lightweight educational Q&A chatbot using simple token overlap intent matching over a JSON intents file. Provides quick, deterministic responses and a fallback for unmatched queries.

## Features
- JSON-driven intents (patterns + responses)
- Tokenization with NLTK `punkt`
- Simple any-token pattern matching
- CLI loop with exit commands (`quit`, `exit`)
- Fallback response for unknown input

## How It Works
- Loads `intents.json` at startup.
- User input and pattern strings are lowercased and tokenized (`word_tokenize`).
- If any token from a pattern appears in the user input, that intent is selected.
- A random response from the intent’s `responses` list is returned.
- No ML model; purely rule based.

## Requirements

### Prerequisites
- Python 3.13+
- NLTK (downloads `punkt` at runtime)
- `intents.json` present in the same directory

### Installation
```bash
cd Rule-Based-Chatbot
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate
uv pip install -r requirements.txt   # or: uv pip install .
```

(If running in a restricted environment, pre-download NLTK data:
`python -c "import nltk; nltk.download('punkt')"`)
 
## Usage
```bash
python main.py
```
Type questions; use `quit` or `exit` to terminate.

## Example
```
EduBot: Hello! Ask me anything (type 'quit' to exit)
You: scholarship options abroad
EduBot: You can explore merit-based international scholarships...
You: thanks
EduBot: You're welcome!
You: quit
EduBot: Goodbye!
```

## Project Structure
```
Rule-Based-Chatbot/
├── main.py
├── intents.json
├── pyproject.toml
└── README.md
```

## intents.json Schema (excerpt)
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey"],
      "responses": ["Hello!", "Hi there!"]
    }
  ],
  "fallback": "Sorry, I did not understand that."
}
```

## Limitations
- Any-token match can cause false positives.
- No context memory.
- Order / priority not enforced (first matching intent wins).

## Possible Improvements
- Use lemmatization / stopword filtering.
- Add scoring (token overlap count) instead of first match.
- Introduce context state or slot filling.

## License
MIT (see root LICENSE if present).

## Contributions
PRs and issues welcome.

## Acknowledgements
-