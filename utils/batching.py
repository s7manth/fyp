from dotenv import load_dotenv
load_dotenv(".env")

from itertools import islice
from random import shuffle

from constants import topics

for tid, ts in islice(topics.items(), 1):
    deconstructed = ts.strip().split("\n")
    shuffle(deconstructed)
    print("\n".join(deconstructed))
    print("*" * 50)
    shuffle(deconstructed)
    print("\n".join(deconstructed))

# from openai import OpenAI
# client = OpenAI()

# num_stories = 10
# prompts = ["Once upon a time,"] * num_stories

# response = client.completions.create(
#     model="davinci-002",
#     prompt=prompts,
#     max_tokens=20,
# )

# stories = [""] * len(prompts)
# for choice in response.choices:
#     stories[choice.index] = prompts[choice.index] + choice.text

# for story in stories:
#     print(story)
