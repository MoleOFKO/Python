# Multi-modal AI : Image Captioning
#-------------------------------------------
import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"
import streamlit as st # to build the web application
from PIL import Image # to open and process uploaded image
from transformers import pipeline # to use pre-trained model easily

# Configure the Streamlit page
st.set_page_config(
    page_title = "Multimodal AI: Image Captioning", # Set the title displayed in the browser tab
    page_icon = "🖼️", # Set the icon displayed in the browser tab
    layout = "centered"
)

# Display the main title of the application
st.title("🖼️ Multimodal AI: Image Captioning")

# Display a subtitle 
st.subheader("Computer Vision (CV) + Natural Language Processing (NLP)")

# Display a short description explaining what the application does
st.write(
    "Upload an image and the AI will describe it in a sentence."
    "The model analyzes the image and generates text."
)

# Cache the loaded model so it can be reused between interactions
@st.cache_resource
# Define a function to load the image captioning model
def load_model():
    return pipeline(
        "image-to-text",
        model = "Salesforce/blip-image-captioning-base", # Specify the pretrained BLIP model
        framework = "pt"
    )

# Create a file uploader that accepts image files 
uploaded_file = st.file_uploader(
    "Choose an image", # Display the upload instruction
    type = ["jpg", "jpeg", "png", "webp"] # Allow JPG, JPEG, PNG and WEBP image formats
)

# Check whether the user has uploaded an image
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB") # Open the uploaded image and convert into RGB

    st.image(
        image,
        caption = "Uploaded Image",
        use_container_width = True
    )

    # Create a button that staffs image caption generation
    if st.button("Generate Caption", type = "primary"):
        # Display a loading message while the AI processes the Image
        with st.spinner("Ai is analyzing image........."):

            try:
                caption_model = load_model()

                # Generate a text description from the uploaded image
                results = caption_model(
                    image,
                    text = "the photography of",
                    max_new_tokens = 40 # limits the number of newly generated tokens
                )

                # Extract the generated caption from the model's output
                caption = results[0]["generated_text"]

                # Display a success message  when caption generation finishes
                st.success("Caption generated!")

                # Display a heading for the generated description
                st.markdown("## AI Description")

                # Display the generated caption on the page
                st.write(caption)

            # Catch error if the model fails to run
            except Exception as error:
                st.error(
                    "The model count not run."
                    "Check your internet connection and installed packages."
                )

                # Display the detailed error for debugging
                st.write("Error Type: ", type(error).__name__)
                st.code(str(error))

    # Draw a horizontal divider at the button of the page
    st.divider()

    st.caption(
        "Learning note: Computer Vision processes the image."
        "Natural Language Processing generates a text description."
    )
