# CIFAR-10 Image Classification System using CNN
#==========================================================

# 1. Import Libraries
#==========================================================
import os # os is used to work with folders and file paths.
import tensorflow as tf # to build and trained the CNN model
import numpy as np # to work with arrays
import matplotlib.pyplot as plt # to visualize the images and the training process
from PIL import Image # to work with images
from tensorflow.keras import layers, models # to build the CNN model

#==========================================================
# 2. Setting
#==========================================================
# # CIFAR-10 images are 32x32 pixels
IMAGE_SIZE = (32, 32) 

# Number of epochs to train the model
EPOCHS = 10 

# Number of images to process in a batch
BATCH_SIZE = 64 

# Path to the dataset folder
DATASET_PATH = 'dataset'

# Path to the training dataset
TRAIN_PATH = os.path.join(DATASET_PATH, 'train') 

# Path to the testing dataset
TEST_PATH = os.path.join(DATASET_PATH, 'test')

# Path to save the trained model
MODEL_PATH = 'cifar10_cnn.keras'

CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

#==========================================================
# 3. Create train/test folders
#==========================================================
def create_folders():
    for main_folder in [TRAIN_PATH, TEST_PATH]:
        for class_name in CLASS_NAMES:
            # Create a folder for each class in the train and test directories
            os.makedirs(
                os.path.join(main_folder, class_name), 
                exist_ok=True
            )

#==========================================================
# 4. Save CIFAR-10 images to folders
#==========================================================
def save_images(images, labels, main_folder):
    # Display the folder where images are being saved
    print(f"Saving images to {main_folder}...")

    # loop though all all images and get the image index
    for index, images in enumerate(images):
        class_name = CLASS_NAMES[int(labels[index])]

        # Create the complete file path for the image
        filename = os.path.join(
            main_folder, 
            class_name, 
            f"{index}.png"
        )

        # Check wether the image file does not exist
        if not os.path.exists(filename):
            # Convert the Numpy array into an image and save it as PNG
            Image.fromarray(images).save(filename)

#==========================================================
# 5. Load CIFAR-10 dataset
#==========================================================
print("Loading CIFAR-10 dataset...")

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Convert the training labels labels From 2S arrays into a 1D format
y_train = y_train.flatten()

# Convert the testing labels labels From 2S arrays into a 1D format
y_test = y_test.flatten()

# Create all train/test folders
create_folders()

# Save all training images into the train folder
save_images(x_train, y_train, TRAIN_PATH)

# Save all testing images into the test folder
save_images(x_test, y_test, TEST_PATH)

#==========================================================
# 6. Normalize pixel values
#==========================================================
# Convert the training pixels from 0-255 into values between 0 and 1
x_train = x_train.astype('float32') / 255.0

# Convert the testing pixels from 0-255 into values between 0 and 1
x_test = x_test.astype('float32') / 255.0

#==========================================================
# 7. Build the CNN model
#==========================================================
model = tf.keras.Sequential([
    # Input layer for 32x32 RGB images
    layers.Input(shape=(32, 32, 3)), 

    # First convolutional layer with 32 filters
    layers.Conv2D(32, (3, 3), activation='relu'),
    # First max pooling layer 
    layers.MaxPool2D((2, 2)), 

    # Second convolutional layer with 64 filters
    layers.Conv2D(64, (3, 3), activation='relu'), 
    # Second max pooling layer
    layers.MaxPool2D((2, 2)),     

    # Third convolutional layer with 64 filters
    layers.Conv2D(64, (3, 3), activation='relu'), 
    # Flatten the output of the convolutional layers
    layers.Flatten(), 

    # Fully connected layer with 64 units
    layers.Dense(64, activation='relu'), 
    # Output layer with 10 units for 10 classes
    layers.Dense(10, activation='softmax') 

])  

# Display the model structure and number of parameters of the CNN
model.summary()

#==========================================================
# 8. Compile the model
#==========================================================
model.compile(
    loss = 'sparse_categorical_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy']
)

#==========================================================
# 0. Train the model
#==========================================================
model.fit(
    x_train,
    y_train,
    epochs = EPOCHS,
    batch_size = BATCH_SIZE,
    validation_data = (x_test, y_test)
)

#==========================================================
