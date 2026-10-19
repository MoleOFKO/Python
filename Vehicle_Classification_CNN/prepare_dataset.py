"""Create train/test folders from raw car-brand images.

This follows the same assignment style as the CIFAR-10 project:
1. define class names,
2. create required folders,
3. collect valid image files,
4. split them into train and test sets,
5. save the organized dataset.
"""

import random
import shutil
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
RAW_DIR = PROJECT_DIR / "raw_dataset"
DATASET_DIR = PROJECT_DIR / "dataset"
CLASS_NAMES = ["audi", "bmw", "mercedes_benz", "toyota"]
TEST_FRACTION = 0.2
SEED = 42
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def create_folders() -> None:
    """Create the required train and test folders for every class."""
    for split in ["train", "test"]:
        for class_name in CLASS_NAMES:
            (DATASET_DIR / split / class_name).mkdir(parents=True, exist_ok=True)


def image_files(folder: Path) -> list[Path]:
    """Return real image files and ignore placeholders like .gitkeep."""
    return [
        file
        for file in folder.iterdir()
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS and not file.name.startswith(".")
    ]


def split_images(files: list[Path]) -> tuple[list[Path], list[Path]]:
    """Split a class list into train and test sets using a reproducible seed."""
    random.seed(SEED)
    shuffled = files[:]
    random.shuffle(shuffled)
    split_index = max(1, int(len(shuffled) * (1 - TEST_FRACTION)))
    return shuffled[:split_index], shuffled[split_index:]


def copy_files(destination_folder: Path, files: list[Path]) -> None:
    """Copy image files into the target dataset folder."""
    destination_folder.mkdir(parents=True, exist_ok=True)
    for file in files:
        shutil.copy2(file, destination_folder / file.name)


def clear_images(folder: Path) -> None:
    """Remove old generated images so reruns cannot mix different splits."""
    for file in image_files(folder):
        file.unlink()


def main() -> None:
    """Prepare the dataset structure required by the assignment."""
    create_folders()
    prepared_any = False

    for brand in CLASS_NAMES:
        source = RAW_DIR / brand
        if not source.is_dir():
            raise FileNotFoundError(
                f"Missing folder: {source}. Create raw_dataset/{brand} and place car photos there."
            )

        files = image_files(source)
        if not files:
            print(f"No valid images found in {source}. Add JPG/PNG/WebP images and remove .gitkeep placeholders.")
            continue

        if len(files) < 2:
            print(f"Warning: {source} has only {len(files)} usable image(s). A CNN still needs more examples.")

        train_files, test_files = split_images(files)
        train_folder = DATASET_DIR / "train" / brand
        test_folder = DATASET_DIR / "test" / brand
        clear_images(train_folder)
        clear_images(test_folder)
        copy_files(train_folder, train_files)
        copy_files(test_folder, test_files)

        prepared_any = True
        print(f"{brand}: {len(train_files)} train, {len(test_files)} test")

    if not prepared_any:
        raise FileNotFoundError(
            "No real images were found in raw_dataset. Add labelled car images to raw_dataset/audi, "
            "raw_dataset/bmw, raw_dataset/mercedes_benz, and raw_dataset/toyota, then run this script again."
        )

    print("\nDataset prepared in dataset/train and dataset/test.")


if __name__ == "__main__":
    main()
