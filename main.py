from dataPictureCollector import*
from classification import*
from triLAB import*
from changeManual import*

def displayList(listStr: list[str]):
    for i in range(1, len(listStr)+1):
        print(str(i) + '. ' + listStr[i-1])
        print('\n')

def openFolder():
    path='Images'
    directories = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    
    print('Voici la liste des dossiers disponibles :')
    print('\n')
    displayList(directories)
    index=int(input('Lequel voulez-vous utiliser ? (saisir uniquement le numéro associé) \n'))-1
    
    path=os.path.join(path, directories[index])
    
    fileCount = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                fileCount += 1
    return path, fileCount, directories[index]



def findFactors(n:int)->list[tuple[int,int]]:
    """Trouve la liste des tupple (a,b) tel que a*b=n

    Args:
        n (int):

    Returns:
        list[tuple[int,int]]: liste de facteurs de n
    """
    factors = []
    for a in range(1, int(np.sqrt(n)) + 1):
        if n % a == 0:
            b = n // a
            factors.append((a, b))
    return factors

def dimensionPossible(numberImage):
    factors=findFactors(numberImage)
    listDimension=[]
    for a, b in factors:
        if a!=b:
            listDimension.append(str(a)+' lignes et '+ str(b) + ' colonnes')
            listDimension.append(str(b)+' lignes et '+ str(a) + ' colonnes')
        
        else:
            listDimension.append(str(a)+' lignes et '+ str(b) + ' colonnes')
    print('\n')
    print('Voci les dimension possibles pour votre images :')
    print('\n')
    displayList(listDimension)
    numberRows, numberColumns=tuple(input('Quel dimension voulez vous ? (Veuillez saisir nbLignes,nbColonnes) \n').split(','))
    return int(numberRows), int(numberColumns)

def gridProfilesToGridName(gridProfiles):
    grid=createGrid(len(gridProfiles[0]), len(gridProfiles))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]=gridProfiles[j][i]['Name']
    return grid

def main():
    createDataSet(10,10,100)
    #Ouvrir les dossier
    nameFolder, numberImage, nameFinalImage=openFolder()
    
    #Definir dimension tableau
    numberRows, numberColumns= dimensionPossible(numberImage)

    #Ouvrir les images
    print('\n')
    print('Etape 1: Création des profils \n')
    profiles=profilesCreator(nameFolder)
    
    #Classer les images
    print('Etape 2: Clustering des images \n')
    clusters=clusteringLAB(profiles, numberColumns)
        
    #Tier et les images
    print('Etape 3: Trie des cluster et organisation de la sttructure \n')
    grid=organisedGrid(profiles, clusters)
    
    #faire l'image
    print('Etape 4: Création de l\'image  \n')
    grid=gridProfilesToGridName(grid)
    gridToImage(grid, nameFolder, nameFinalImage+'.png')
    
    print('L\'opération s\'est déroulé sans soucis majeur. L\'image à bien était créé.')
    
    print('\n')
    change = bool(input('Voulez vous faire des changements (Oui/Non -> 1/0) \n'))
    
    if change:
        manualChange(grid, nameFolder, nameFinalImage)
    
    print('Meci d\'utilisé notre générateur de dégradés')
    
      
    
    
    
    
    



if __name__ == '__main__':
    main()