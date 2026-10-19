# Car Brand Classification using CNN

This project classifies car images into four brands: **Audi, BMW, Mercedes-Benz, and Toyota**. It follows the assignment rules: folder-based training/testing data, preprocessing, a CNN with convolution/pooling/flatten/dense layers, a saved model, evaluation graphs, and a Streamlit prediction UI.

## Dataset setup

Download or collect labelled car images for the four brands. A suitable source is the [Stanford Cars dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html), or another dataset whose licence permits course use. Place images in this exact structure:

```text
raw_dataset/
  audi/
  bmw/
  mercedes_benz/
  toyota/
```

Important: only real image files count. Placeholders like `.gitkeep` are ignored, and the script will stop with a clear message if a brand folder has no valid JPG/PNG/WebP photos. Use at least 100 varied images per brand where possible. Then split the dataset reproducibly into 80% training and 20% testing data:

```powershell
python prepare_dataset.py
```

## Run

```powershell
cd "D:\PROJECT\Python\Vehicle_Classification_CNN"
pip install -r requirements.txt
python prepare_dataset.py
python train_model.py
streamlit run app.py
```

## Project files

- `prepare_dataset.py` - creates `dataset/train` and `dataset/test` from the labelled raw images.
- `train_model.py` - preprocesses images, trains/evaluates the CNN, and saves the model and graphs.
- `app.py` - Streamlit application for image prediction.
- `car_brand_classifier.keras` - trained model created after training.

The previous CIFAR-10 vehicle model must not be used for car-brand predictions because CIFAR-10 does not contain brand labels.
