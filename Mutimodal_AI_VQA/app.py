# Multimodal AI: Visual Question Answering (VQA) with BLIP pretrained model
#--------------------------------------------------------------------------
import streamlit as st # to create application interface
from PIL import Image # to open and process uploaded images
import torch # to run the deep learning model
from transformers import BlipProcessor, BlipForQuestionAnswering # BLIP processor and model for VQA

# Configure the Streamlit Page
st.set_page_config(
    page_title = "BLIP Visual Question Answering", # Set the browser tab title
    page_icon = "🤖", # Set the page icon
    layout = "centered"
)

# Display the main application title
st.title("🤖 Visual Question Answering (VQA)")

# Add a short description
st.write("Upload an image, ask a question about it, and the BLIP model answers.")

# Define the name of the pretrained BLIP model to be used for VQA
MODEL_NAME = "Salesforce/blip-vqa-base"

# Define a function to load the model
def load_model():
    # Check whether CUDA = Compute Unified Device Architecute (NVIDIA GPU) is available
    # use the GPU if available, otherwise, use the CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"Device: {device}")

    # Load the pretrained BLIP processor
    