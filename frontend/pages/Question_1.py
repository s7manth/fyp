import streamlit as st

st.markdown(
    """
    ## Question
    Consider a project where you are developing a natural language processing (NLP) system tasked with analyzing customer reviews for a multilingual e-commerce platform. The reviews are in various languages, including English, French, and Mandarin, and vary significantly in length, style, and domain-specific terminology. You are in the process of designing the initial data preprocessing pipeline to improve the efficiency and effectiveness of downstream tasks such as sentiment analysis, keyword extraction, and summarization. Given these requirements, which combination of preprocessing steps would be most effective?

    1. Applying regular expressions to remove all non-alphanumeric characters, followed by stemming for English and French reviews, and then sentence segmentation using punctuation for all reviews.
    2. Implementing a language detection step followed by language-specific tokenization, using lemmatization for English and French reviews, and applying a CRF-based (Conditional Random Fields) tokenizer for Mandarin, followed by domain-specific vocabulary normalization for all reviews.
    3. Using sentence segmentation based on punctuation for all reviews without language detection, followed by a unified grapheme cluster tokenizer for all languages, and applying a generic stop-words removal step.
    4. Applying a simple whitespace tokenizer for all reviews, followed by stemming for all languages and then removing numerals and punctuation using regular expressions.
    5. Conducting a simple Unicode normalization step for all reviews, followed by language detection, and applying a machine learning-based sentence segmentation model trained on a multilingual corpus that includes all target languages.
    """
)

st.session_state.selected_option_1 = None

if "options_disabled_1" not in st.session_state:
    st.session_state.options_disabled_1 = False

def select_option(option: str | None):
    if option is None:
        st.error("No option selected!")

    st.session_state.options_disabled_1 = True

    print(f"selected option: {option}")

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
with st.form("Select what you think is correct!"):
    st.radio(
        "Options",
        key="selected_option_1",
        index=0 if not st.session_state.selected_option_1 else options.index(st.session_state.selected_option_1),
        options=options,
        disabled=st.session_state.options_disabled_1
    )

    submitted = st.form_submit_button(
        "Submit",
        on_click=lambda: select_option(st.session_state.selected_option_1)
    )

if st.session_state.options_disabled_1:
    st.write(f"Selected: {st.session_state.selected_option_1}")
