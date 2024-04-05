import os
import re

from rich import print

DIRECTORY = "./responsebuffers/userstudy-quiz-cs5246"

for filepath in [os.path.join(DIRECTORY, fname) for fname in os.listdir(DIRECTORY)]:
    with open(filepath, "r") as file:
        contents = file.read()
        contents = re.split("## Question|## Solution|## Correct Answer|## Reasoning", contents)
        contents = list(filter(lambda x: x, contents))
        contents = list(map(lambda x: x.strip(), contents))
        # the order is question, solution, correct answer, reasoning

    dirpath = filepath[:-3]
    os.mkdir(dirpath)

    for content, fname in zip(contents, ["question.md", "solution.md", "correct answer.md", "reasoning.md"]):
        with open(os.path.join(dirpath, fname), "w+") as file:
            file.write(content)
