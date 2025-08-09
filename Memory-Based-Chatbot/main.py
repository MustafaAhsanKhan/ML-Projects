from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
import os
import time

load_dotenv()

def main():
    model = ChatOpenAI(
        temperature=0,
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
        model="deepseek/deepseek-r1-0528:free"
    )

    prompt = "You are an educational assistant focused strictly on education-related topics, especially study abroad programs, universities, scholarships, academic life, exams, etc. If the user asks anything unrelated to education or study abroad, politely respond that you can only help with educational questions."
    tools = []

    # Create the agent
    agent_executor = create_react_agent(model, tools, prompt=prompt)

    # Create memory to store chat history
    memory = ConversationBufferMemory(return_messages=True)

    print("Welcome to the AI Agent with Memory!\nType 'exit' to quit the program.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Exiting the AI Agent. Goodbye!")
            break

        # Add user message to memory
        memory.chat_memory.add_message(HumanMessage(content=user_input))

        # Send the entire chat history to the agent
        all_messages = memory.chat_memory.messages
        print("\nAI: ", end="")
        for chunk in agent_executor.stream({"messages": all_messages}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    # Add AI message to memory
                    memory.chat_memory.add_message(AIMessage(content=message.content))

                    words = message.content.split()
                    for word in words:
                        print(word, end=" ", flush=True)
                        time.sleep(0.05)  # Printing delay
        print()

if __name__ == "__main__":
    main()
