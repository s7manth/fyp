A data scientist is working on preprocessing a large dataset of customer reviews to improve the performance of a sentiment analysis model. The dataset contains numerous instances of non-standard words, emojis, and various types of noise. The data scientist decides to clean the text data using Python. Which of the following regular expression (regex) patterns and methods is most appropriate for removing emojis, leaving standard text, numerical characters, basic punctuation marks (.,!?"), and whitespace intact?

1. `re.sub(r'[^\w\s.,!?"]', '', text)`
2. `re.sub(r'[\U00010000-\U0010ffff]', '', text)`
3. `re.sub(r'[\u2600-\u26FF\u2700-\u27BF]', '', text)`
4. `re.sub(r'[^a-zA-Z0-9\s.,!?"]', '', text)`
5. `re.sub(r'[\w\s.,!?"]', '', text)`