You are tasked with developing a text preprocessing module for a sentiment analysis system that analyzes customer reviews of a new smartphone. One key step in your module is to remove URLs from the text, as they are not useful for sentiment analysis and could potentially skew the results.

Given a sample review:
"I just bought the new SuperPhone and it's amazing! Check out the specs here: http://www.superphone.com/specs. Best purchase I've made!"

Which of the following regular expressions would be most effective for identifying and removing the URL from this review text?

1. `http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+`
2. `http[s]?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}\\b/[-a-zA-Z0-9@:%_+.~#?&//=]*`
3. `www\\.[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}`
4. `http[s]?://[\\w-]+(\\.[\\w-]+)+[/#?]?.*$`
5. `^[http[s]?://|www\\.]([a-zA-Z0-9]+[.-]?)+[a-zA-Z0-9]{2,6}([/\\w-./?%&=]*)?$`