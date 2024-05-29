from __future__ import annotations

import numpy as np

def distanceImage(image1, image2):
    data1=image1[-1]
    data2=image2[-1]
    return np.sqrt((data1[0]-data2[0])**2+(data1[1]-data2[1])**2+(data1[2]-data2[2])**2)

def fillAdjacentCell(grid, currentRow: int, currentColumn: int, images: list, activeList: list):
    pass