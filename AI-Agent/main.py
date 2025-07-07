from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
from langchain_openai import OpenAIEmbeddings
import os

load_dotenv()


def main():

    model = ChatOpenAI(
        temperature=0,
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
        model="deepseek/deepseek-r1-0528:free")
    prompt = "You are an educational assistant focused strictly on education-related topics, especially study abroad programs, universities, scholarships, academic life, exams, etc. If the user asks anything unrelated to education or study abroad, politely respond that you can only help with educational questions."
    tools = []
    agent_executor = create_react_agent(model, tools, prompt=prompt)

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