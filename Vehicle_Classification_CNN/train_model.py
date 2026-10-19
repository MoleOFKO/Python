"""Train a CNN to classify Audi, BMW, Mercedes-Benz, and Toyota images."""

import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models

IMAGE_SIZE = (128, 128)
EPOCHS = 15
BATCH_SIZE = 32
LEARNING_RATE = 0.001
SEED = 42

PROJECT_DIR = Path(__file__).resolve().parent
TEMP_DIR = PROJECT_DIR / ".tmp"
TEMP_DIR.mkdir(exist_ok=True)
tempfile.tempdir = str(TEMP_DIR)
DATASET_DIR = PROJECT_DIR / "dataset"
TRAIN_DIR = DATASET_DIR / "train"
TEST_DIR = DATASET_DIR / "test"
MODEL_PATH = PROJECT_DIR / "car_brand_classifier.keras"
CLASS_NAMES = ["audi", "bmw", "mercedes_benz", "toyota"]


def load_datasets():
    """Load organized images and reserve 20% of train data for validation."""
    missing = [name for name in CLASS_NAMES if not (TRAIN_DIR / name).is_dir()]
    if missing or not TEST_DIR.exists():
        raise FileNotFoundError(
            "Dataset not prepared. Put brand images in raw_dataset/<brand>/, then run: python prepare_dataset.py"
        )

    train_data = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR, labels="inferred", label_mode="int", class_names=CLASS_NAMES,
        validation_split=0.2, subset="training", seed=SEED,
        image_size=IMAGE_SIZE, batch_size=BATCH_SIZE,
    )
    validation_data = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR, labels="inferred", label_mode="int", class_names=CLASS_NAMES,
        validation_split=0.2, subset="validation", seed=SEED,
        image_size=IMAGE_SIZE, batch_size=BATCH_SIZE,
    )
    test_data = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR, labels="inferred", label_mode="int", class_names=CLASS_NAMES,
        shuffle=False, image_size=IMAGE_SIZE, batch_size=BATCH_SIZE,
    )
    prefetch = tf.data.AUTOTUNE
    return train_data.prefetch(prefetch), validation_data.prefetch(prefetch), test_data.prefetch(prefetch)


def build_model() -> tf.keras.Model:
    """Create the required CNN: convolution, pooling, flatten and dense layers."""
    augmentation = tf.keras.Sequential(
        [layers.RandomFlip("horizontal"), layers.RandomRotation(0.08)], name="data_augmentation"
    )
    model = models.Sequential([
        layers.Input(shape=(*IMAGE_SIZE, 3)), augmentation, layers.Rescaling(1.0 / 255),
        layers.Conv2D(32, (3, 3), activation="relu"), layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"), layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation="relu"), layers.MaxPooling2D((2, 2)),
        layers.Flatten(), layers.Dropout(0.35), layers.Dense(128, activation="relu"),
        layers.Dense(len(CLASS_NAMES), activation="softmax"),
    ], name="car_brand_classifier_cnn")
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
        loss="sparse_categorical_crossentropy", metrics=["accuracy"],
    )
    return model


def save_training_graphs(history: tf.keras.callbacks.History) -> None:
    for metric, title, ylabel, filename in [
        ("accuracy", "Car Brand CNN Accuracy", "Accuracy", "accuracy_graph.png"),
        ("loss", "Car Brand CNN Loss", "Loss", "loss_graph.png"),
    ]:
        plt.figure(figsize=(8, 5))
        plt.plot(history.history[metric], label=f"Training {ylabel}")
        plt.plot(history.history[f"val_{metric}"], label=f"Validation {ylabel}")
        plt.title(title); plt.xlabel("Epoch"); plt.ylabel(ylabel); plt.legend(); plt.tight_layout()
        plt.savefig(PROJECT_DIR / filename, dpi=150)
        plt.close()


def main() -> None:
    tf.keras.utils.set_random_seed(SEED)
    train_data, validation_data, test_data = load_datasets()
    model = build_model()
    model.summary()
    history = model.fit(train_data, validation_data=validation_data, epochs=EPOCHS, verbose=2)
    test_loss, test_accuracy = model.evaluate(test_data, verbose=0)
    print(f"\nTest loss: {test_loss:.4f}")
    print(f"Test accuracy: {test_accuracy:.2%}")
    model.save(MODEL_PATH)
    save_training_graphs(history)
    print(f"\nSaved model: {MODEL_PATH.name}")


if __name__ == "__main__":
    main()
