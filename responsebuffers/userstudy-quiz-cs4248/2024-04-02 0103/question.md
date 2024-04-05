In an effort to improve the effectiveness of a search engine, an NLP specialist decides to enhance the preprocessing pipeline with algorithms for text normalization and word tokenization. The specialist wishes to ensure that the search engine can effectively handle various forms of the same words, improving both retrieval accuracy and user satisfaction. Consider the following text snippet from the search engine's database:

```
"Email is not only one of the oldest forms of online communication but also vastly prevalent across diverse domains. E-mail, often seen as a more formal variation, serves similar purposes."
```

The goal is to transform this text in a way that enhances word matching while preserving the unique contextual meanings of variations such as "Email" and "E-mail". Which combination of preprocessing steps would best achieve this goal?

1. Apply lowercasing, followed by a stemming algorithm, and finally perform sentence segmentation.
2. Perform sentence segmentation, apply a lemmatization algorithm, and then remove stop words.
3. Normalize spelling variations (e.g., "E-mail" to "Email"), apply lowercasing, and then perform word tokenization.
4. Use a regular expression to tokenize the text based on punctuation and whitespace, followed by applying a Named Entity Recognition (NER) algorithm.
5. First apply a context-aware spelling correction algorithm, then lemmatize the text, and finally apply lowercasing.