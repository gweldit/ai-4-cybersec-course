import joblib
import streamlit as st
import torch

from models import Perceptron
from preprocessing import PreprocessEmail as pr


def load_model(input_size, output_size=1):
    # create an architecture to load the saved weights
    model = Perceptron(input_size, output_size)
    # load the model or the phishing email classifier
    model.load_state_dict(torch.load("model.pt"))
    # set model in eval mode
    model.eval()
    return model


st.write("Phishing Email Detector")
# Create a text input
text = st.text_input("For One Email, Enter Your Text:")

# Preprocess the text
processed_text = pr.clean_email(text)

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
y_pred = torch.where(pred > 0.5, 1, 0)
label = "malware" if y_pred.item() == 1 else "normal"
st.write(
    f"Email is classified as = {label}, with probability = {pred.item() * 100:.3f}%"
)
