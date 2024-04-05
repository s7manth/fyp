The key to solving this question lies in understanding how different techniques can influence the weight or presence of words in text data during pre-processing or feature extraction, specifically in the context of Naive Bayes models for sentiment analysis.

1. **Over-sampling the minority class:** This technique is used to balance class distribution in the training dataset and does not directly affect the impact of commonly occurring words on the model's performance.
   
2. **Applying Term Frequency-Inverse Document Frequency (TF-IDF) weighting:** TF-IDF reduces the weight of words that appear frequently across documents (reviews, in this case), hence diminishing their influence on the classifier's decision. This is achieved by considering not just the frequency of a word in a single document (term frequency) but also how common the word is across all documents (inverse document frequency). This seems like a promising solution.
   
3. **Increasing the Laplace smoothing parameter:** Laplace (or Add-one) smoothing is used to address the issue of zero probabilities in Naive Bayes models for words that haven't been seen in the training set. While it can affect the scores of words, it does not specifically target commonly occurring non-informative words in the context described.
   
4. **Using a stop-words list to completely remove common words before training:** This approach directly removes common words believed to be non-contributory towards the sentiment expressed in the texts. It's a brute-force method that can effectively address the issue but may also remove words that could have contextual sentiment value in some cases.
   
5. **Employing a word embedding model trained on a large corpus of text:** Word embeddings provide dense vector representations of words capturing semantic similarities. While powerful for many NLP tasks, choosing embedding models does not inherently solve the issue of diminishing the impact of frequently occurring non-informative words in the model's decision process as described.

The most appropriate solution that directly addresses the described problem by adjusting the contribution of words based on their document frequency, and hence, minimizing the influence of commonly occurring non-contributory words, is **Applying Term Frequency-Inverse Document Frequency (TF-IDF) weighting**.