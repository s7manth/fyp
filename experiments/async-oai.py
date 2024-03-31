import openai
import asyncio
import time
import aiohttp
import os
import math

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
        ans = await asyncio.wait_for(task, timeout=20 * math.log(10 + tries, 2))
        return ans
    except:
        tries += 1
        if tries < 6:
            delay = 2 * (2 ** tries)
            time.sleep(delay)
            ans = await waiting_code(task, tries)
            return ans
        else:
            print("ERROR: failed waiting")
            return []

NUMBER_OF_COMPLETIONS_PER_TOPIC = 10
async def main():
    tasks = []
    tids = []
    for tid, ts in topics.items():
        print(f"INFO: generating for topics {tid} {ts}")
        for _ in range(NUMBER_OF_COMPLETIONS_PER_TOPIC):
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
            tids.append(tid)

    try:
        for coro, tid in tqdm(zip(tasks, tids), total=len(tasks)):
            completion = await waiting_code(coro, 0)
            completions.append({
                "completion": completion,
                "tid": tid
            })

        return completions
    except:
        print("ERROR: something went wrong lmao")

loop = asyncio.new_event_loop()
completions = loop.run_until_complete(main())

for i, cobj in enumerate(completions):
    completion = cobj["completion"]
    tid = cobj["tid"]

    if completion == []: continue

    response = str(completion.choices[0].message.content)
    response_file = RESPONSE((datetime.now() + timedelta(minutes=i)).strftime("%Y-%m-%d %H%M"), tid)

    with open(response_file, "w+") as file:
        file.write(response)

    print(f"response written to file {response_file}")
