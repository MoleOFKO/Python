6# Test the saved model with the demo sentences in test_examples.csv.

import csv
import json
import os

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "emotion_lstm.keras")
TOKENIZER_PATH = os.path.join(BASE_DIR, "tokenizer.json")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")
EXAMPLES_PATH = os.path.join(BASE_DIR, "test_examples.csv")
MAX_LEN = 40


def main():
    """Run the demo sentences through the saved model and show the results."""
    with open(EXAMPLES_PATH, "r", encoding="utf-8", newline="") as file:
        examples = list(csv.DictReader(file))

    with open(LABELS_PATH, "r", encoding="utf-8") as file:
        labels = json.load(file)["labels"]

    with open(TOKENIZER_PATH, "r", encoding="utf-8") as file:
        tokenizer = tokenizer_from_json(file.read())

    model = tf.keras.models.load_model(MODEL_PATH)
    texts = [example["text"] for example in examples]
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=MAX_LEN, padding="post")
    predictions = model.predict(padded, verbose=0)

    correct_count = 0
    print(f"{'Expected':<12} {'Predicted':<12} {'Confidence':<12} Text")
    print("-" * 95)

    for example, prediction in zip(examples, predictions):
        predicted_index = int(np.argmax(prediction))
        predicted_label = labels[predicted_index]
        confidence = float(prediction[predicted_index])
        passed = predicted_label == example["expected_emotion"]
        correct_count += int(passed)
        status = "PASS" if passed else "CHECK"
        print(
            f"{example['expected_emotion']:<12} {predicted_label:<12} "
            f"{confidence:>9.1%}   {status}: {example['text']}"
        )

    print(f"\nPassed {correct_count} of {len(examples)} examples.")
    if correct_count != len(examples):
        raise SystemExit(1)


if __name__ == "__main__":
    main()