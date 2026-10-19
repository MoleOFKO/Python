# Short Project Report: Car Brand Classification Using CNN

## Objective

Build an image-classification application that predicts one of four car brands: Audi, BMW, Mercedes-Benz, or Toyota.

## Dataset and preprocessing

The included dataset has 349 labelled photos per brand (1,396 total). `raw_dataset/` stores the original photos in folders organized by brand. `prepare_dataset.py` copies these source photos into `dataset/train/` and `dataset/test/`, creating a reproducible, class-wise 80/20 split with 279 training and 70 test photos per brand. The two folders serve different purposes and should not be merged: keeping the test photos separate prevents them from being used during training and preserves a fair final evaluation. No source photo is placed in both sets. Images are converted to RGB, resized to 128 x 128 pixels, and normalized from 0-255 to 0-1. The dataset source and attribution are documented in `README.md`.

## CNN model

The model has three convolutional layers with 32, 64, and 128 filters, max-pooling after each convolution, a flatten layer, dropout, a 128-neuron dense layer, and a four-class softmax output. It uses Adam with a 0.001 learning rate, sparse categorical cross-entropy, batch size 32, and 15 epochs. A 20% portion of the training set is used for validation; the separate test set is reserved for final evaluation.

## Evaluation

Measured using the included `car_brand_classifier.keras` model and the 280-image held-out test set:

| Metric | Result |
| --- | ---: |
| Test loss | 1.5370 |
| Test accuracy | 32.86% |

The result is modest and the training curves indicate overfitting. The model demonstrates the required training and prediction workflow, but predictions should not be treated as reliable without further data and model improvements. `train_model.py` saves updated accuracy and loss graphs whenever the model is retrained.

## Streamlit application

`app.py` accepts JPG, JPEG, PNG, or WebP images, displays the uploaded image, predicts the brand, and reports confidence and probabilities for all four classes. `test_images/` contains held-out examples for checking the upload and prediction workflow.
