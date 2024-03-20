from rich import print
from langchain.docstore.document import Document
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import MarkdownHeaderTextSplitter

from langchain import hub
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

from bs4 import BeautifulSoup
from markdown import markdown
import re

def markdown_to_text(markdown_string):
    html = markdown(markdown_string)
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(string=True))
    return text

load_dotenv(".env")

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

text = str()
with open("./data/cleaned/2.md", "r") as file:
    text = file.read()
    text = text.strip()
    paragraphs = text.split("\n\n")
    paragraphs = [markdown_to_text(para).replace("\n", " ") for para in paragraphs]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(text)

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="interquartile"
)

# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=100,
#     chunk_overlap=20,
#     length_function=len,
#     is_separator_regex=False,
# )
#

docs = list()

list_of_strings = [markdown_to_text(split.page_content) for split in md_header_splits]
metadatas = [split.metadata for split in md_header_splits]

for split in md_header_splits:
    docs.extend(text_splitter.create_documents(list_of_strings, metadatas=metadatas))
print(docs)
exit(0)

# print(markdown_to_text(md_header_splits[0].page_content)

MODEL = "gemma"
TOP_P = 0.9
TOP_K = 100
MAX_TOKENS = 4096
URL = "http://localhost:8997"

system_prompt = ""
user_prompt= ""

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



# print(paragraphs)

print("#### Semantic Chunking ####")

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

# Percentile - all differences between sentences are calculated, and then any difference greater than the X percentile is split
text_splitter = SemanticChunker(OpenAIEmbeddings())
text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="percentile" # "standard_deviation", "interquartile"
)
documents = text_splitter.create_documents([text])
print(documents)


# from langchain.output_parsers.openai_tools import JsonOutputToolsParser
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableLambda
# from langchain.chains import create_extraction_chain
# from typing import Optional, List
# from langchain.chains import create_extraction_chain_pydantic
# from langchain_core.pydantic_v1 import BaseModel
# from langchain import hub

# MODEL = "gpt-3.5-turbo"

# obj = hub.pull("wfh/proposal-indexing")
# llm = ChatOpenAI(model=MODEL)
# runnable = obj | llm

# class Sentences(BaseModel):
#     sentences: List[str]

# # Extraction
# extraction_chain = create_extraction_chain_pydantic(pydantic_schema=Sentences, llm=llm)
# def get_propositions(text):
#     runnable_output = runnable.invoke({
#     	"input": text
#     }).content
#     propositions = extraction_chain.invoke(runnable_output)["text"][0].sentences
#     return propositions

# text = text.strip()
# paragraphs = text.split("\n\n")

# text_propositions = []
# for i, para in enumerate(paragraphs):
#     propositions = get_propositions(para)
#     text_propositions.extend(propositions)
#     print (f"Done with {i}")

# print(text_propositions)

# print (f"You have {len(text_propositions)} propositions")
# # print(text_propositions[:10])

# print("#### Agentic Chunking ####")

# from agenticchunker import AgenticChunker
# ac = AgenticChunker()
# ac.add_propositions(text_propositions)
# print(ac.pretty_print_chunks())
# chunks = ac.get_chunks(get_type='list_of_strings')
# print(chunks)

# documents = [Document(page_content=chunk, metadata={"source": "local"}) for chunk in chunks]

print(documents)

vectorstore = Chroma.from_documents(documents=documents,
                                    embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")

llm = ChatOpenAI(model_name="gpt-4-0125-preview", n=5)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(rag_chain.invoke("""
Create 10 different multiple choice question (MCQ) and solution that covers the following topic: Text Normalization for Lemmatization
"""))
