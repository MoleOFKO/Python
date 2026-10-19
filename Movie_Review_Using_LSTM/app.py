# Movie Review sentiment Classifier
#--------------------------------------------------

# Step-1 : Import Libraries
#--------------------------------------------------
import streamlit as st  # For creating web app
import numpy as np  # for handling input data
import tensorflow as tf  # for loading and using LSTM model

#--------------------------------------------------
# Step-2 : Setting
#--------------------------------------------------
# Define the trained model file
MODEL_PATH = "sentiment_lstm.keras" 

#--------------------------------------------------
# Step-3 : Page Configuration
#--------------------------------------------------
# Configure the streamlit page
st.set_page_config(
    page_title="Movie Review Sentiment Classifier",
    page_icon="🎬",
    layout="centered"
)

#--------------------------------------------------
# Step-4 : Application Title
#--------------------------------------------------
# Display the application title
st.title("🎬 Movie Review Sentiment Classifier")

# Display a short description
st.write(
    "Enter a movie review and the LSTM model will predict"
    " whether the review is Positive or Negative."
)

#--------------------------------------------------
# Step-5 : Load Model
#--------------------------------------------------
@st.cache_resource

# Create a function to load the model
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

# Try to laod the model
try:

    # load the trained LSTM model
    model = load_model()

# Handle errors when the model cannot be load
except Exception as e:
    st.error("Could not load the model.")

    # Display the actual exception
    st.exception(e)
    # Stop the streamlit application
    st.stop()
#--------------------------------------------------
# Step-6 : User Input
#--------------------------------------------------
# Display the input section title
st.header("Enter a Movie Review")

# Create a text area for the movie review text
review_text = st.text_area(
    "Movie Review",
    placeholder="Example: This movie was amazing and I really enjoyed it.",
    height=180
)

#--------------------------------------------------
# Step-7 : Prediction Button
#--------------------------------------------------
if st.button(
    "Predict Sentiment",
    type="primary"
):
    # Check whether the user entered a review
    if review_text.strip() == "":
        st.warning("Please enter a movie review.")

    else:
        # Remove the unnecessary spaces from the review
        review_text = review_text.strip()

        # Convert the review text into a one-item object
        input_data = np.array(
            [review_text],
            dtype=object
        )

        # Predict sentiment using the trained model
        prediction = model.predict(
            input_data,
            verbose = 0
        )

        # Get the probability value
        probability = float(prediction[0][0])

        # Check whether probability at least 0.5
        if probability >= 0.5:
            sentiment = "Positive"
            # Calculate confidence for positive prediction
            confidence = probability

        else:
            sentiment = "Negative"
            # Calculate confidence for negative prediction
            confidence = probability
        #-------------------------------------------------
        # Step-8 : Display Result
        #-------------------------------------------------
        # Display the result header
        st.header("Prediction Result")

        # Display the original review
        st.write("**Review:**")
        st.info(review_text)

        # Display the predicted sentiment
        st.write("**Sentiment**")
        if sentiment == "Positive":
            st.success("😊 Positive Review")
        else:
            st.error("😢 Negative Review")

        #-------------------------------------------------
        # Step-9 : Display  Probability
        #-------------------------------------------------
        # Display model probability
        st.write(f"**Positive Probability : {probability:.2%}**")

        # Display confidence
        st.write(f"**Confidence : {confidence:2%}**")

        # Display a progress bar
        st.progress(confidence)

#-------------------------------------------------
# Step-10 : Example Review
#-------------------------------------------------
st.subheader("Example Reviews")
st.write(
    "😊 **Positive Review**"
    "This movie was amazing and I really enjoyed it."
)

st.write(
    "😢 **Negative Review**"
    "This movie was boring and I did not like it."
)

#-------------------------------------------------
# Step-11: Model Information
#-------------------------------------------------
st.divider()

st.caption(
    "Model : LSTM | Dataset : IMDB" \
    "Task: Binary Classification"
)