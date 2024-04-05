In an effort to improve the search functionality of an online news portal, a data scientist is tasked with developing a system that categorizes news articles into predefined topics such as 'Politics', 'Economics', 'Technology', etc. To achieve this, the scientist decides to utilize a K-Nearest Neighbors (KNN) classification algorithm based on the similarity of text content. Before implementing this model, they perform preprocessing steps including tokenization, stop-word removal, and TF-IDF vectorization on the corpus of articles.

Given a new, unseen article, the KNN algorithm will classify it by:

1. Calculating its Euclidean distance from every article in the training set and selecting the K articles with the smallest distances.
2. Identifying the most frequent label among the K nearest neighbors and assigning it to the new article.
3. Averaging the TF-IDF vectors of the K nearest neighbors and assigning the label of the closest vector to the new article.
4. Calculating the cosine similarity between the new article and every article in the training set, selecting the K articles with the highest similarity scores.
5. Utilizing a majority vote among the K nearest neighbors based on Jaccard similarity to determine the article's category.