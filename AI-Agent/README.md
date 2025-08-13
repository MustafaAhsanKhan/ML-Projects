# AI Educational Agent

This project implements an AI agent that serves as an educational assistant, focusing specifically on education-related topics such as study abroad programs, universities, scholarships, academic life, and exams.

## Features

- **Education-Focused Responses**: The agent only responds to education-related queries
- **Real-time Stream Output**: Text is displayed word by word for a more natural conversation experience
- **Simple CLI Interface**: Easy-to-use command-line interface for interactions
- **OpenRouter Integration**: Uses the DeepSeek model via OpenRouter API

## How It Works

The project uses:
- `langchain` and `langgraph` for agent creation and orchestration
- ReAct (Reasoning and Acting) framework for improved agent responses
- OpenAI API via OpenRouter for accessing the DeepSeek language model
- Environment variable management for API key security

## Requirements

### Prerequisites
- Python 3.13+
- OpenRouter API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-educational-agent.git
   cd ai-educational-agent
   ```

2. Set up a virtual environment using UV:
   ```bash
   pip install uv
   uv venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`

4. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
   
   Alternatively, you can use:
   ```bash
   uv pip install .
   ```

5. Create a `.env` file with your API key:
   ```
   OPENAI_API_KEY=your_openrouter_api_key_here
   ```

## Usage

1. Activate your virtual environment if not already active.

2. Run the main script:
   ```bash
   python main.py
   ```

3. Interact with the AI agent:
   - Type your education-related questions
   - Type 'exit' to quit the program

Example conversation:
```
Welcome to the AI Agent!
Type 'exit' to quit the program.

You: What are the best universities for computer science in the US?

AI: Some of the top universities for computer science in the US include MIT, Stanford, Carnegie Mellon University, UC Berkeley, and Caltech. These institutions are known for their cutting-edge research, distinguished faculty, and excellent job placement rates. Would you like more specific information about any of these universities or details about their computer science programs?
```

## Project Structure

```
AI-Agent/
├── .env                 # Environment variables (API keys)
├── .python-version      # Python version specification
├── main.py             # Main application code
├── pyproject.toml      # Project dependencies
├── README.md          # Project documentation
└── uv.lock            # UV lock file for dependencies
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) for the agent framework
- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- [OpenRouter](https://openrouter.ai/) for API access to various LLMs