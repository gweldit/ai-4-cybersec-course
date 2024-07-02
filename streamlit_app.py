import re

import streamlit as st


def preprocess_text(text):
    # Remove all the special characters
    processed_text = re.sub(r"\\W", " ", text)

    # Remove all single characters
    processed_text = re.sub(r"\\s+[a-zA-Z]\\s+", " ", processed_text)

    # Remove single characters from the start
    processed_text = re.sub(r"\\^[a-zA-Z]\\s+", " ", processed_text)

    # Substituting multiple spaces with single space
    processed_text = re.sub(r"\\s+", " ", processed_text, flags=re.I)

    # Removing prefixed 'b'
    processed_text = re.sub(r"^b\\s+", "", processed_text)

    # Converting to Lowercase
    processed_text = processed_text.lower()

    return processed_text


# Create a text input
text = st.text_input("Enter your text")

# Preprocess the text
processed_text = preprocess_text(text)

# Display the preprocessed text
st.write(processed_text)
