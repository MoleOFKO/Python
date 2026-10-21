# Text Emotion Classification using Word Embedding and LSTM
# Easy explanation:
# - We load labeled text examples from local CSV files
# - We change words into numbers
# - We train an LSTM model to learn the patterns
# - We save the model so the app can use it later

import csv
import json
import os

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODEL_PATH = os.path.join(BASE_DIR, "emotion_lstm.keras")
TOKENIZER_PATH = os.path.join(BASE_DIR, "tokenizer.json")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")
MAX_LEN = 40
VOCAB_SIZE = 10000

EMOTION_CLASSES = ["joy", "sadness", "anger", "fear"]

def load_split(file_path):
    """Read sentences and emotion labels from one local CSV split."""
    label_to_index = {emotion: index for index, emotion in enumerate(EMOTION_CLASSES)}
    texts = []
    labels = []

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            text = row["text"].strip()
            emotion = row["label"].strip()
            if text and emotion in label_to_index:
                texts.append(text)
                labels.append(label_to_index[emotion])

    if not texts:
        raise ValueError(f"No usable text examples found in {file_path}")

    return texts, np.array(labels)


def build_model():
    """Create a simple Word Embedding + LSTM model for emotion classification."""
    model = models.Sequential([
        layers.Embedding(input_dim=VOCAB_SIZE, output_dim=64),
        layers.LSTM(64),
        layers.Dense(32, activation="relu"),
        layers.Dense(len(EMOTION_CLASSES), activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


if __name__ == "__main__":
    print("Loading the local emotion dataset...")
    train_texts, train_labels = load_split(os.path.join(DATASET_DIR, "train.csv"))
    validation_texts, validation_labels = load_split(os.path.join(DATASET_DIR, "validation.csv"))
    test_texts, test_labels = load_split(os.path.join(DATASET_DIR, "test.csv"))
    print(
        f"Loaded {len(train_texts)} training, {len(validation_texts)} validation, "
        f"and {len(test_texts)} test examples."
    )

    # Tokenization converts words into numbers.
    tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token="<OOV>")
    tokenizer.fit_on_texts(train_texts)

    train_sequences = tokenizer.texts_to_sequences(train_texts)
    validation_sequences = tokenizer.texts_to_sequences(validation_texts)
    test_sequences = tokenizer.texts_to_sequences(test_texts)

    # We pad the sequences so every sentence has the same length.
    train_padded = pad_sequences(train_sequences, maxlen=MAX_LEN, padding="post")
    validation_padded = pad_sequences(validation_sequences, maxlen=MAX_LEN, padding="post")
    test_padded = pad_sequences(test_sequences, maxlen=MAX_LEN, padding="post")

    train_one_hot = to_categorical(train_labels, num_classes=len(EMOTION_CLASSES))
    validation_one_hot = to_categorical(validation_labels, num_classes=len(EMOTION_CLASSES))
    test_one_hot = to_categorical(test_labels, num_classes=len(EMOTION_CLASSES))

    print("Training the LSTM model...")
    model = build_model()
    model.fit(
        train_padded,
        train_one_hot,
        validation_data=(validation_padded, validation_one_hot),
        epochs=12,
        batch_size=64,
        callbacks=[
            EarlyStopping(
                monitor="val_loss",
                patience=3,
                restore_best_weights=True,
            )
        ],
        verbose=1,
    )

    test_loss, test_accuracy = model.evaluate(test_padded, test_one_hot, verbose=0)
    print(f"Held-out test accuracy: {test_accuracy:.2%}")

    model.save(MODEL_PATH)

    with open(TOKENIZER_PATH, "w", encoding="utf-8") as file:
        file.write(tokenizer.to_json())

    with open(LABELS_PATH, "w", encoding="utf-8") as file:
        json.dump({"labels": EMOTION_CLASSES}, file)

    print("Model saved successfully:", MODEL_PATH)
    print("Tokenizer saved successfully:", TOKENIZER_PATH)
    print("Labels saved successfully:", LABELS_PATH)
    print("Training completed.")
