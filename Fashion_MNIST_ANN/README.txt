FASHION-MNIST IMAGE CLASSIFICATION USING ANN
==============================================

This project meets the Fashion-MNIST ANN assignment requirements.

FILES
-----
train_model.py       Trains the original and modified ANN models and saves results.
app.py               Streamlit application for image prediction.
requirements.txt     Required Python packages.
results/             Created by training; contains the required graphs, matrix, report, and examples.

HOW TO RUN
----------
1. Open this folder in VS Code.
2. Install packages:
   pip install -r requirements.txt
3. Train the models and create all result files:
   python train_model.py
4. Start the Streamlit application:
   streamlit run app.py

MODEL EXPERIMENT
----------------
The original ANN has no dropout. The modified ANN adds Dropout(0.2).
The training script evaluates both models and records their actual test accuracies in results/report.pdf.

IMAGE PREPROCESSING
-------------------
The Streamlit app detects the plain image background, crops the clothing item, and centers it
on a 28 x 28 black canvas. This makes ordinary product photos more similar to Fashion-MNIST images.
