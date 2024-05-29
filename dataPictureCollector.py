from __future__ import annotations

from PIL import Image
import os


def nameImageCollector(nameFolder: str)->list[str]:
    try:
        files = [file for file in os.listdir(nameFolder) if os.path.isfile(os.path.join(nameFolder, file))]
        return files
    except FileNotFoundError:
        print(f"Le dossier '{nameFolder}' n'existe pas.")
        

def mediumColor(nameFolder: str, nameImage: str)->tuple[int, int, int]:
    pathImage=os.path.join(nameFolder, nameImage)
    with Image.open(pathImage) as image:
        
        image=image.convert('RGB')
        pixel=list(image.getdata())
        numberPixel=len(pixel)
        
        counterRed=counterGrenn=counterBlue=0
        for red, green, blue in pixel:
            counterRed+=red
            counterGrenn+=green
            counterBlue+=blue
            
        return (counterRed//numberPixel, counterGrenn//numberPixel, counterBlue//numberPixel)
    
def imageProfileCreator(nameFolder: str):
    namesImage=nameImageCollector(nameFolder)
    profilesImage=[]
    for nameImage in namesImage:
        imageData=mediumColor(nameFolder, nameImage)
        profileImage=(nameImage, imageData)
        profilesImage.append(profileImage)
    return profilesImage