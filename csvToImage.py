from __future__ import annotations

import csv
import os
from PIL import Image

def csvToImage(pathFileCSV, folderImage, nameFinalImage='image.png'):
    with open(pathFileCSV, 'r') as file:
        reader = csv.reader(file)
        grid = [row for row in reader] 
    numberRow = len(grid)
    numberColumn = len(grid[0])
    
    images = {}
    widthImage = 0
    heightImage = 0
    for row in grid:
        for nameImage in row:
            if nameImage not in images:
                path=os.path.join(folderImage, nameImage)
                img = Image.open(path)
                images[nameImage] = img
                widthImage = max(widthImage, img.width)
                heightImage = max(heightImage, img.height)
                
    imageFinal = Image.new('RGB', (numberColumn * widthImage, numberRow * heightImage))
    for indexRow, row in enumerate(grid):
        for indexColumn, nameImage in enumerate(row):
            img = images[nameImage]
            imageFinal.paste(img, (indexColumn * widthImage, indexRow * heightImage))
    imageFinal.save(nameFinalImage)
            