"""Process images for color extraction and profile."""

import numpy as np
from skimage.color import rgb2lab
from colorthief import ColorThief
from PIL import Image


class ImageProfile:

    """Class to handle image processing and color extraction."""

    def __init__(self, path: str):
        self.path = path
        self.image = Image.open(path)
        self.color_thief = ColorThief(path)
        self.dominant_color_rgb = None
        self.dominant_color_lab = None

    def __str__(self):
        return f"Path: {self.path} \n"
    
    ### GET ###
    def get_dominant_color_rgb(self):
        """Get the dominant color in RGB format."""
        if self.dominant_color_rgb is None:
            self.dominant_color_rgb = np.array(self.color_thief.get_color())
        return self.dominant_color_rgb

    def get_dominant_color_lab(self):
        """Get the dominant color in LAB format."""
        if self.dominant_color_lab is None:
            rgb = self.get_dominant_color_rgb()
            rgb_normalized = np.array(rgb) / 255.0
            self.dominant_color_lab = rgb2lab([[rgb_normalized]])[0][0]
        return self.dominant_color_lab

    def get_size(self):
        """Get the size of the image."""
        return self.image.size

    def get_width(self):
        """Get the width of the image."""
        return self.image.size[0]

    def get_height(self):
        """Get the height of the image."""
        return self.image.size[1]
    
    def get_image(self):
        """Get the image object."""
        return self.image

    ### Distance methods ###
    def get_distance_lab_to(self, other):
        """Get the distance in LAB color space to another image."""
        lab1 = self.get_dominant_color_lab()
        lab2 = other.get_dominant_color_lab()
        return np.linalg.norm(lab1 - lab2)

    def get_distance_rgb_to(self, other):
        """Get the distance in RGB color space to another image."""
        rgb1 = self.get_dominant_color_rgb()
        rgb2 = other.get_dominant_color_rgb()
        return np.linalg.norm(rgb1 - rgb2)
