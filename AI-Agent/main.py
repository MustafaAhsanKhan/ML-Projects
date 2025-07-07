from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
)

completion = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {
            "role": "user",
            "content": "Explain how recursion works in Python."
        }
    ],
)

print(completion.choices[0].message.content)
