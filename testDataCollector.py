from dataPictureCollector import*
from csvTratement import*
      


def testUniqueImage(nameFolder: str):
    images=imageProfileCreator(nameFolder)
    grid=createGrid(len(images), 2)
    i=0
    for image in images:
        imageApproximation = Image.new('RGB', (500, 500), image[-1])
        path = os.path.join(nameFolder, str(image[0])[:-4:]+'Approximation.png')
        imageApproximation.save(path)
        grid[i][0]=str(image[0])
        grid[i][1]=str(image[0])[:-4:]+'Approximation.png'
        i+=1
    gridToCSV(grid)
    csvToImage('plan.csv', nameFolder, 'test.png')
    clearFolder('nameFolder')
    

def clearFolder(nameFolder):
    files = [file for file in os.listdir(nameFolder)]        
    for i in range(len(files)):
        if i % 2 == 1:
            file_to_delete = os.path.join(nameFolder, files[i])
            os.remove(file_to_delete)
            print(f"Supprimé: {file_to_delete}")