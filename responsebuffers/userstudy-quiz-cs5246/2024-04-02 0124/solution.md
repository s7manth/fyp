The task at hand is to clean the text data by removing all emojis while keeping standard English text characters, numerical characters, basic punctuation marks (.,!?"), and whitespace. Regex can be used to match patterns of text for the purpose of replacing or removing them.

1. `re.sub(r'[^\w\s.,!?"]', '', text)`: This pattern inverts the match using `^` within `[]`, targeting everything except word characters (`\w`), whitespace (`\s`), and the specified punctuation marks. This is a strong candidate because it aims to preserve the characters mentioned in the problem statement while removing others, which includes most emojis.

2. `re.sub(r'[\U00010000-\U0010ffff]', '', text)`: This pattern targets a specific range of Unicode characters typically associated with emojis and other non-standard text symbols. However, it may not capture all emojis, as emojis can be found in other Unicode ranges as well. 

3. `re.sub(r'[\u2600-\u26FF\u2700-\u27BF]', '', text)`: This pattern specifically targets two Unicode blocks commonly associated with miscellaneous symbols and dingbats, which include many emojis. Like option 2, it may not remove all emojis since emojis span multiple Unicode blocks.

4. `re.sub(r'[^a-zA-Z0-9\s.,!?"]', '', text)`: This pattern is similar to option 1, but it explicitly lists English alphabet characters (both uppercase and lowercase) and numerical characters instead of using the shorthand word character (`\w`). This option is practically equivalent to option 1 for the purpose of this task, with the minor distinction that `\w` also includes underscore (`_`), which isn't specified as retainable in the problem statement. Thus, depending on whether the underscore character is considered noise or not, there might be a slight preference.

5. `re.sub(r'[\w\s.,!?"]', '', text)`: This pattern is incorrect for the task because it removes everything that should be kept (i.e., English text characters, numerical characters, basic punctuation, and whitespace) by directly targeting these characters without inversion.

Given the task's requirements, option 1 and option 4 are both technically correct answers, with a slight nuance regarding the handling of the underscore character. However, option 1 is more inclusive by leveraging `\w`, which simplifies the regex and encompasses a wider array of word characters. Therefore, the best answer is option 1.