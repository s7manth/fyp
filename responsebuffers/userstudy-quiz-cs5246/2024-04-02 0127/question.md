You are working on a sentiment analysis project where your task involves preprocessing a large dataset of customer reviews for a machine learning model. The reviews are stored as strings in a dataset, with some reviews containing URLs, email addresses, and various forms of punctuation that you intend to clean up. You decide to use regular expressions (regex) to streamline the preprocessing phase. Given the scenario, which of the following regex patterns accurately identifies and allows for the removal of URLs and email addresses without significantly impacting other text content?

1. `r'\S*@\S*\s|\bhttp:\/\/\S+'`
2. `r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|\bhttps?://\S+'`
3. `r'@\S+|\bhttp\S+'`
4. `r'\S*@\S*\s|\bhttps?://\S+\b'`
5. `r'\b[A-Za-z]+@\S+|\bhttp\S+'`