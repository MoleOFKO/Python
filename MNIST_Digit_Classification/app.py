#--------------------------------------------------
# 1. Import Libraries
#--------------------------------------------------
import streamlit as st
import numpy as np
import tensorflow as tf

# Import Image for image processing and ImageOps for image operations such as grayscake and invert
from PIL import Image, ImageOps

#--------------------------------------------------
# 2. MODEL PATH
#--------------------------------------------------
# Define the path of trained MNIST model
MODEL_PATH = "mnist_model.keras"   

#--------------------------------------------------
# 3. Streamlit  Page Configuration
#--------------------------------------------------
# Configure the streamlit page
st.set_page_config(
    page_title = "MNIST Digit Classifier",
    page_icon = "",
    layout = "centered"
)

#--------------------------------------------------
# 4. Load Trained Model
#--------------------------------------------------
@st.cache_resource # Chache the loaded model to Streamlit does not reload it every time the page changes
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

#--------------------------------------------------
# 5. Page Title and Description
#--------------------------------------------------
#Display the main title of the Streamlit application
st.title("MNIST Handwritten Digit Classification")

#Display descriptions explaining what the application does
st.write(
    "Upload a handwritten digit image and the neural network will predict the digit (0-9)."
)

#--------------------------------------------------
# 6. Load Model with Error Handling 
#--------------------------------------------------
try:
    # Call the load_model() function and store it in variable
    model = load_model()

except Exception:
    # Display error message  telling the user to train the model first
    st.error(
        "Model not found. Please run the python train_model.py first."
    )
    # Stop the Streamlit application
    st.stop()

#--------------------------------------------------
#  7. Image Uploader
#--------------------------------------------------
uploaded_file = st.file_uploader(
    type = ["png", "jpg", "jpeg"] # Allow PNG, JPG, and JPEG image format
)
#--------------------------------------------------
#  8. Process Uploaded Image
#--------------------------------------------------
if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file).convert("L")

    # Display a subtitle for the uploaded image
    st.subheader("Uploaded Image")

    # Display the uploaded image with a width of 200 pixels
    st.image(image, width = 200)

    #--------------------------------------------------
    #  9. Convert Image to Grayscale
    #--------------------------------------------------
    # Grayscale = One intensity value per pixel
    image = ImageOps.grayscale(image)

    #--------------------------------------------------
    #  10. Check Image Background
    #--------------------------------------------------
    # Convert the PIL image into a Numpy array
    arr = np.array(image)

    # Calculate the average pixel brightness.
    # If the average is greater than 127, the image is relatively bright
    if arr.mean() > 127:
        # Invert the grayscale image
        image = ImageOps.invert(image)

        # White -> Black
        # Black -> White

    #--------------------------------------------------
    #  11. Resize Image to MNIST size
    #--------------------------------------------------
    # Resize the image to 28 x 28 pixels
    image = image.resize((28, 28))

    # Original image = Any size
    # After resizing = 28 x 28

    #--------------------------------------------------
    #  12. Convert Image to NumPy Array
    #--------------------------------------------------
    # Convert the image to a NumPy array, change the data type to float32,
    # and normalize pixel value from 0-255 to 0-1
    image_array = np.array(image).astype("float32") / 255.0

    #--------------------------------------------------
    #  13. Add Batch Dimension
    #--------------------------------------------------
    # NN model expects image shape (batch_size, 28, 28)

    # Add the batch dimension to the image
    input_data = np.expand_dims(image_array, axis = 0)

    # Before: (28, 28)
    # After: (1, 28, 28)
    # 1 = One image
    #--------------------------------------------------
    #  14. Make Prediction
    #--------------------------------------------------

    # Pass the processed image to the neural network and get prediction
    prediction = model.predict(input_data, verbose = 0)[0]

    #--------------------------------------------------
    #  15. Get Prediction Digit
    #--------------------------------------------------
    # Find the index with the highest probability
    predicted_digit = int(np.argmax(prediction))

    #Example 
    # prediction = [0.01, 0.02, 0.90, 0.01, .....]
    # Highest probability = 0.09, index = 2
    # Therefore, predicted_digit = 2
    #--------------------------------------------------
    # 16. Get Confidence
    #--------------------------------------------------
    # Get the probability of the predicted_digit
    confidence = float(prediction[predicted_digit])

    #--------------------------------------------------
    # 17. Display Prediction
    #--------------------------------------------------
    st.subheader("Prediction")

    st.success(
        f"Predicted Digit: **{predicted_digit}**"
    )

    #--------------------------------------------------
    # 18. Display Confidence
    #--------------------------------------------------
    st.write(
        f"Confidence: **{confidence * 100:.2f}%**"
    )

    #--------------------------------------------------
    # 19. Display Processed Image
    #--------------------------------------------------
    st.subheader("Processed 28 x 28 Image")

    st.image(image, width = 200)

    #--------------------------------------------------
    # 20. Display All Prediction Probabilities
    #--------------------------------------------------
    st.subheader("Prediction Probabilities")

    for digit, probability in enumerate(prediction):
        st.write(
            f"Digit {digit}: {probability * 100:.2f}%"
        )

    st.progress(float(confidence))