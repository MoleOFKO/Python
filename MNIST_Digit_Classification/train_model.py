#MNIST Handwritten Digit Classification
#------------------------------------------
# 1. Import Libraries
#------------------------------------------
import tensorflow as tf
import numpy as np
import os

from tensorflow.keras import layers, models # type: ignore

#------------------------------------------
# 2. Folder Paths
#------------------------------------------
TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"
MODEL_PATH = "mnist_model.keras"   

#------------------------------------------
# 3. Create Train/Test Folders
#------------------------------------------
# Loop through the training and testing folder paths
for folder in [TRAIN_DIR, TEST_DIR]:
    # Loop through digits 0 to 9
    for digit in range(10):        # fixed: range[10] -> range(10)
        digit_folder = os.path.join(folder, str(digit))

        # Create a complete path such as dataset/train/0
        os.makedirs(
            digit_folder,
            exist_ok = True
        )

#------------------------------------------
# 4. Load MNIST Dataset
#------------------------------------------
print("Loading MNIST Dataset........")

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()  # fixed: minist -> mnist

# x_train = training images
# y_train = training labels
# x_test = testing images
# y_test = testing labels

print("Train images: ", x_train.shape) #(60000, 28, 28)
print("Test images: ", x_test.shape) #(10000, 28, 28)

#------------------------------------------
# 5. Save Training Images
#------------------------------------------
print("\nSaving training images........")

for i in range(len(x_train)):
    digit = y_train[i]

    file_path = os.path.join(
        TRAIN_DIR,
        str(digit),
        f"{i}.png"
    )

    # Add one channel dimension because an image normally has a channel dimension
    img_array = np.expand_dims(x_train[i], axis=-1)

    #Before(28, 28)
    #After(28, 28, 1)

    image = tf.keras.utils.array_to_img(img_array)

    image.save(file_path)

#------------------------------------------
# 5. Save Testing Images
#------------------------------------------
print("\nSaving testing images........")

for i in range(len(x_test)):
    digit = y_test[i]

    file_path = os.path.join(
        TEST_DIR,
        str(digit),
        f"{i}.png"
    )

    # Add one channel dimension because an image normally has a channel dimension
    img_array = np.expand_dims(x_test[i], axis=-1)

    #Before(28, 28)
    #After(28, 28, 1)

    image = tf.keras.utils.array_to_img(img_array)

    image.save(file_path)

#-----------------------------------------------------------------------------
# 7. Normalize Data for Training
#-----------------------------------------------------------------------------

# Convert training pixel values in float32 and normalize them from 0-255 to 0-1
x_train = x_train.astype("float32")/255.0

# Normalize testing image in the same way
x_test = x_test.astype("float32")/255.0

#-----------------------------------------------------------------------------
# 8. Build Neural Network
#-----------------------------------------------------------------------------

# Create a Sequential neural network where layers are processed one after another
model = models.Sequential([
    # Define the input shape of each MNIST image
    layers.Input(shape=(28,28)),
    # Flatten the  28x28 image into a one-dimensional image
    layers.Flatten(),
    # 28x28 = 784

    # Create a fully connected hidden layer with 128 neurons usings ReLU activation
    layers.Dense(
        128,
        activation = "relu"
    ),

    # Randomly turn off 20% of neurons during training to reduce overfitting
    layers.Dropout(0.2),

    # Create another hidden layer with 64 neurons with ReLU activation
    layers.Dense(
        64,
        activation = "relu"
    ),

    layers.Dense(
        10,
        activation = "softmax"
    )
])

#-----------------------------------------------------------------------------
# 9. Compile the Model
#-----------------------------------------------------------------------------
# Configure the model before training
model.compile(
    # Use the Adam optimizer to update
    optimizer = "adam",
    # Use the spare categorical cross-entrophy as the loss function
    loss = "sparse_categorical_crossentropy",  # fixed spelling
    # Measure model performance using accuracy
    metrics = ["accuracy"]
)

#-----------------------------------------------------------------------------
# 10. Train Neural Network
#-----------------------------------------------------------------------------

print("\nTraining Neural Network........\n")

# Train the neural network using the training images and labels
model.fit(
    x_train, # Training Images
    y_train, # Training labels
    epochs = 5, # Train the complete training dataset 5 times
    batch_size = 128, # Process 128 images at a time before updating the model weights
    validation_split = 0.1 # Use 10% of the training data for validation
)

#-----------------------------------------------------------------------------
# 11. Test The Model
#-----------------------------------------------------------------------------

# Evaluate the trained data using unseen fata
test_loss, test_accuracy = model.evaluate(
    x_test, # Testing images
    y_test, # Testing labels
    verbose = 1 # Show evaluation progress bar
)

#-----------------------------------------------------------------------------
# 12. Display Test Results
#-----------------------------------------------------------------------------

print("\n===================================================================")
print("TEST RESULTS")
print("\n===================================================================")

# Display the test loss with 4 decimal places
print(f"Test Loss: {test_loss:.4f}")
# Convert the accuracy from decimal to percentage and display it
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

#-----------------------------------------------------------------------------
# 13. Save The Trained Model
#-----------------------------------------------------------------------------

# Save the trained neural network as Keras model file
model.save(MODEL_PATH)

print(f"Model saved as: ")
print(MODEL_PATH)