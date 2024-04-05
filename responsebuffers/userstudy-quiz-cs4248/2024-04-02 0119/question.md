You are working on a Named Entity Recognition (NER) system that aims to accurately identify and classify named entities in financial news articles into categories such as "Organization," "Person," "Financial Metric," and "Location." After training an initial model using Conditional Random Fields (CRFs), you notice that while the model performs well on common entity types like "Person" and "Location," it struggles with "Financial Metric," often confusing it with general numeric entities or dates.

To improve your model's performance on "Financial Metric" entities, which of the following strategies would most likely enhance its accuracy?

1. Increase the size of the training dataset by adding more financial news articles without specifically focusing on "Financial Metric" entities.
2. Incorporate feature engineering to include context-specific signal words (e.g., "revenue," "profit," "loss") and common financial symbols (e.g., "$," "%") adjacent to numeric entities.
3. Shift from using CRFs to a simpler Part-of-Speech (POS) tagging technique, given its specialized focus on tagging individual words.
4. Apply more rigorous pre-processing steps, such as stop-word removal and case normalization, to reduce the feature space and potentially increase the model's focus on numeric entities.
5. Enhance the training process by including a more diverse set of named entity recognition tools, such as HMM-based taggers, alongside CRFs to leverage ensemble learning effects.