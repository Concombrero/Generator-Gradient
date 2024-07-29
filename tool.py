from __future__ import annotations

import cv2
import csv
import os
import numpy as np
import random
from PIL import Image

def distanceDatas(data1, data2):
    distance=0
    for i in range(len(data1)):
        distance+=(data1[i]-data2[i])**2
    return np.sqrt(distance)
    
def RGBtoLAB(rgb_color:tuple[int, int, int])->tuple[int, int, int]:
    """Converti un code  RGB en LAB

    Args:
        rgb_color (tuple[int, int, int]): RGB code

    Returns:
        tuple[int, int, int]:: LAB code
    """
    rgb_color = np.array([[rgb_color]], dtype=np.uint8)
    lab_color = cv2.cvtColor(rgb_color, cv2.COLOR_RGB2LAB)
    return tuple(lab_color[0][0])

def createImage(codeRGB:tuple[int, int, int], sizeImage: tuple[int, int], pathSave: str)->None:
    """Créer une image unie

    Args:
        codeRGB (tuple[int, int, int]): code couleur de l'image
        sizeImage (tuple[int, int]): taille de l'image
        pathSave (str): endroit ou l'image est sauvegardé
    """
    image=Image.new('RGB', sizeImage, codeRGB)
    image.save(pathSave)

def createGrid(numberRow: int, numberColumn: int):
    """create a grid full of 0

    Args:
        numberRow (int):
        numberColumn (int): 

    Returns:
        grid:
    """
    grid = [[None for _ in range(numberColumn)] for _ in range(numberRow)]
    return grid

def displayGrid(grid):
    """Display a grid

    Args:
        grid (list[list]):
    """
    print('\n')
    for ligne in grid:
        for element in ligne:
            print(element, end='   ')
        print('\n')

def gridToImage(grid, nameFolderImage:str, nameFinalImage:str)->None:
    """create a image from a grid full of image name

    Args:
        grid:
        nameFolderImage (str): Name/path of the folder with all the images
        pathFinalImage (str): path du dossier ou le fichier sera enregistré  
        nameFinalImage (str): nom de l'image finale
    """
    displayGrid(grid)
    numberRow = len(grid)
    numberColumn = len(grid[0])
    
    #ouverture des fichers
    maxWidthImage = 0
    maxHeightImage = 0
    images = {}
    for row in grid:
        for nameImage in row:
            if nameImage==None:
                break
            if nameImage not in images:
                path=os.path.join(nameFolderImage, nameImage)
                img = Image.open(path)
                images[nameImage] = img
                maxWidthImage = max(maxWidthImage, img.width)
                maxHeightImage = max(maxHeightImage, img.height)
    
    #Creation de la dernière image
    imageFinal = Image.new('RGB', (numberColumn * maxWidthImage, numberRow * maxHeightImage))
    for indexRow, row in enumerate(grid):
        for indexColumn, nameImage in enumerate(row):
            if nameImage==None:
                break
            img = images[nameImage]
            imageFinal.paste(img, (indexColumn * maxWidthImage, indexRow * maxHeightImage))
    
    path=os.path.join('Final', nameFinalImage)
    imageFinal.save(path)


def createDataSet(width, height, size):
    for i in range(size):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        image = Image.new('RGB', (width, height), color)
        path=os.path.join('Images', 'DataSet')
        path = os.path.join(path, str(i)+'.png')
        image.save(path)