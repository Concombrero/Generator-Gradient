from __future__ import annotations

import numpy as np

def distanceDataImage(data1, image2):
    data2=image2[-1]
    return np.sqrt((data1[0]-data2[0])**2+(data1[1]-data2[1])**2+(data1[2]-data2[2])**2)


def medimuColorAdjacent(grid, row, column):
    sizeGrid=(len(grid)-1, len(grid[0])-1)
    directions=[(-1, -1), (-1,0), (-1,-1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    counterRed=counterGrenn=counterBlue=0
    counterImage=0
    
    for direction in directions:
        coordonate=(row+direction[0], column+direction[1])
        if coordonate[0]<=sizeGrid[0] and coordonate[1]<=sizeGrid[1] and grid[coordonate[0]][coordonate[1]]!=0:
            counterImage+=1
            dataImage=grid[coordonate[0]][coordonate[1]][-1]
            counterRed+=dataImage[0]
            counterGrenn+=dataImage[1]
            counterBlue+=dataImage[2]
        
    return (counterRed//counterImage, counterGrenn//counterImage, counterBlue//counterImage)    


def fillAdjacentCell(grid, currentRow: int, currentColumn: int, images: list, activeList: list):
    sizeGrid=(len(grid)-1, len(grid[0])-1)
    directions=[np.array([0,1]), np.array([1, 0]), np.array([1, 1])]
    currentImage=grid[currentRow][currentColumn]
    
    for direction in directions:
        coordonate=np.array([currentRow, currentColumn]) + direction
        if coordonate[0]<=sizeGrid[0] and coordonate[1]<=sizeGrid[1] and grid[coordonate[0]][coordonate[1]]==0:
            activeList.append(coordonate)
            data=medimuColorAdjacent(grid, coordonate[0], coordonate[1])
            nextImage=min(images, key=lambda img: distanceDataImage(data, img))
            grid[coordonate[0]][coordonate[1]]=nextImage
            images.remove(nextImage)