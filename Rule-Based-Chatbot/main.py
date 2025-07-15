import nltk
import json
import random
import nltk
import re


nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# Preprocess input by tokenizing
def preprocess(text):
    return word_tokenize(text.lower())

# Match input with patterns
def match_intent(user_input):
    tokens = preprocess(user_input)
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess(pattern)
            if any(word in tokens for word in pattern_tokens):
                return random.choice(intent["responses"])
    return intents["fallback"]

# Chat loop
def chat():
    print("EduBot: Hello! Ask me anything (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("EduBot: Goodbye!")
            break
        response = match_intent(user_input)
        print("EduBot:", response)

if __name__ == "__main__":
    chat()
