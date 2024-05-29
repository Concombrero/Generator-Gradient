from other import*
from dataProcessing import*
from dataPictureCollector import*


def main():
    nameFolder=input('folder name ?')
    
    images=imageProfileCreator(nameFolder)
    
    numberImage=len(images)
    configurations=getDivisor(numberImage)
    print('\n')
    print('Which configuration ?')
    for configuration in configurations:
        print(configuration[1], ',', configuration[0])
        print(configuration[0], ',', configuration[1])
    print('\n')
    configuration = input(' ')
    numberColumn, numberRow= configuration.split(',')
    numberColumn=int(numberColumn)
    numberRow=int(numberRow)
    
    grid=creatorGrid(numberColumn, numberRow)
    activeList=[(0,0)]
    
    grid[0][0]=images[0]
    images.pop(0)
    
    while activeList:
        
        currentCoordonate=activeList[0]
        currentColumn=currentCoordonate[0]
        currentRow=currentCoordonate[1]
        fillAdjacentCell(grid, currentRow, currentColumn, images, activeList)
        activeList.pop(0)
        