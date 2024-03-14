"""
File: fewshot-vanilla.py
Description: few shot prompting using openai api
"""

# constants
MODEL = "gpt-4-1106-preview"

# few shot prompting
# SYSTEM_PROMPT = ""
PROMPT_PREFACE_FILE_PATH = "./prompts/vanilla-prompt-few-shot-preface.txt"
TOPIC = "Feed Forward Neural Networks in NLP using PyTorch"
PROMPT_EXAMPLES_FILE_PATH = "./prompts/few-shot-examples.txt"
RESPONSE_FILE_PATH = lambda timestamp: f"./responsebuffers/{timestamp} (vanilla-few-shot).txt"

import openai
import os

from datetime import datetime
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

prompt = str()
with open(PROMPT_PREFACE_FILE_PATH, "r+") as file:
  prompt = file.read()
  prompt = prompt.replace("<<TOPIC>>", TOPIC)

with open(PROMPT_EXAMPLES_FILE_PATH, "r+") as file:
  prompt += file.read()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORGANIZATON")
)

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "system",
      "content": f"You are a highly skilled subject matter expert in {TOPIC} and a creative question architect.",
    },
    {
      "role": "user",
      "content": prompt
    },
  ],
  temperature=0.8,
  max_tokens=4096,
)

response = str(completion.choices[0].message.content)

with open(RESPONSE_FILE_PATH(datetime.now().strftime("%d-%m-%Y %H:%M:%S")), "w+") as file:
  file.write(response)
