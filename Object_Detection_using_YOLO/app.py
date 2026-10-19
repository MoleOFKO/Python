# Object Detection using CNN-Based architecture YOLO model
#--------------------------------------------------------------
import streamlit as st # Create the web interface
import cv2 # Process images and videos
import os # Manage files and paths
import numpy as np # Convert image bytes into an array
import tempfile # Create temporary files
from ultralytics import YOLO # Load the YOLO object detection model
#--------------------------------------------------------------
# 2. Configure Streamlit Page
#--------------------------------------------------------------
st.set_page_config(
    page_title = "CNN based Object Detection",# Browser tab title 
    page_icon = "🔭", # Browser tab icon
    layout = "wide" # use a wide page layout
) 

#--------------------------------------------------------------
# 3. Display the page title
#--------------------------------------------------------------
# Show the main title
st.title("CNN-Based Object Detection")

# Show Short description
st.write("Upload an image or video to detect objects")

#--------------------------------------------------------------
# 4. Load the pretrained YOLO model
#--------------------------------------------------------------
@st.cache_resource # Cache the model to avoid reloading it on every rerun the app
def load_model():
    return YOLO("yolov8n.pt") # Load the YOLOv8 Nano weights

model = load_model()

#--------------------------------------------------------------
# 5. Create Input Section
#--------------------------------------------------------------
# let the user to select input type
input_type = st.radio(
    "Select the input type", # Display the selection label
    ["Image", "Video"] # Provide two options
)

# Set the confidence threshold
confidence = st.slider( # Create the slider
    "Detection Confidence",
    min_value = 0.1, # Minimum confidence is 10%
    max_value = 1.0, # Maximum confidence is 100%
    value = 0.5, # Default confidence is 50%
    step = 0.1 # Increase or decrease by 10%
)

#--------------------------------------------------------------
# 6. Image Detection
#--------------------------------------------------------------
if input_type == "Image":
    uploaded_file = st.file_uploader(
        "Upload an Image", # Display upload instructions
        type = ["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None: # Continue if a file was uploaded
        # Read the uploaded image
        image_bytes = uploaded_file.getvalue() # Get the file contents as bytes

        # Convert image bytes into Numpy array
        image_array = np.frombuffer(
            image_bytes,
            dtype = np.uint8 # Interpret each value as an unsigned 8-bit integer
        )

        # Decode the array into an OpenCV image
        image = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR # Decode the image in color
        )

        if image is None: # Check whether the image decoding failed
            st.error("Could not read this image.")

        else: # Continue if the image is valid 

            # Run object detection
            results = model.predict(
                source = image,
                conf = confidence,
                verbose = False # Wide detailed model logs
            )

            # Draw bounding boxes around detected objects
            annotated_image = results[0].plot() # Draw boxes, labels, confidence scores

            # Convert BGR to RGB for Streamlit
            annotated_image = cv2.cvtColor(
                annotated_image,
                cv2.COLOR_BGR2RGB # Change the channel order
            )

            # Display
            st.image(
                annotated_image,
                caption = "Detected Objects",
                use_container_width = True # Fit the image to the available width
            )

            # Display the detected class names and confidence
            st.subheader("Detection Results")

            if len(results[0].boxes) == 0: # Check if no objects were detected
                st.info("No objects Detected.")

            else: # Process each detected object
                for box in results[0].boxes:
                    class_id = int(box.cls[0]) # Get the predicted class id as an integer
                    class_name = model.names[class_id] # Convert the class id into a name 

                    score = float(box.conf[0]) # Get the confidence score as a float 

                    # Display the object name and confidence
                    st.write(
                        f"Object : {class_name} |"
                        f"Confidence : {score:.2%}" # Display confidence as a percentage 
                    )

#--------------------------------------------------------------
# 7. Video Detection
#--------------------------------------------------------------
else: # Tun the block if Video is selected
    uploaded_video = st.file_uploader(
        "Upload a video",
        type = ["mp4", "mov", "avi"] # Accept these video formats
    )

    if uploaded_video is not None: # Continue if a video was uploaded

        # Save the uploaded video temporarily
        temp_input = tempfile.NamedTemporaryFile(
            delete = False,
            suffix = ".mp4" # Keep the file after closing and use and MP$ suffix
        )

        # Write the uploaded video bytes to the file
        temp_input.write(uploaded_video.getvalue())
        temp_input.close() # Close the temporary input file

        # Create a temporary output file 
        temp_output = tempfile.NamedTemporaryFile(
            delete = False,
            suffix = ".mp4" # Keep the output file after closing and use an MP4 suffix
        )

        # Store the output file path
        output_path = temp_output.name
        temp_output.close() # Close the temporary output file

        # Open the input video
        cap = cv2.VideoCapture(temp_input.name) # Crate a video object
        writer = None
        video_processed = False

        try:
            if not cap.isOpened():
                st.error("Could not open the input video.")
            else:
                # Read video properties
                fps = cap.get(cv2.CAP_PROP_FPS) # Get frames per second
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Get the video width
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Get the video height

                # Use a safe fallback if FPS is unavailable
                if fps <= 0:
                    fps = 25.0 # Use 25 as a fallback

                if width <= 0 or height <= 0:
                    st.error("Could not read the input video's dimensions.")
                else:
                    # Create the output video writer
                    writer = cv2.VideoWriter(
                        output_path,
                        cv2.VideoWriter_fourcc(*"mp4v"), # Select the MP3V video code
                        fps, # Set the output frame rate
                        (width, height) # Select the output frame dimensions
                    )

                    # Check whether the input or output video
                    if not writer.isOpened():
                        st.error("Could not create the output video.")
                    else:
                        progress = st.progress(0) # Create a progress
                        status = st.empty() # Create a placeholder for status updates

                        # Get the total number of frames
                        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # Read the total frame

                        processed_frames = 0 # Initialize the processed counter

                        # Read and process video frames
                        while True:
                            success, frame = cap.read()
                            if not success:
                                break

                            # Detect object in the current frame
                            results = model.predict(
                                source=frame, # Use the current frame as input
                                conf=confidence,
                                verbose=False
                            )
                            # Draw bounding boxes around detected objects
                            annotated_frame = results[0].plot() # Draw boxes and labels on the frame

                            # Save the processed frame
                            writer.write(annotated_frame) # write the annotated frame to the output video
                            processed_frames += 1 # Increase the processed frame counter

                            # Update progress
                            if total_frames > 0:
                                progress.progress(
                                    # Calculate progress and limit it to 100#
                                    min(processed_frames / total_frames, 1.0)
                                )
                                status.write(
                                    f"Processed Frames : {processed_frames}"
                                )

                        video_processed = processed_frames > 0
        finally:
            # Release video resources
            cap.release() # Release the input video
            if writer is not None:
                writer.release() # Finish writing adn release the output video
            # Clean up the uploaded temporary video
            os.remove(temp_input.name) # Delete the temporary input file

        if video_processed:
            st.success("Video Processing Completed.")

            # Display the processed video
            st.subheader("Detected Video")
            with open(output_path, "rb") as video_file:
                video_bytes = video_file.read()

            st.video(video_bytes)

            # Allow the user to download the result
            st.download_button(
                "Download Detected Video",
                data=video_bytes,
                file_name="detected_video.mp4", # Name the downloaded file
                mime="video/mp4"
            )

        if os.path.exists(output_path):
            os.remove(output_path)
                    