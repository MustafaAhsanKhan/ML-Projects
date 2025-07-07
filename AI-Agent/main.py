from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

@tool


def main():
    model = ChatOpenAI(
    temperature=0,
    base_url="https://openrouter.ai/api/v1",  # ✅ Force use of OpenRouter
    api_key=os.getenv("OPENAI_API_KEY"),       # ✅ Load from your .env
    model="deepseek/deepseek-r1-0528:free"  # ✅ Use correct model name
)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome to the AI Agent!\nType 'exit' to quit the program.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Exiting the AI Agent. Goodbye!")
            break
        
        print("\nAI: " , end = "")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()