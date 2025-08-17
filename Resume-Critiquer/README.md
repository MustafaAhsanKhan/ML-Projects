# Resume Critiquer

Streamlit app that ingests a PDF or TXT resume and produces structured, role‑aware improvement feedback via an OpenRouter‑hosted LLM (DeepSeek). Focuses on actionable recommendations (clarity, impact, skills, experience).

## Features
- PDF / TXT upload with text extraction (PyPDF2 for PDFs)
- Role‑specific guidance (optional target job role field)
- Structured AI critique (content clarity, skills, experience, improvements)
- OpenRouter DeepSeek model integration (chat completion)
- Simple, single‑file Streamlit UI

## How It Works
1. User uploads a resume (PDF/TXT) + optional job role.
2. Text extracted:
   - PDF: iterates pages with `PyPDF2.PdfReader`
   - TXT: direct decode
3. A structured prompt is assembled and sent to the OpenRouter endpoint (`deepseek/deepseek-r1-0528:free`).
4. Response displayed as formatted markdown.
5. Basic validation: empty/failed extraction triggers an error message.

## Requirements
### Prerequisites
- Python 3.13+
- OpenRouter API key (exported as OPENAI_API_KEY)

### Key Dependencies
- streamlit
- PyPDF2
- openai (SDK for calling OpenRouter-compatible endpoint)
- python-dotenv

## Installation
```bash
# From monorepo root
cd Resume-Critiquer
uv venv
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate

uv pip install -r requirements.txt   # or: uv pip install .
```

Create `.env`:
```
OPENAI_API_KEY=your_openrouter_api_key_here
```

## Usage
```bash
streamlit run main.py
```
1. Upload a PDF or TXT resume.
2. (Optional) Enter the job role (e.g., "Data Analyst", "Backend Engineer").
3. Click Analyze Resume.
4. Read structured feedback under "AI Feedback".

## Example Prompt (Internal)
The app composes a prompt requesting:
- Content clarity & impact
- Skills presentation
- Experience description quality
- Tailored improvements for the specified role (or general applications)

## Project Structure
```
Resume-Critiquer/
├── main.py          # Streamlit application
├── pyproject.toml   # Project metadata & dependencies
├── README.md        # This documentation
└── (optional) uv.lock
```

## Environment Variables
- OPENAI_API_KEY: OpenRouter API key used by the OpenAI SDK with base_url override.

## Extending
- Add DOCX parsing (e.g., python-docx).
- Enable streaming responses (`stream=True`).
- Add export (download JSON or markdown report).
- Integrate keyword gap analysis vs. target job description.

## Troubleshooting
- Empty output: ensure file is readable (scanned PDFs without text need OCR).
- Auth errors: verify OPENAI_API_KEY and network access.
- Rate limits: switch to a paid tier or add retry logic.

## License
MIT (see root LICENSE if present).

## Contributions
Issues and pull requests welcome.

## Acknowledgements
- Streamlit
- PyPDF2
- OpenRouter / DeepSeek model providers
- OpenAI Python SDK (for compatible API interface)