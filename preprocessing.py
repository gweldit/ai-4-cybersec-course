import os
import re
import string
from pathlib import Path

import pandas as pd


class PreprocessEmail:
    @staticmethod
    def read_smish_data(file_path):
        """reads SMISH data from a given file path"""

        try:
            df = pd.read_csv(file_path, header=None, delimiter="\t")
            # add header to the columns of the dataframe
            df.columns = ["label", "sms_message"]
            return df
        except Exception as e:
            raise ValueError(e)

    @staticmethod
    def clean_email(text):
        # Convert all the text messages to a lower case
        text = text.lower()

        # Remove numbers from text
        text = re.sub(r"\d+", "", text)

        # Remove punctuation from text
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove all the special characters
        text = re.sub(r"\W", " ", text)

        # Remove all single characters
        text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)

        # Remove single characters from the start
        text = re.sub(r"^\^[a-zA-Z]\s+", " ", text)

        # Substituting multiple spaces with single space
        text = re.sub(r"\s+", " ", text, flags=re.I)

        # Removing prefixed 'b'
        text = re.sub(r"^b\s+", "", text)

        return text


if __name__ == "__main__":
    current_dir = os.getcwd()
    # print("curr dir = ", current_dir)
    # access parent folder
    parent_folder = Path(current_dir).absolute()

    # dataset_folder = os.path.join(parent_folder, "phishing-email-dataset")
    # sms_phishing_folder_path = os.path.join(dataset_folder, "smssmishcollection")

    # smishing_file_path = os.path.join(
    #     sms_phishing_folder_path, "SMSSmishCollection.txt"
    # )
    # print(smishing_file_path)

    # df = PreprocessEmail.read_smish_data(smishing_file_path)
    # # # df["clean_text"] = df["sms_message"].apply(pr.clean_text)

    # corpus = df["sms_message"].tolist()
    # cleaned_corpus = [PreprocessEmail.clean_text(doc) for doc in corpus]
    # df["clean_text"] = cleaned_corpus
    # print(cleaned_corpus[:10])
