import os
import random

MODULE = "4248"

FOLDER = f"./responsebuffers/blooms-{MODULE}"

all = list()

for topic in os.listdir(FOLDER):
    for tax in os.listdir(os.path.join(FOLDER, topic)):
        for file in os.listdir(os.path.join(FOLDER, topic, tax)):
            all.append(os.path.join(FOLDER, topic, tax, file))

random.shuffle(all)

for id, file in enumerate(all):
    print(f"{id + 1} -> {file}")
