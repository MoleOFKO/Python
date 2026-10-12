#Streamlit UI for CIFAR-10 Image Classification

import streamlit as st # for UI
import tensorflow as tf # to load and run CNN model
import numpy as np # numerical calculations
from PIL import Image  # to load and run upload image

#----------------------------------------------------------
# 1. Setting
#----------------------------------------------------------
# This is the path of the trained CNN model
MODEL_PATH = 'cifar10_cnn.keras'

# These are the 10 classes that CIFAR-10 model can predict
CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
    ]

#----------------------------------------------------------
# 2. Page Settings
#----------------------------------------------------------
st.set_page_config(
    page_title="CIFAR-10 Image Classification",
    page_icon=":camera:",
    layout="centered"
)

#----------------------------------------------------------
# 3. Load trained model
#----------------------------------------------------------
@st.cache_resource # cache the model so it dose not reload every time the user uploads a new image
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

#----------------------------------------------------------
# 4. Title
#----------------------------------------------------------
# Display the main title of the application
st.title(":camera: CIFAR-10 Image Classification")

# Display a short description of the application
st.write("CNN based image classification system")

st.info(
    "Upload a small RGB image. The model was trained on"
    "32 x 32 CIFAR-10 images."
)

#----------------------------------------------------------
# 5. Upload image
#----------------------------------------------------------
uploaded_file = st.file_uploader(
    "Choose an  image",
    type = ["jpg", "jpeg", "png", "webp"]
)

#----------------------------------------------------------
# 6. Predict
#----------------------------------------------------------
if uploaded_file is not None:
    # Continue processing when the user uploads an image
    image = Image.open(uploaded_file).convert("RGB")

    # Display a subheading for the uploaded image
    st.subheader("Uploaded Image")

    # Display the uploaded image with a width of 300 pixels
    st.image(image, width = 300)

    # Resize the uploaded image to 32 by 32 pixels
    image_resized = image.resize((32, 32))

    # Convert the resized image into NumPy array
    image_array = np.array(image_resized)

    # Convert pixel values from 0-255 to values between 0 and 1
    image_array = image_array.astype("float32") / 255.0

    # Add one extra dimension so the model receives one image as a batch
    image_array = np.expand_dims(image_array, axis=0)

    # Run the prediction when the user clicks the Predict button
    if st.button(":camera: Predict Image"):

        # Load the trained CNN model
        model = load_model()

        # Use the CNN model to predict the uploaded image
        prediction = model.predict(image_array, verbose = 0)

        # Find the index of the class with highest probability
        predicted_index = np.argmax(prediction[0])

        # Convert the predicted class index to class name
        predicted_class = CLASS_NAMES[predicted_index]

        # Convert tje predicted probability into a percentage
        confidence = prediction[0][predicted_index] * 100

        # Display the predicted class as a success message
        st.success(f"Prediction : **{predicted_class}**")

        # Display the prediction confidence with two decimal place
        st.write(f"Confidence : {confidence:.2f}")

        # Display a heading for the class probability 
        st.subheader("Class Probabilities")

        # Create a dictionary containing the probability of each class
        probabilities = {
            CLASS_NAMES[i]: float(prediction[0][i] * 100)
            for i in range(len(CLASS_NAMES))
        }

        # Display the class probability as a bar chart
        st.bar_chart(probabilities)

    #----------------------------------------------------------
    # 7. Project information
    #----------------------------------------------------------
    # Add a horizontal driver between sections
    st.divider()


    # Display a heading for the CIFAR-10 classes
    st.subheader("CIFAR-10 Classes")

    # Display the 10 class names in one line
    st.write(", ".join(CLASS_NAMES))

    #
    st.caption("Mini Project: CIFAR Image Classification System using CNN")
