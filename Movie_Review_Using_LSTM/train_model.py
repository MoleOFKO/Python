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

# Reverse the dictionary so that indexes can be converted back to words
reverse_word_index = {
    value: key for key, value in word_index.items()
}
# Word -> Number
# Example :
# { 1 : "the"
#   2 : "movie"
#   3 : "is"
#   49 : "good"
#}

# # Define the function to decode an encoded review
# Example: [10, 24, 14, 17] to ["I love this movie"]
def decode_review(encoded_review):
    
    # Create an empty list to store decoded words
    words = []

    for number in encoded_review:
        word = reverse_word_index.get(number - 3, "?")
        words.append(word)

    return " ".join(words)

#----------------------------------------------
# 6. Simple Text Cleaning
#----------------------------------------------
def clean_text(text):
    
    # Convert the characters to lowercase
    text = text.lower()

    # Remove characters that are not English letters or spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()

#----------------------------------------------
# 7. Save reviews into train/test folders
#----------------------------------------------
# Define a function to save reviews as text files
def save_reviews(reviews, labels, folder, max_per_class):
    # Initialize the positive review counter
    positive_count = 0

    # Initialize the negative review counter
    negative_count = 0

    # Loop through all reviews
    for i, review in enumerate(reviews):

        # Convert the current label to an integer
        label = int(labels[i])

        # Check whether the review is positive
        if label == 1:
            # Skip the review if the positive limit has been reached
            if positive_count >= max_per_class:
                continue

            # Set the class name to positive
            class_name = "positive"

            # Store the current positive review number
            count = positive_count

            # Increase the positive counter by one
            positive_count += 1
        else:
            # Set the review if the negative limit has been reached
            if negative_count >= max_per_class:
                continue

            class_name = "negative"

            count = negative_count

            negative_count += 1

        # Convert the encoded review back into text
        text = decode_review(reviews)

        # Clean the review text
        text = clean_text(text)

        file_path = os.path.join(
            folder,
            class_name,
            f"review_{count + 1}.txt"
        )

        # Open the file in write mode using UTF-8 encoding
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        # Check whether both positive and negative limit are reached
        if positive_count >= max_per_class and negative_count >= max_per_class:
            break


print("Saving training reviews...")
save_reviews(
    x_train,
    y_train,
    TRAIN_FOLDER,
    MAX_TRAIN_PER_CLASS
)

print("Saving testing reviews...")
save_reviews(
    x_test,
    y_test,
    TEST_FOLDER,
    MAX_TEST_PER_CLASS
)

print("Dataset folders created successfully.")

#----------------------------------------------
# 8. Prepare text data for the LSTM
#----------------------------------------------
# Convert the encoded training reviews into clean text
train_texts = [
    clean_text(decode_review(review))
    for review in x_train[:MAX_TRAIN_PER_CLASS * 2]
]

# Convert the encoded testing reviews into clean text
test_texts = [
    clean_text(decode_review(review))
    for review in x_test[:MAX_TEST_PER_CLASS * 2]
]

# Get the labels corresponding to the training texts
train_labels = y_train[:len(train_texts)]

# Get the labels corresponding to the testing texts
test_labels = y_test[:len(test_texts)]

#----------------------------------------------
# 9. Text Vectorization
#----------------------------------------------
# Create a TextVectorization layer
vectorizer = layers.TextVectorization(
    max_tokens=MAX_WORDS,
    output_mode="int",
    output_sequence_length=MAX_LENGTH
)

vectorizer.adapt(train_texts)

#----------------------------------------------
# 10. Build LSTM Model
#----------------------------------------------
# Create a Sequential neural network model
model = models.Sequential([
    # Define the input as string
    layers.Input(shape=(1,), dtype=tf.string),
    # Convert text into integer squences
    vectorizer,

    # Convert integer word IDs into dense word vectors
    layers.Embedding(
        input_dim=MAX_WORDS, 
        output_dim=64
    ),

    # Add an LSTM layer with 64 units
    layers.LSTM(64),

    # Add a fully connected layer with 32 neurons
    layers.Dense(32, activation="relu"),

    # Add the final binary classification layer to classify Positive or Negative
    layers.Dense(1, activation="sigmoid")
])

# 
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

#----------------------------------------------
# 11. Train model
#----------------------------------------------
print("Preparing training data...")

# Convert the labels into int32
train_labels = np.array(train_labels, dtype=np.int32)
test_labels = np.array(test_labels, dtype=np.int32)

# Create Tensorflow Dataset for training
# Example
# ("good movie", 1)
# ("great movie", 1)
# ("bad movie", 0)
train_dataset = tf.data.Dataset.from_tensor_slices(
    (train_texts, train_labels)
)

# Shuffle the training data
train_dataset = train_dataset.shuffle(
    buffer_size=len(train_texts),
    reshuffle_each_iteration=True
    )

# Crate batches of 64 samples
train_dataset = train_dataset.batch(64)

# improve input performance
train_dataset.prefetch(
    tf.data.AUTOTUNE
)

print("Training model...")
model.fit(
    train_dataset,
    epochs=5
)

#----------------------------------------------
# 12. Evaluate model
#----------------------------------------------
print("Evaluating model...")