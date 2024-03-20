import os

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
from dotenv import load_dotenv
from constants import topics
from time import sleep

load_dotenv(".env")

os.environ["LANGCHAIN_PROJECT"] = "ollama-langchain"

SYSTEM_PROMPT = "./prompts/zeroshot-oss-vanilla-system-prompt.txt"
USER_PROMPT = "./prompts/zeroshot-vanilla-user-prompt-template.txt"

MODEL = "gemma"
TOP_P = 0.9
TOP_K = 100
MAX_TOKENS = 4096
URL = "http://localhost:8997"

RESPONSE = lambda timestamp, tid: f"./responsebuffers/zeroshot-vanilla-{MODEL}/{tid}/{timestamp}.md"

# read in the prompt files
system_prompt = str()
with open(SYSTEM_PROMPT, "r") as file:
  system_prompt = file.read()

user_prompt = str()
with open(USER_PROMPT, "r") as file:
  user_prompt = file.read()

llm = ChatOllama(
    base_url=URL,
    model=MODEL,
    num_ctx=MAX_TOKENS,
    top_p=TOP_P,
    top_k=TOP_K
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", user_prompt)
])
chain = prompt | llm | StrOutputParser()

for tid, ts in list(topics.items()):
    print(f"INFO: generating for topic: {tid}")

    for _ in range(5):
        response = str(chain.invoke({ "topics": ts }))
        response_file = RESPONSE(datetime.now().strftime("%Y-%m-%d %H%M"), tid)

        with open(response_file, "w+") as file:
            file.write(response)

        print(f"INFO: response written to file {response_file}")
        sleep(60)
