"""Logiciel"""

import os

from Traitement.image_processing import ImageProfile
from Traitement.traitement import create_color_gradient
from Traitement.create_image import create_cluster_image_grid


INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"

def select_folder():
    """User selects a folder from the input directory."""
    for i, folder in enumerate(os.listdir(INPUT_FOLDER)):
        print(f"{i}: {folder}")
    selected_folder = int(input("Select a folder: "))
    selected_folder = os.listdir(INPUT_FOLDER)[selected_folder]
    print("")
    return os.path.join(INPUT_FOLDER, selected_folder)
    
def get_factors(n: int):
    """Get all factors (divisors) of an integer."""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def select_size(folder):
    """User selects the size of the images."""
    n = len(os.listdir(folder))
    factors = get_factors(n)
    print("Select the size of the images:")
    for i, factor in enumerate(factors):
        print(f"{i}: {factor} x {n // factor}")
    selected_size = int(input("Select a size: "))
    selected_size = factors[selected_size]
    print("")
    return selected_size

def main():
    """Logiciel"""
    folder = select_folder()
    k_clusters = select_size(folder)

    # Create list of image files
    image_files = [f"{folder}/{file}" for file in os.listdir(folder) if file.endswith(('.jpg', '.jpeg', '.png'))]
    images = [ImageProfile(path) for path in image_files]

    max_width = max(image.get_width() for image in images)
    max_height = max(image.get_height() for image in images)
    max_size = max(max_width, max_height)

    clusters = create_color_gradient(images, k_clusters)
    create_cluster_image_grid(clusters, f"{OUTPUT_FOLDER}/{os.path.basename(folder)}.png", (max_size, max_size))

if __name__ == "__main__":
    main()
