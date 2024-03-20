import requests
import json

# from constants import topics
# from time import sleep

# clear = "\x1B[2J\x1B[1;1H"
# for tid, ts in list(topics.items()):
#     print(f"{clear} {ts}")
#     sleep(1)

SYSTEM_PROMPT = "./prompts/zeroshot-vanilla-system-prompt.txt"
USER_PROMPT = "./prompts/zeroshot-vanilla-user-prompt.txt"

# read in the prompt files
system_prompt = str()
with open(SYSTEM_PROMPT, "r") as file:
  system_prompt = file.read()

user_prompt = str()
with open(USER_PROMPT, "r") as file:
  user_prompt = file.read()

URL = "http://localhost:8997"

def get_all_available_models():
    r = requests.get(URL + "/api/tags")
    r = r.json()
    return [md["model"] for md in r["models"]]

def create_chat_completion(model, system_prompt, user_prompt, top_p, top_k):
    payload = {
        'model': model,
        'system': system_prompt,
        'prompt': user_prompt,
        "options": {
            "temperature": 1.0
        }
    }

    r = requests.post(URL + "/api/generate", json=payload, stream=True)
    r.raise_for_status()
    complete_response = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if body.get("done", False):
            return complete_response

        response_part = body.get("response", "")
        complete_response += response_part
        # the response streams one token at a time, print that as we receive it
        print(response_part, end="", flush=True)

    return complete_response

create_chat_completion("llama2:13b", system_prompt, user_prompt, 0.9, 100)
