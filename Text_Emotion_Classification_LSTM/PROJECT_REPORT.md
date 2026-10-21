# Text Emotion Classification using Word Embedding and LSTM

## 1. Objective
The goal of this project is to build a deep learning model that classifies text into emotion categories such as joy, sadness, anger, and fear.

## 2. Dataset
The project uses the DAIR.AI Emotion dataset, which contains labeled English text. The original dataset has six emotion labels; this assignment uses four: joy, sadness, anger, and fear. The local CSV splits contain 14,124 training examples, 1,741 validation examples, and 1,775 test examples. Love and surprise examples are excluded.

Dataset source: https://huggingface.co/datasets/dair-ai/emotion
The dataset card states the data is for educational and research purposes.

## 3. Preprocessing
The text is cleaned and converted into integer sequences using tokenization. Then the sequences are padded to a fixed length so the model can read them consistently.

## 4. Model Architecture
The model includes the following layers:
- Word Embedding layer
- LSTM layer
- Dense layer
- Output layer with softmax activation

This matches the assignment requirements for multi-class text emotion classification.

## 5. Training and Evaluation
The model is trained on the training split, uses the validation split for early stopping, and evaluates on the separate test split. The latest run achieved 92.96% test accuracy. Results can vary slightly between training runs.

The trained model is saved as `emotion_lstm.keras`.

## 6. Streamlit App
The app allows the user to enter a sentence, click Predict, and view the predicted emotion and confidence score.

## 7. Conclusion
This project follows the assignment rules and demonstrates how Word Embedding and LSTM can be used for text-based emotion classification.
