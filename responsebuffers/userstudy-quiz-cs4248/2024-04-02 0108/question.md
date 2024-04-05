In the context of using Naive Bayes for sentiment analysis on movie reviews, suppose you're optimizing your model to distinguish between positive and negative reviews. After initial training, you notice that certain commonly occurring words (e.g., 'the', 'is', 'at') are overly influencing the classification results, leading to inaccuracies. To address this issue, you consider applying a technique that adjusts the contribution of words based on their frequency across documents. Which of the following techniques could best address this problem by minimizing the impact of commonly occurring words that don’t contribute much to the overall sentiment?

1. Over-sampling the minority class in your training dataset.
2. Applying Term Frequency-Inverse Document Frequency (TF-IDF) weighting.
3. Increasing the Laplace smoothing parameter.
4. Using a stop-words list to completely remove common words before training.
5. Employing a word embedding model trained on a large corpus of text.