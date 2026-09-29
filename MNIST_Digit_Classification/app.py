#--------------------------------------------------
# 1. Import Libraries
#--------------------------------------------------
import streamlit as st
import numpy as np
import tensorflow as tf

# Import Image for image processing and  Image operations such as grayscale and 
from PIL import Image, ImageChops

#--------------------------------------------------
# 2. MODEL PATH 
#--------------------------------------------------

#Define the path of the trained MNIST model
MODEL_PATH = "mist_model.keras"

#--------------------------------------------------
# 3. Streamlit page Configuration
#--------------------------------------------------

#Configure the streamlit page
st.set_page_config(
    page_title = "MNIST Digit Classify",
    page_icon = "HH",
    layout = "centered"
)

#--------------------------------------------------
# 4. Load Trained Model
#--------------------------------------------------
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)
