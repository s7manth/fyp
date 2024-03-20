import tika
from tika import parser

tika.initVM()

parsed = parser.from_file("./data/raw/3.pdf", headers={
    "X-Tika-PDFocrStrategy": "auto"
})

print(parsed["metadata"])

with open("./data/cleaned/3.txt", "w") as file:
    file.write(parsed["content"])
