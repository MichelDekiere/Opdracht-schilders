import os
import shutil
import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import hashlib
import random


def make_subset(original_dir, new_base_dir, subset_name, start_index, end_index):
    for category in os.listdir(original_dir):
        dir = new_base_dir / subset_name / category
        os.makedirs(dir)
        fnames = [f"{i}.jpg" for i in range(start_index, end_index)]
        for fname in fnames:
            shutil.copyfile(src=original_dir / category / fname,
                            dst=dir / fname)


def balance_dataset(dir_path):
    """
    Random images kopiëren tot dat alle klassen hetzelfde aantal images hebben en dus gebalanceerd zijn.

    Parameters:
        dataset_dir: A string containing the path to a directory containing
        subdirectories to different classes.
    """

    sizes = [check_amount_of_images(f"{dir_path}/{painter}") for painter in os.listdir(dir_path)]
    target_size = max(sizes)
    biggest_class = os.listdir(dir_path)[sizes.index(target_size)]

    for cls in os.listdir(dir_path):
        if (cls != biggest_class):

            while check_amount_of_images(f"{dir_path}/{cls}") < target_size:
                random_file = random.choice(os.listdir(f"{dir_path}/{cls}"))
                shutil.copy(f"{dir_path}/{cls}/{random_file}",
                            f"{dir_path}/{cls}/{random.randint(0, 1000)}.{random_file}")  # random int voor naam zetten anders zou
                # de image gewoon overgeschreven worden en zou het aantal niet omhoog gaan
                # indien de random_int al bestaat wordt deze gewoon overgeschreven, dus geen nood aan error catch


def check_amount_of_images(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    return count


def rename_files(dir_path):
    """"
    Hernoemen van de files naar de nummering per schilder, dit formaat is nodig voor het goed functioneren van een latere functie (make_subset)

    Parameters:
        dataset_dir: A string containing the path to a directory containing
            subdirectories to different classes.
    """
    i = 0

    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            try:
                os.rename(f"{dir_path}/{path}", f"{dir_path}/{i}.jpg")
                i += 1
            except:
                continue


def remove_duplicates(directory):
    # Set the directory containing the images

    # Create a list to store the hashes of the images
    image_hashes = []

    # Iterate through the images in the directory
    for filename in os.listdir(directory):
        # Open the image
        image = Image.open(os.path.join(directory, filename))

        # Calculate the hash of the image
        image_hash = hashlib.sha256(image.tobytes()).hexdigest()

        # Check if the hash is already in the list
        if image_hash in image_hashes:
            # If the hash is already in the list, this is a duplicate image
            # so we can delete it
            os.remove(os.path.join(directory, filename))
        else:
            # If the hash is not in the list, this is a unique image
            # so we add its hash to the list
            image_hashes.append(image_hash)

    # All duplicate images have been deleted
    print('Done!')


def create_data_with_labels(dataset_dir, size=(180, 180)):
    """
    Labelt de data (0 = Mondriaan, 1 = Picasso, 2 = Rubens, ...)
    Print welke files corrupted zijn. (bv. data\Picasso\\145.jpg --> FAILED)
    Preprocessed ook de data (resized naar (180x180)

    Parameters:
        dataset_dir: A string containing the path to a directory containing
            subdirectories to different classes.
    Returns:
        de data met de labels
    """
    image_paths_per_label = collect_paths_to_files(dataset_dir)

    images = []
    labels = []
    for label, image_paths in image_paths_per_label.items():
        for image_path in image_paths:

            # print(str(image_path))

            img = cv2.imread(str(image_path))

            if (img is not None):
                # print(f"{i} {str(image_path)} --> succes")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                images.append(img)

                # print(label)
                labels.append(label)

            else:
                print(f"{str(image_path)} --> FAILED")

    data = np.array([preprocess_image(image.astype(np.float32), size)
                     for image in images])

    labels = np.array(labels)

    return data, labels


def collect_paths_to_files(dataset_dir):
    """Returns a dict with labels for each subdirectory of the given directory
    as keys and lists of the subdirectory's contents as values.

    Parameters:
        dataset_dir: A string containing the path to a directory containing
            subdirectories to different classes.
    Returns:
        image_paths_per_label: A dict with labels as keys and lists of file
        paths as values.
    """
    dataset_dir = Path(dataset_dir)
    painter_dirs = [f for f in sorted(os.listdir(dataset_dir)) if not f.startswith('.')]
    image_paths_per_label = {
        label: [
            dataset_dir / painter_dir / '{0}'.format(f)
            for f in os.listdir(dataset_dir / painter_dir) if not f.startswith('.')
        ]
        for label, painter_dir in enumerate(painter_dirs)
    }
    return image_paths_per_label


def preprocess_image(image, size: tuple):
    """Returns a preprocessed image.

    Parameters:
        image: A RGB image with pixel values in range [0, 255].
    Returns
        image: The preprocessed image.
    """

    image = cv2.resize(image, size)

    return image
