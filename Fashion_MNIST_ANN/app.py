"""Streamlit interface for Fashion-MNIST ANN predictions."""

from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps


MODEL_PATH = Path("fashion_mnist_ann.keras")
CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot",
]


@st.cache_resource
def load_model() -> tf.keras.Model:
    """Load the saved model once so Streamlit does not reload it after every interaction."""
    return tf.keras.models.load_model(MODEL_PATH)


def prepare_image(uploaded_image: Image.Image) -> tuple[Image.Image, np.ndarray]:
    """Match product photos to Fashion-MNIST by isolating the item before resizing it."""
    image = ImageOps.grayscale(uploaded_image)
    pixels = np.array(image, dtype="float32")

    # Product photos usually have a plain border. Its median brightness estimates the background.
    border_pixels = np.concatenate((pixels[0], pixels[-1], pixels[:, 0], pixels[:, -1]))
    background_brightness = np.median(border_pixels)
    foreground = np.abs(pixels - background_brightness)
    rows, columns = np.where(foreground > 30)

    if len(rows) > 0:
        # Crop the detected item and preserve its shape instead of stretching a rectangle into 28 x 28.
        item = foreground[rows.min():rows.max() + 1, columns.min():columns.max() + 1]
        scale = 24 / max(item.shape)
        item_size = (max(1, round(item.shape[1] * scale)), max(1, round(item.shape[0] * scale)))
        item = np.array(Image.fromarray(item.astype("uint8")).resize(item_size, Image.Resampling.LANCZOS))

        # A black canvas with a centered item matches the layout of Fashion-MNIST training images.
        canvas = np.zeros((28, 28), dtype="uint8")
        top = (28 - item_size[1]) // 2
        left = (28 - item_size[0]) // 2
        canvas[top:top + item_size[1], left:left + item_size[0]] = item
        image = Image.fromarray(canvas)
    else:
        # Keep a safe fallback for photos where foreground detection finds no visible item.
        if pixels.mean() > 127:
            image = ImageOps.invert(image)
        image = image.resize((28, 28))

    image_array = np.array(image).astype("float32") / 255.0
    # A model expects a batch, so one 28 x 28 image becomes shape (1, 28, 28).
    return image, np.expand_dims(image_array, axis=0)


st.set_page_config(page_title="Fashion-MNIST ANN", page_icon="👕", layout="wide")

background_color = "#eef3fb"
card_color = "rgba(255,255,255,0.84)"
text_color = "#0f172a"
muted_color = "rgba(15, 23, 42, 0.72)"
border_color = "rgba(148, 163, 184, 0.35)"
uploader_bg = "rgba(255,255,255,0.88)"
upload_button = "linear-gradient(135deg, #111827, #0f172a)"

st.markdown(
    f"""
    <style>
    html, body {{
        background: {background_color};
    }}
    .stApp {{
        background: {background_color};
        color: {text_color};
    }}
    header[data-testid="stHeader"] {{
        display: none;
    }}
    .block-container {{
        padding-top: 1.25rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }}
    .topbar-shell {{
        width: 100%;
        background: rgba(9, 16, 28, 0.94);
        border-bottom: 1px solid {border_color};
        margin: -0.8rem -1.2rem 1.5rem -1.2rem;
        padding: 0.85rem 2rem 0.9rem 2rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.16);
    }}
    .brand-pill {{
        display: inline-block;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        background: linear-gradient(90deg, rgba(96,165,250,0.15), rgba(168,85,247,0.18));
        border: 1px solid rgba(96,165,250,0.25);
        color: #60a5fa;
        font-weight: 800;
        font-size: 0.8rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }}
    .hero-title {{
        font-size: clamp(3rem, 6vw, 6rem);
        line-height: 0.96;
        letter-spacing: -0.06em;
        margin: 0.4rem 0 0.7rem 0;
        font-weight: 800;
        color: {text_color};
    }}
    .subtitle {{
        font-size: clamp(1.1rem, 2vw, 1.7rem);
        color: {muted_color};
        margin-bottom: 1.6rem;
        font-weight: 400;
    }}
    [data-testid="stFileUploader"] > section {{
        background: {uploader_bg};
        border: 1px solid {border_color};
        border-radius: 22px;
        padding: 1.2rem 1.2rem 0.9rem 1.2rem;
        box-shadow: 0 12px 30px rgba(148, 163, 184, 0.14);
    }}
    [data-testid="stFileUploader"] button {{
        background: {upload_button};
        color: #f8fafc;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        padding: 0.8rem 1.2rem;
    }}
    .result-card {{
        background: {card_color};
        border: 1px solid {border_color};
        border-radius: 26px;
        padding: 1.6rem;
        margin-top: 1rem;
        box-shadow: 0 18px 35px rgba(15, 23, 42, 0.08);
    }}
    .result-label {{
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: {muted_color};
    }}
    .prediction-pill {{
        display: inline-block;
        background: linear-gradient(135deg, rgba(34,197,94,0.15), rgba(16,185,129,0.12));
        color: #34d399;
        border: 1px solid rgba(16,185,129,0.2);
        border-radius: 999px;
        padding: 0.55rem 0.9rem;
        font-weight: 800;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }}
    .probability-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin: 0.35rem 0;
        font-size: 0.95rem;
        color: {text_color};
    }}
    .probability-bar {{
        height: 0.55rem;
        border-radius: 999px;
        background: rgba(148, 163, 184, 0.22);
        overflow: hidden;
        margin-bottom: 0.8rem;
    }}
    .probability-bar > div {{
        height: 100%;
        border-radius: inherit;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #34d399);
    }}
    div[data-testid="stMetricValue"] {{
        font-size: 2rem;
        font-weight: 800;
        color: {text_color};
    }}
    .stProgress > div > div {{
        background: linear-gradient(90deg, #60a5fa, #8b5cf6);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar-shell">
        <div class="brand-pill">AI Fashion Classifier</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="hero-title">Fashion-MNIST<br>Image Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a clothing image to preview it and predict its Fashion-MNIST class.</div>', unsafe_allow_html=True)

if not MODEL_PATH.exists():
    st.error("Model not found. Run `python train_model.py` first.")
    st.stop()

model = load_model()
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    processed_image, input_data = prepare_image(original_image)
    probabilities = model.predict(input_data, verbose=0)[0]
    class_index = int(np.argmax(probabilities))

    predicted_label = CLASS_NAMES[class_index]
    confidence_value = probabilities[class_index] * 100

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    left, right = st.columns([1.15, 0.85])
    left.image(original_image, caption="Uploaded image", use_container_width=True)
    right.image(processed_image, caption="Processed 28 x 28 image", use_container_width=True)

    st.markdown('<div class="result-label">Prediction</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="prediction-pill">{predicted_label}</div>', unsafe_allow_html=True)
    st.metric("Confidence", f"{confidence_value:.2f}%")

    with st.expander("View all class probabilities", expanded=False):
        for class_name, probability in zip(CLASS_NAMES, probabilities):
            percentage = probability * 100
            st.markdown(
                f"<div class='probability-row'><span>{class_name}</span><strong>{percentage:.2f}%</strong></div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div class='probability-bar'><div style='width:{percentage}%'></div></div>",
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)
