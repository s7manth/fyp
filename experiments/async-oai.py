import openai
import asyncio
import time
import aiohttp
import os

from itertools import islice
from tqdm import tqdm
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv(".env")

from constants import topics

# constants
MODEL = "gpt-4-0125-preview"

SYSTEM_PROMPT = "./prompts/zeroshot-vanilla-system-prompt.txt"
USER_PROMPT = "./prompts/zeroshot-vanilla-user-prompt-template.txt"

# TEMPERATURE = 1.0
TOP_P = 0.9
MAX_TOKENS = 4096

RESPONSE = lambda timestamp, tid: f"./responsebuffers/zeroshot-vanilla-gpt4/{tid}/{timestamp}.md"

# read in the prompt files
system_prompt = str()
with open(SYSTEM_PROMPT, "r") as file:
  system_prompt = file.read()

user_prompt = str()
with open(USER_PROMPT, "r") as file:
  user_prompt = file.read()

# initialize an openai client
client = openai.AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORGANIZATON")
)

def backoff_delay(backoff_factor, attempts):
    # backoff algorithm
    delay = backoff_factor * (2 ** attempts)
    return delay

def retry_request():
    pass

completions = []

async def waiting_code(task, tries):
    try:
        ans = await asyncio.wait_for(task, timeout=15)
        return ans
    except:
        tries += 1
        if tries < 4:
            delay = 2 * (2 ** tries)
            time.sleep(delay)
            ans = await waiting_code(task, tries)
            return ans
        else:
            print("ERROR: failed waiting")
            return []

async def main():
    tasks = []
    for tid, ts in tqdm(islice(topics.items(), 16, 17)):
        print(ts)
        for _ in range(11):
            await asyncio.sleep(1)
            tasks.append(
                asyncio.create_task(
                    client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {
                                "role": "system",
                                "content": system_prompt,
                            },
                            {
                                "role": "user",
                                "content": user_prompt + ts,
                            }
                        ]
                    )
                )
            )

    try:
        for coro in tqdm(tasks, total=len(tasks)):
            completion = await waiting_code(coro, 0)
            completions.append(completion)

        return completions
    except:
        print("ERROR: something went wrong lmao")

loop = asyncio.new_event_loop()
completions = loop.run_until_complete(main())

for i, completion in enumerate(completions):
    if completion == []: continue

    response = str(completion.choices[0].message.content)
    response_file = RESPONSE((datetime.now() + timedelta(minutes=i)).strftime("%Y-%m-%d %H%M"), 21)

    with open(response_file, "w+") as file:
        file.write(response)

    print(f"response written to file {response_file}")
