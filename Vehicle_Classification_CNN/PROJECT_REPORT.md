# Short Project Report: Car Brand Classification using CNN

## Objective

Develop an image-classification application that predicts whether a car image is Audi, BMW, Mercedes-Benz, or Toyota.

## Dataset and preprocessing

The dataset consists of labelled car-brand images collected from a permitted source. Images are stored in `raw_dataset/audi`, `raw_dataset/bmw`, `raw_dataset/mercedes_benz`, and `raw_dataset/toyota`. The preparation script creates reproducible 80% training and 20% testing folders. During training, images are resized to 128 x 128 RGB pixels, then pixel values are normalized from 0-255 to 0-1.

## CNN model

The CNN has three convolutional layers (32, 64, and 128 filters), three max-pooling layers, a flatten layer, dropout, a dense layer with 128 neurons, and a four-neuron softmax output layer. It uses Adam with a 0.001 learning rate, sparse categorical cross-entropy, batch size 32, and 15 epochs.

## Evaluation and application

After training, the model is evaluated on the unseen test set and saved as `car_brand_classifier.keras`. The script saves accuracy and loss graphs. The Streamlit app accepts an uploaded image, displays it, predicts its car brand, shows confidence, and shows probabilities for all four brands. Add the final test accuracy and loss after training.
