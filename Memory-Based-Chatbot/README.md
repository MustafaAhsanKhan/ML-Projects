# Memory Based Chatbot

Interactive CLI educational assistant with short‑term conversational memory. Focused strictly on education (study abroad, universities, scholarships, academic life, exams) and declines non‑educational queries.

## Features
- Education‑only scope enforcement
- ConversationBufferMemory retains prior turns (session memory)
- ReAct agent via LangChain + LangGraph
- Word‑by‑word streaming output
- OpenRouter DeepSeek model integration
- Simple, dependency‑light CLI

## How It Works
- Chat history stored in `ConversationBufferMemory` (in‑memory only)
- Entire message list passed each turn to the ReAct agent (`create_react_agent`)
- Streaming loop prints agent tokens word by word with slight delay
- System prompt restricts domain to educational content

## Requirements
### Prerequisites
- Python 3.13+
- OpenRouter API key (exported as OPENAI_API_KEY)

### Installation
```bash
# From monorepo root
cd Memory-Based-Chatbot
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate

uv pip install -r requirements.txt   # or: uv pip install .
```

Create `.env`:
```
OPENAI_API_KEY=your_openrouter_key
```

## Usage
```bash
python main.py
```
- Ask education‑related questions
- Type `exit` to quit
- Memory resets when the process ends

## Example
```
You: Recommend scholarships for international undergraduates in Germany.
AI: DAAD undergraduate options are limited, but look at ... Would you like application timeline guidance?
You: Yes, timeline please.
AI: Typical sequence: (1) Program shortlist (2) Collect transcripts ...
```

## Project Structure
```
Memory-Based-Chatbot/
├── main.py
├── pyproject.toml
├── README.md
├── .env                # (not committed) API key
└── uv.lock             # Dependency lock (if generated)
```

## Extending
- Swap memory for `ConversationBufferWindowMemory` to cap context
- Add persistence (e.g., SQLite or JSON) for multi‑session recall
- Plug in tools (search, retrieval) by supplying a tools list to the agent

## License
MIT (see root LICENSE if present).

## Contributions
Issues and PRs welcome.

## Acknowledgements
- LangChain / LangGraph
- OpenRouter
-