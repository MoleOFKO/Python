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
    processor = BlipProcessor.from_pretrained(MODEL_NAME)

    # Load the pretrained BLIP Visual Question Answering model
    model = BlipForQuestionAnswering.from_pretrained(MODEL_NAME).to(device)

    # Move the model to the selected computing device
    model.to(device)

    # Set the model to evaluation mode
    model.eval() 

    return processor, model, device

# Create an image uploader
uploaded_image = st.file_uploader(
    label = "Choose an image",
    type = ["jpg", "jpeg", "png", "webp"]
)

# Create a text input for the user's question
question = st.text_input(
    label = "Ask a question about an image", # Display the question prompt
    placeholder = "e.g. What color is the car?" # Show a example question
)


# Check whether the user has uploaded an image
if uploaded_image is not None:

    try:
        image = Image.open(uploaded_image).convert("RGB")

        st.image(
            image,
            caption = "Uploaded Image",
            use_container_width = True
        )

        # Create a button that starts the answer generation process when clicked
        if st.button(label = "Get Answer", type = "primary"):
            # Check wether the user entered an non-empty question
            if not question.strip():
                st.warning("Please enter a question first.")
            else:
                with st.spinner("Loading the BLIP model and generating an answer......."):

                    # Load the processor, model, and computing  device
                    processor, model, device = load_model()

                    # Preprocess the image and question into PyTorch
                    inputs = processor(
                        image = image, # Uploaded the uploaded image
                        text = question.strip(), # remove extra spaces and provide the question
                        return_tensors = "pt" # return the processed data s PyTorch tensors
                    )

                    # Move every input tensor to the same device as the model
                    inputs = {
                        key: value.to(device)
                        for key, value in inputs.items()
                    }

                    # Disable gradient calculation because training is not required 
                    with torch.inference_mode():

                        # Generate an answer based on the image and question
                        output = model.generate(
                            **inputs, # Pass the processed image and question to the model
                            max_new_tokens = 20 # Limit the generated answer length to 20 new tokens
                        )

                        # Convert the generated token IDs into readable text
                        answer = processor.decode(
                            output[0], # Select the first generated answer
                            skip_special_tokens = True # remove the special tokens from the decoded text
                        )

                    st.success("Answer")
                    st.markdown(f"**{answer}**") # Display the generated answer in bold text

                    st.caption(f"Model: {MODEL_NAME} | Device: {device.upper()}")


    except Exception as error:
        st.error("The image could not processed ir the model failed to run.")

        st.exception(error) # dispaly the detail error


else: 
    st.info("Upload an image to begin.")

#Create an expandable section containing example questions
with st.expander("Example questions"):
    # Display several example questions as Markdown list
    st.markdown(
        "- What is in the picture?\n"
        "- What color is the car?\n"
        "- How many people are there?\n"
        "- What is the person doing?\n"
        "- Is there a dog in the image?\n"
    )

st.caption("Note : The model may make mistake. Check answers against the image.")