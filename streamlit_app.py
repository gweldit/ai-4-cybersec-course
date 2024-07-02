import re

import joblib
import streamlit as st
import torch

from models import Perceptron


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


def load_model(input_size, output_size=1):
    # create an architecture to load the saved weights
    model = Perceptron(input_size, output_size)
    model.load_state_dict(torch.load("classifier.pt"))
    # set model in eval mode
    model.eval()
    return model


# Create a text input
text = st.text_input("For One Email, Enter Your Text:")

# Preprocess the text
processed_text = preprocess_text(text)

# Display the preprocessed text
st.write(processed_text)


# first read the email from the user input
# email = st.text_input("Enter Your Email:")
# preprocess the email
# email = preprocess_text(email)

# load countvectorizer and extract features from the email using countvectorizer
loaded_vectorizer = joblib.load("vectorizer.joblib")
X = loaded_vectorizer.transform([processed_text]).toarray()
# print(X.shape)
# load and normalized the extracted features
loaded_scaler = joblib.load("scaler.joblib")
normalized_X = loaded_scaler.transform(X)
# print("shape of normalized X: ", X.shape)
# load pytorch model (classifier) and predict the class of the email
input_size = normalized_X.shape[1]
model = load_model(input_size, 1)

# convert normalized_X from numpy to pytorch Tensor
normalized_X = torch.from_numpy(normalized_X).float()

pred = model(normalized_X)
# display the predicted class on streamlit app
label = "malware" if torch.round(pred) == 1 else "normal"
st.write(
    f"Email is classified as = {label}, with probability = {pred.item() * 100:.3f}%"
)
