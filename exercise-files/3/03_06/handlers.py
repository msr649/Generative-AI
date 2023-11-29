import openai
import os
import json
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
client = openai.OpenAI()

# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a helpful assistant"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]


def print_messages(messages):
    messages = [
        json.dumps(message) for message in messages if message["role"] != "system"
    ]
    for message in messages:
        m = json.loads(message)
        role = "Bot" if m["role"] == "assistant" else "You"
        print(Fore.BLUE + role + ": " + m["content"])
    return messages


def generate_chat_completion(user_input=""):
    pass
