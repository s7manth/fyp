import json
import os
import sys

from collections import defaultdict
from pprint import pprint as print

from constants import topics

directory = sys.argv[1]

all_files = defaultdict(list)

for path, subdirs, files in os.walk(directory):
    if path.endswith("test"): continue
    for name in files:
        if name.startswith("."): continue

        all_files[path].append(os.path.join(path, name))

jsonobject = lambda system_prompt, question, response: {"system_prompt": system_prompt, "question": question, "response": response}


SYSTEM_PROMPT = "./prompts/zeroshot-vanilla-system-prompt.txt"
USER_PROMPT = "./prompts/zeroshot-vanilla-user-prompt-template.txt"

# read in the prompt files
system_prompt = str()
with open(SYSTEM_PROMPT, "r") as file:
  system_prompt = file.read()

user_prompt = str()
with open(USER_PROMPT, "r") as file:
  user_prompt = file.read()

for subdir in all_files:
    modified_user_prompt = user_prompt + topics[subdir[-2:]]

    for file in all_files[subdir]:
        with open(file, "r") as f:
            response = f.read()
            obj = jsonobject(system_prompt, modified_user_prompt, response)

        with open("./utils/test.jsonl", "a") as f:
            f.write(json.dumps(obj) + "\n")
