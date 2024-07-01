import os
import re
import string
from pathlib import Path

import pandas as pd


class PreProcessData:
    @staticmethod
    def read_smish_data(self, file_path):
        """reads SMISH data from a given file path"""

        try:
            df = pd.read_csv(file_path, header=None, delimiter="\t")
            # add header to the columns of the dataframe
            df.columns = ["label", "sms_message"]
            return df
        except Exception as e:
            raise ValueError(e)

    @staticmethod
    def clean_text(text):
        # change all the text messages to a lower case
        text = text.lower()
        # remove numbers from text
        # text = re.sub(r"\d+", "", text)

        # remove punctuation from text
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Remove special characters
        text = re.sub(r"\W", " ", text)
        return text


if __name__ == "__main__":
    pr = PreProcessData()
    current_dir = os.getcwd()
    # print("curr dir = ", current_dir)
    # access parent folder
    parent_folder = Path(current_dir).absolute()

    dataset_folder = os.path.join(parent_folder, "phishing-email-dataset")
    sms_phishing_folder_path = os.path.join(dataset_folder, "smssmishcollection")

    smishing_file_path = os.path.join(
        sms_phishing_folder_path, "SMSSmishCollection.txt"
    )
    print(smishing_file_path)

    df = pr.read_smish_data(smishing_file_path)
    # # df["clean_text"] = df["sms_message"].apply(pr.clean_text)

    corpus = df["sms_message"].tolist()
    cleaned_corpus = [pr.clean_text(doc) for doc in corpus]
    df["clean_text"] = cleaned_corpus
    print(cleaned_corpus[:10])
