from __future__ import annotations

import numpy as np

def distanceImage(image1, image2):
    data1=image1[-1]
    data2=image2[-1]
    return np.sqrt((data1[0]-data2[0])**2+(data1[1]-data2[1])**2+(data1[2]-data2[2])**2)

def fillAdjacentCell(grid, currentRow: int, currentColumn: int, images: list, activeList: list):
    sizeGrid=(len(grid)-1, len(grid[0])-1)
    directions=[np.array([0,1]), np.array([1, 0]), np.array([1, 1])]
    currentImage=grid[currentRow][currentColumn]
    
    for direction in directions:
        coordonate=np.array([currentRow, currentColumn]) + direction
        if coordonate[0]<=sizeGrid[0] and coordonate[1]<=sizeGrid[1] and grid[coordonate[0]][coordonate[1]]==0:
            activeList.append(coordonate)
            nextImage=min(images, key=lambda img: distanceImage(currentImage, img))
            grid[coordonate[0]][coordonate[1]]=nextImage
            images.remove(nextImage)