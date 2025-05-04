import numpy as np
from k_means_constrained import KMeansConstrained
from Traitement.image_processing import ImageProfile

class Cluster:
    """
    Represents a cluster of images with a representative color in LAB space.
    """

    def __init__(self, color: tuple[float, float, float], images: list[ImageProfile]):
        """
        Initialize a Cluster object.

        Args:
            color (tuple[float, float, float]): The representative color of the cluster in LAB space.
            images (list[ImageProfile]): List of ImageProfile objects in the cluster.
        """
        self.color = color
        self.images = images

    def __len__(self):
        """
        Returns:
            int: The number of images in the cluster.
        """
        return len(self.images)

def to_polar_angle(points):
    """
    Convert 2D Cartesian coordinates (A, B) to polar angles (modulo 2π).

    Args:
        points (list[tuple[float, float]]): List of points in 2D space.

    Returns:
        np.ndarray: Array of angles in radians (modulo 2π).
    """
    points = np.array(points)
    angles = np.arctan2(points[:, 1], points[:, 0]) % (2 * np.pi)
    return angles

def cluster_colors(image_profiles: list[ImageProfile], k_clusters: int):
    """
    Cluster the images based on the polar angle (modulo 2π) of their LAB dominant color.

    Args:
        image_profiles (list[ImageProfile]): List of ImageProfile objects to cluster.
        k_clusters (int): Number of clusters to create.

    Returns:
        dict[int, list[ImageProfile]]: A dictionary where keys are cluster indices
                                       and values are lists of ImageProfile objects.
    """
    lab_colors = [profile.get_dominant_color_lab()[1:] for profile in image_profiles]  # Use only A and B
    angles = to_polar_angle(lab_colors).reshape(-1, 1)  # Reshape to 2D array for clustering

    model = KMeansConstrained(n_clusters=k_clusters, size_max=len(image_profiles) // k_clusters, random_state=42)
    labels = model.fit_predict(angles)

    clusters = {i: [] for i in range(k_clusters)}
    for label, profile in zip(labels, image_profiles):
        clusters[label].append(profile)

    return clusters

def get_average_color(image_profiles: list[ImageProfile]):
    """
    Calculate the average LAB color of a list of ImageProfile objects.

    Args:
        image_profiles (list[ImageProfile]): List of ImageProfile objects.

    Returns:
        tuple[float, float, float]: The average LAB color of the images.
    """
    lab_colors = [profile.get_dominant_color_lab() for profile in image_profiles]
    return np.mean(np.array(lab_colors), axis=0)

def sort_clusters_by_polar(clusters_object):
    """
    Sort clusters based on their representative colors (A and B) using polar coordinates.

    Args:
        clusters_object (list[Cluster]): List of Cluster objects to sort.

    Returns:
        list[Cluster]: Sorted list of Cluster objects.
    """
    cluster_colors_list = [cluster.color[1:] for cluster in clusters_object]  # Use only A and B
    polar_angles = to_polar_angle(cluster_colors_list)
    sorted_indices = np.argsort(polar_angles)
    return [clusters_object[i] for i in sorted_indices]

def sort_images_in_cluster(cluster):
    """
    Sort images within a cluster based on their L coordinate.

    Args:
        cluster (Cluster): A Cluster object containing images to sort.

    Returns:
        list[ImageProfile]: Sorted list of ImageProfile objects within the cluster.
    """
    image_colors = [image.get_dominant_color_lab()[0] for image in cluster.images]  # Use only L
    sorted_indices = np.argsort(image_colors)
    return [cluster.images[i] for i in sorted_indices]

def create_color_gradient(image_profiles: list[ImageProfile], k_clusters: int):
    """
    Create a color gradient by clustering and sorting images and clusters.

    Args:
        image_profiles (list[ImageProfile]): List of ImageProfile objects to process.
        k_clusters (int): Number of clusters to create.

    Returns:
        list[Cluster]: A list of Cluster objects representing the sorted color gradient.
    """
    print("Clustering images...")
    clusters = cluster_colors(image_profiles, k_clusters)
    clusters_object = [Cluster(get_average_color(images), images) for images in clusters.values()]

    print("Sorting clusters...")
    sorted_clusters = sort_clusters_by_polar(clusters_object)

    print("Sorting images in clusters...")
    for cluster in sorted_clusters:
        cluster.images = sort_images_in_cluster(cluster)
    return sorted_clusters
