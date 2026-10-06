# Fashion-MNIST Image Classification Using Artificial Neural Network

## 1. Introduction
This project focuses on building and evaluating an image classification system for the Fashion-MNIST dataset using an Artificial Neural Network (ANN). The objective is to classify 10 categories of clothing items such as T-shirt, Trouser, Sneaker, Bag, and Ankle boot.

The project includes both the training and evaluation workflow and an interactive Streamlit application that allows users to upload images and receive predictions. The system demonstrates how machine learning can be applied to real visual classification problems in a simple and accessible way.

## 2. Problem Statement
Fashion-MNIST is a standard benchmark dataset used for image recognition tasks. The goal is to train a classifier that can correctly identify the category of clothing shown in an image. A successful model should achieve high accuracy while also being able to generalize to new user-uploaded images.

## 3. Project Objectives
The main objectives of this project are:
- To understand the Fashion-MNIST dataset and its structure.
- To build an ANN model for image classification.
- To compare a baseline model with a modified model using Dropout.
- To evaluate model performance using accuracy, loss, confusion matrix, and classification report.
- To develop an interactive UI for real-time classification.

## 4. Dataset Description
The Fashion-MNIST dataset consists of 70,000 grayscale images, each with a size of 28 x 28 pixels. The dataset is divided into:
- 60,000 training images
- 10,000 testing images

Each image belongs to one of 10 classes:
1. T-shirt/top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle boot

The training and evaluation scripts normalize pixel values from 0-255 to 0-1 to improve model training stability and performance.

## 5. Methodology
### 5.1 Model Architecture
The implemented ANN uses the following structure:
- Input layer: 28 x 28 grayscale image
- Flatten layer: converts 2D image to 1D vector of 784 features
- Dense layer: 128 neurons, ReLU activation
- Dense layer: 64 neurons, ReLU activation
- Optional Dropout layer: used in the modified model
- Output layer: 10 neurons, Softmax activation

The model is compiled with:
- Optimizer: Adam
- Loss function: Sparse Categorical Crossentropy
- Metric: Accuracy

### 5.2 Baseline and Modified Model
The project compares two model variants:
- Baseline model: no dropout layer
- Modified model: Dropout(0.2) added to reduce overfitting

The same dataset and preprocessing steps are used for both models, ensuring a fair comparison.

### 5.3 Training Process
The model is trained for 5 epochs with a batch size of 128 and a validation split of 10%. The script saves training history, performance plots, and confusion matrix results automatically.

## 6. Data Preprocessing
Preprocessing is important because the model expects normalized grayscale images. The workflow includes:
- Converting image data type to float32
- Scaling pixel values to the range [0,1]
- Flattening image pixels to feed the network
- Using evaluation metrics to measure the quality of classification

For the Streamlit app, uploaded product images are processed to resemble Fashion-MNIST samples by removing the background and centering the clothing item on a 28 x 28 black canvas.

## 7. Evaluation Metrics
The project uses the following evaluation criteria:
- Accuracy
- Loss
- Confusion Matrix
- Classification Report
- Precision, Recall, and F1-score

The final generated classification report shows that the model achieved a test accuracy of 0.87 (87%). This indicates strong performance across most of the 10 clothing categories.

## 8. Results and Analysis
From the generated evaluation report:
- Overall accuracy: 87%
- Best-performing classes: Trouser, Sandal, Sneaker, Bag, and Ankle boot
- Lower-performing classes: Shirt and Pullover, which are harder to distinguish due to visual similarity

The confusion matrix and classification report confirm that the model is effective in general, while a few visually similar classes remain harder to classify correctly.

### Key Observations
- The ANN performs well on simple and distinct clothing types.
- Classes with similar silhouettes or textures may be misclassified more often.
- Dropout helps control overfitting and improves the model’s generalization ability.

## 9. Streamlit Application
The project also includes a user-friendly web application built with Streamlit. The interface allows the user to:
- Upload a clothing image
- Preprocess the image automatically
- View the processed 28 x 28 image
- See the predicted class name
- View confidence percentage
- Inspect the probability distribution across all 10 classes

This makes the project practical and easy for non-technical users to interact with.

## 10. Project Files
The project contains the following major files:
- train_model.py: trains and evaluates the ANN models and exports results.
- app.py: loads the trained model and provides the Streamlit interface.
- requirements.txt: includes all Python dependencies.
- results/: contains graphs, reports, and sample outputs.

## 11. Challenges and Limitations
Although the model performs well, some limitations still exist:
- Real-world product images may differ from the dataset distribution.
- Background noise or complex lighting can reduce prediction accuracy.
- Classes like Shirt and Pullover may be confused due to similar appearance.

These issues can be improved in future work by using more advanced preprocessing, data augmentation, or CNN-based architectures.

## 12. Conclusion
This project successfully demonstrates the design, training, evaluation, and deployment of a Fashion-MNIST classifier using an ANN. The system achieves strong classification performance and provides an interactive interface for prediction. It also fulfills the assignment requirements by combining machine learning, evaluation metrics, and practical application in a complete workflow.

In conclusion, the project shows how deep learning techniques can be applied to image classification tasks in an efficient, understandable, and user-friendly way.

## 13. Final Remarks
The project is a strong example of applied AI and machine learning. It combines academic understanding with practical implementation, making it suitable for educational assignment purposes and future extension into more advanced computer vision systems.
