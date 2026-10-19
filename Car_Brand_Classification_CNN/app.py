"""Streamlit interface for the car-brand CNN."""

from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "car_brand_classifier.keras"
CLASS_NAMES = ["audi", "bmw", "mercedes_benz", "toyota"]
IMAGE_SIZE = (128, 128)

st.set_page_config(page_title="Car Brand Classification", page_icon="🚘", layout="centered")


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


def format_brand(name: str) -> str:
    return name.replace("_", " ").title()


st.title("🚘 Car Brand Classification using CNN")
st.write("Upload a car image to classify it as Audi, BMW, Mercedes-Benz, or Toyota.")
st.info("For best results, upload a clear image showing one of the four trained car brands.")

if not MODEL_PATH.exists():
    st.warning("Model not found. Prepare the dataset and run `python train_model.py` first.")
    st.stop()

uploaded_file = st.file_uploader("Choose a car image", type=["jpg", "jpeg", "png", "webp"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.subheader("Uploaded Image")
    st.image(image, width=400)
    if st.button("Predict Car Brand", type="primary"):
        image_array = np.expand_dims(np.asarray(image.resize(IMAGE_SIZE), dtype="float32"), axis=0)
        probabilities = load_model().predict(image_array, verbose=0)[0]
        predicted_index = int(np.argmax(probabilities))
        st.success(f"Prediction: {format_brand(CLASS_NAMES[predicted_index])}")
        st.write(f"Confidence: {probabilities[predicted_index] * 100:.2f}%")
        st.subheader("Brand Probabilities")
        st.bar_chart({format_brand(name): float(score * 100) for name, score in zip(CLASS_NAMES, probabilities)})

st.divider()
st.subheader("Car Brands")
st.write(", ".join(format_brand(name) for name in CLASS_NAMES))
st.caption("Assignment: Image Classification using Convolutional Neural Network (CNN)")
