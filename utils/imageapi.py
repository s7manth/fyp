
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="A vector of human face without identity",
  size="1024x1024",
  quality="hd",
  style="vivid",
  n=1,
)

image_url = response.data[0].url
print(image_url)
