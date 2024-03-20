SYSTEM_PROMPT = """
You are a lecturer for an advanced undergraduate natural language processing course. Your task is to evaluate
a plausible candidate for an assessment-grade multiple choice question rigorously. You should first understand
the question, the assumptions, and carefully evaluate the options given to choose the correct one.

If the question doesn't make sense, or has an error, point out the error and explain your reasoning behind it.
If the question is valid, just give the correct option choice.
"""

USER_PROMPT = """
## Question

Suppose we have a binary classification problem where we want to predict whether a given email is spam or not. We have a dataset of features such as the words used in the email, the sender's address, and other factors. Our goal is to train a model that can accurately classify new emails based on these features.

Which of the following logistic regression models would be most appropriate for this problem?
## Options

1. Binary Logistic Regression
2. Multinomial Logistic Regression
3. Polynomial Logistic Regression
4. Ridge Logistic Regression
5. Lasso Logistic Regression
"""

SYSTEM_PROMPT = """

"""

USER_PROMPT = """
The dialogue above is from **ELIZA**, an early natural language processing system
ELIZA
that could carry on a limited conversation with a user by imitating the responses of a Rogerian psychotherapist (Weizenbaum, 1966). ELIZA is a surprisingly simple program that uses pattern matching to recognize phrases like "I need X" and translate them into suitable outputs like "What would it mean to you if you got X?". This simple technique succeeds in this domain because ELIZA doesn't actually need to know anything to mimic a Rogerian psychotherapist. As Weizenbaum notes, this is one of the few dialogue genres where listeners can act as if they know nothing of the world. ELIZA's mimicry of human conversation was remarkably successful: many people who interacted with ELIZA came to believe that it really *understood* them and their problems, many continued to believe in ELIZA's abilities even after the program's operation was explained to them (Weizenbaum, 1976), and even today
such **chatbots** are a fun diversion.
chatbots
Of course modern conversational agents are much more than a diversion; they can answer questions, book flights, or find restaurants, functions for which they rely on a much more sophisticated understanding of the user's intent, as we will see in Chapter 15. Nonetheless, the simple pattern-based methods that powered ELIZA and other chatbots play a crucial role in natural language processing.
"""


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(".env")
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORGANIZATON")
)

completion = client.chat.completions.create(
  model="gpt-4-0125-preview",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_PROMPT}
  ],
  top_p=0.9
)

print(completion.choices[0].message.content)
