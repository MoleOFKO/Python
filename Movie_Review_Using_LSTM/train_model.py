# Movie Review Sentiment Classifier

#----------------------------------------------
# 1. import libraries
#----------------------------------------------
import os # to define path for folder
import re # Import the regular expression module for text cleaning
import numpy as np # for numerical operations
import matplotlib.pyplot as plt # for plotting graph
import tensorflow as tf 
from tensorflow.keras.datasets import imdb
from tensorflow.keras import layers, models

#----------------------------------------------
# 2. Settings
#----------------------------------------------
# Set the maximum vocabulary size
MAX_WORDS = 10000

# Set the maximum length of each review
MAX_LENGTH = 200

# Set the maximum number of review per class for training
MAX_TRAIN_PER_CLASS = 5000

# Set the maximum number of review pre class for testing
MAX_TEST_PER_CLASS = 2500

# Define the main dataset folder
DATASET_FOLDER = "dataset"

# Create the training folder path
TRAIN_FOLDER = os.path.join(DATASET_FOLDER, "train")

# Create the testing folder path
TEST_FOLDER = os.path.join(DATASET_FOLDER, "test")

MODEL_PATH = "setiment_lstm.keras"

#----------------------------------------------
# 3. Create dataset folders
#----------------------------------------------

for folder in [
    os.path.join(TRAIN_FOLDER, "positive"),
    os.path.join(TRAIN_FOLDER, "negative"),
    os.path.join(TEST_FOLDER, "positive"),
    os.path.join(TEST_FOLDER, "negative")
]:
    # Create the folder if it does not already exits
    os.makedirs(folder, exist_ok=True) 

#----------------------------------------------
# 4. Load IMDB Dataset
#----------------------------------------------
print("Loading IMDB Dataset..........")

# Load the IMDB Dataset and keep only the top 10000 words
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = MAX_WORDS)

#----------------------------------------------
# 5. Convert IMDB numbers back to words
#----------------------------------------------
# Get the dictionary that maps words to integer indexes
word_index = imdb.get_word_index()

# Word -> Number
# Example :
# { "the"   : 1
#  "movie"  : 2
#  "is"     : 3
#  "good"   : 49
#}

# Reverse the dictionary sp that indexes can be converted back to words
reverse_word_index = {
    value: key for key, value in word_index.item()
}
# Word -> Number
# Example :
# { 1 : "the" 
#   2 : "movie"  
#   3 : "is"     
#   49 : "good"  
#}

# # Define the function to decode an encode review
# Example: [10, 24, 14, 17] to ["I love this movie"]
def decode_review(encoded_review):
    
    # Create am empty list to store decoded words
    words = []

    for number in encoded_review:
        word = reverse_word_index.get(number-3, "?")

        words.append(word)

    return " ".join(words)

#----------------------------------------------
# 6. Simple Text Cleaning
#----------------------------------------------
def clean_text():

    # Convert the characters to lowercase
    text = text.lower()

    # Remove characters that are not English letters or spaces
    text = re.sub(r"[^a-zA-Z/s]", " ", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"/s+", " ", text)

    return text.strip()

#----------------------------------------------
# 7. 
#----------------------------------------------
