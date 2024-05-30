from other import*
from dataProcessing import*
from dataPictureCollector import*
from csvToImage import*


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
    
    grid=createGrid(numberRow, numberColumn)
    activeList=[(0,0)]
    
    grid[0][0]=images[0]
    images.pop(0)
    
    while activeList:

        currentCoordonate=activeList[0]
        currentRow=currentCoordonate[0]
        currentColumn=currentCoordonate[1]
        
        
        fillAdjacentCell(grid, currentRow, currentColumn, images, activeList)
        activeList.pop(0)
    
    gridToCSV(grid)
    
    csvToImage('plan.csv', nameFolder)
    
    
    
if __name__ == "__main__":
    main()