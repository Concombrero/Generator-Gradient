"""Grid of imageProfile to new image"""

from PIL import Image
from Traitement.traitement import Cluster

def create_cluster_image_grid(sorted_clusters: list[Cluster], output_path: str, image_size: tuple[int, int]):
    """
    Create a grid image where clusters are arranged along the x-axis (columns)
    and images within each cluster are arranged along the y-axis (rows).

    Args:
        sorted_clusters (list[Cluster]): List of sorted Cluster objects.
        output_path (str): Path to save the output grid image.
        image_size (tuple[int, int]): Size of each image in the grid (width, height).

    Returns:
        None
    """
    max_rows = max(len(cluster.images) for cluster in sorted_clusters)
    num_columns = len(sorted_clusters)

    grid_width = num_columns * image_size[0]
    grid_height = max_rows * image_size[1]

    grid_image = Image.new("RGB", (grid_width, grid_height))

    for col, cluster in enumerate(sorted_clusters):
        for row, image_profile in enumerate(cluster.images):
            img = Image.open(image_profile.path).resize(image_size)
            x = col * image_size[0]
            y = row * image_size[1]
            grid_image.paste(img, (x, y))

    grid_image.save(output_path)