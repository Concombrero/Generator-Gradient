from tool import*


def moveColumn(grid, nameFolder, nameFinalImage):
    indexColumnInitial=int(input('Quelle Colonne déplacer ? \n'))
    indexColumnFinal=int(input('Ou la déplacer ? \n'))
    
    column=[row[indexColumnInitial] for row in grid]
    
    for row in grid:
        del row[indexColumnInitial]
        
    for i, row in enumerate(grid):
        row.insert(indexColumnFinal, column[i])
    
    gridToImage(grid, nameFolder, nameFinalImage+'.png')

def switchCase(grid, nameFolder, nameFinalImage):
    i1, j1=tuple(input('Quel 1er pixel voulez vous changer ? (Veuillez saisir ligne,colonne) \n').split(','))
    i2, j2=tuple(input('Avec quel autre pixel ? (Veuillez saisir ligne,colonne) \n').split(','))
    
    i1=int(i1)
    j1=int(j1)
    i2=int(i2)
    j2=int(j2)
    
    temp=grid[i1][j1]
    grid[i1][j1]=grid[i2][j2]
    grid[i2][j2]=temp
    gridToImage(grid, nameFolder, nameFinalImage+'.png')

def manualChange(grid: np.array, nameFolder, nameFinalImage)->np.array:
    change=True
    while change:
        print('1. Bouger colonne \n')   
        print('2. Switcher 2 pixels \n')
        print('3. Arreter les changements \n')
        
        reponse=int(input('Que voulez vous faire ? (Saisir numéro) \n'))
        
        if reponse==1:
            moveColumn(grid, nameFolder, nameFinalImage)
        elif reponse==2:
            switchCase(grid, nameFolder, nameFinalImage)
        else:
            change=False
    print('Vous avez finit les modifications ')