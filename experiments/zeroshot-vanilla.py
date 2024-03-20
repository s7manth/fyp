"""
File: zeroshot-vanilla.py
Description: zero shot prompting using openai api
"""

# constants
MODEL = "gpt-4-0125-preview"

SYSTEM_PROMPT = "./prompts/zeroshot-vanilla-system-prompt.txt"
USER_PROMPT = "./prompts/zeroshot-vanilla-user-prompt-template.txt"

# TEMPERATURE = 1.0
TOP_P = 0.9
MAX_TOKENS = 4096

RESPONSE = lambda timestamp: f"./responsebuffers/zeroshot-vanilla-gpt4/test/{timestamp}.md"

import openai
import os

from datetime import datetime
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

# read in the prompt files
system_prompt = str()
with open(SYSTEM_PROMPT, "r") as file:
  system_prompt = file.read()

user_prompt = str()
with open(USER_PROMPT, "r") as file:
  user_prompt = file.read()

# initialize an openai client
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORGANIZATON")
)

print("sending request...")

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "system",
      "content": system_prompt
    },
    {
      "role": "user",
      "content": user_prompt
    },
  ],
  top_p=TOP_P,
  max_tokens=MAX_TOKENS,
)

response = str(completion.choices[0].message.content)
response_file = RESPONSE(datetime.now().strftime("%Y-%m-%d %H%M"))

with open(response_file, "w+") as file:
  file.write(response)

print(f"response written to file {response_file}")
