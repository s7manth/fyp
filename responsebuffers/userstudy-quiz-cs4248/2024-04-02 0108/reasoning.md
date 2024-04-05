TF-IDF is a feature extraction technique that transforms text into a meaningful representation of numbers which can be used in machine learning models. It does so by reducing the weight (importance) of words that appear frequently across multiple documents but provides less information about the overall sentiment or content of any specific document. This characteristic makes it especially suitable for the mentioned problem of minimizing the impact of commonly occurring non-informative words on classification outcomes in sentiment analysis tasks. By balancing term frequency with inverse document frequency, TF-IDF naturally attenuates the effect of words that do not contribute significantly to the sentiment orientation of the reviews, thus improving the model's predictive accuracy on such tasks.