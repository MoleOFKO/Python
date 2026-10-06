"""Train and evaluate baseline and modified ANN models on Fashion-MNIST."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix


MODEL_PATH = "fashion_mnist_ann.keras"
RESULTS_DIR = Path("results")
CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot",
]
EPOCHS = 5
BATCH_SIZE = 128


def create_model(dropout_rate: float = 0.0) -> tf.keras.Model:
    """Build the ANN. The optional dropout is the one changed experiment setting."""
    layers = [
        tf.keras.layers.Input(shape=(28, 28)),
        # Flatten changes each 28 x 28 image into the 784 features required by an ANN.
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
    ]

    if dropout_rate:
        # Dropout is only included in the modified model to test its effect on overfitting.
        layers.append(tf.keras.layers.Dropout(dropout_rate))

    layers.append(tf.keras.layers.Dense(10, activation="softmax"))
    model = tf.keras.Sequential(layers)
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def save_sample_images(images: np.ndarray, labels: np.ndarray) -> None:
    """Save one small grid so the dataset samples and their class names are visible."""
    figure, axes = plt.subplots(2, 5, figsize=(10, 4))
    for index, axis in enumerate(axes.flat):
        axis.imshow(images[index], cmap="gray")
        axis.set_title(CLASS_NAMES[labels[index]])
        axis.axis("off")
    figure.tight_layout()
    figure.savefig(RESULTS_DIR / "sample_images.png", dpi=150)
    plt.close(figure)


def save_training_plots(history: tf.keras.callbacks.History) -> None:
    """Save the required accuracy and loss plots from the modified model training."""
    epochs = range(1, len(history.history["accuracy"]) + 1)

    for metric, title, file_name in [
        ("accuracy", "Model Accuracy", "accuracy.png"),
        ("loss", "Model Loss", "loss.png"),
    ]:
        figure, axis = plt.subplots(figsize=(7, 4))
        axis.plot(epochs, history.history[metric], label=f"Training {metric}")
        axis.plot(epochs, history.history[f"val_{metric}"], label=f"Validation {metric}")
        axis.set(title=title, xlabel="Epoch", ylabel=metric.capitalize())
        axis.legend()
        figure.tight_layout()
        figure.savefig(RESULTS_DIR / file_name, dpi=150)
        plt.close(figure)


def save_prediction_examples(images: np.ndarray, labels: np.ndarray, predictions: np.ndarray) -> None:
    """Save correct and incorrect predictions requested in the assignment."""
    predicted_labels = predictions.argmax(axis=1)
    selected = [np.where(predicted_labels == labels)[0][0], np.where(predicted_labels != labels)[0][0]]
    headings = ["Correct prediction", "Incorrect prediction"]

    figure, axes = plt.subplots(1, 2, figsize=(7, 3))
    for axis, image_index, heading in zip(axes, selected, headings):
        axis.imshow(images[image_index], cmap="gray")
        axis.set_title(
            f"{heading}\nTrue: {CLASS_NAMES[labels[image_index]]}\n"
            f"Predicted: {CLASS_NAMES[predicted_labels[image_index]]}"
        )
        axis.axis("off")
    figure.tight_layout()
    figure.savefig(RESULTS_DIR / "prediction_examples.png", dpi=150)
    plt.close(figure)


def save_report_pdf(baseline_accuracy: float, modified_accuracy: float, modified_loss: float) -> None:
    """Create the short report PDF required for submission after real results are available."""
    lines = [
        "Fashion-MNIST Image Classification Using ANN",
        "",
        "1. Introduction",
        "An artificial neural network classifies Fashion-MNIST images into 10 clothing classes.",
        "",
        "2. Dataset and Preprocessing",
        "Fashion-MNIST contains 28 x 28 grayscale images. Pixel values are normalized from 0-255 to 0-1.",
        "The Flatten layer converts every image to 784 input features.",
        "",
        "3. ANN Architecture",
        "Flatten -> Dense(128, ReLU) -> Dense(64, ReLU) -> Dropout(0.2) -> Dense(10, Softmax)",
        "Optimizer: Adam | Loss: Sparse Categorical Crossentropy | Metric: Accuracy",
        "",
        "4. Training Results and Model Evaluation",
        f"Modified-model test accuracy: {modified_accuracy:.2%}",
        f"Modified-model test loss: {modified_loss:.4f}",
        "See accuracy.png, loss.png, confusion_matrix.png, classification_report.txt, and prediction_examples.png.",
        "",
        "5. Experiment and Comparison",
        f"Original model (no dropout) test accuracy: {baseline_accuracy:.2%}",
        f"Modified model (Dropout 0.2) test accuracy: {modified_accuracy:.2%}",
        "The experiment changes dropout only; compare the two test accuracies to judge its effect.",
        "",
        "6. Streamlit Application",
        "The app loads the saved Keras model, preprocesses an uploaded image, and shows the predicted class and confidence.",
        "",
        "7. Conclusion",
        "The ANN provides a complete Fashion-MNIST classification workflow and an interactive prediction interface.",
    ]
    with PdfPages(RESULTS_DIR / "report.pdf") as pdf:
        figure = plt.figure(figsize=(8.27, 11.69))
        figure.text(0.08, 0.95, "\n".join(lines), va="top", fontsize=10, wrap=True)
        plt.axis("off")
        pdf.savefig(figure, bbox_inches="tight")
        plt.close(figure)


def main() -> None:
    """Run the complete training, experiment, evaluation, and results-export workflow."""
    RESULTS_DIR.mkdir(exist_ok=True)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    print("Training images:", x_train.shape)
    print("Testing images:", x_test.shape)
    print("Classes:", ", ".join(CLASS_NAMES))
    save_sample_images(x_train, y_train)

    # Both models receive the same 0-1 normalized pixels for a fair comparison.
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    print("\nTraining original model (no dropout)...")
    baseline_model = create_model()
    baseline_model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1, verbose=2)
    _, baseline_accuracy = baseline_model.evaluate(x_test, y_test, verbose=0)

    print("\nTraining modified model (Dropout 0.2)...")
    model = create_model(dropout_rate=0.2)
    history = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1, verbose=2)
    test_loss, modified_accuracy = model.evaluate(x_test, y_test, verbose=0)
    model.save(MODEL_PATH)

    predictions = model.predict(x_test, verbose=0)
    predicted_labels = predictions.argmax(axis=1)
    save_training_plots(history)
    save_prediction_examples(x_test, y_test, predictions)

    matrix = confusion_matrix(y_test, predicted_labels)
    figure, axis = plt.subplots(figsize=(10, 8))
    ConfusionMatrixDisplay(matrix, display_labels=CLASS_NAMES).plot(ax=axis, xticks_rotation=45, colorbar=False)
    figure.tight_layout()
    figure.savefig(RESULTS_DIR / "confusion_matrix.png", dpi=150)
    plt.close(figure)

    report = classification_report(y_test, predicted_labels, target_names=CLASS_NAMES)
    (RESULTS_DIR / "classification_report.txt").write_text(report, encoding="utf-8")
    save_report_pdf(baseline_accuracy, modified_accuracy, test_loss)

    print(f"\nOriginal model test accuracy: {baseline_accuracy:.2%}")
    print(f"Modified model test accuracy: {modified_accuracy:.2%}")
    print(f"Modified model test loss: {test_loss:.4f}")
    print(f"Model saved as: {MODEL_PATH}")
    print(f"Results saved in: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
