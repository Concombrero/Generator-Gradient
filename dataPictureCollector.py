from tool import*

def nameImageCollector(nameFolder: str)->list[str]:
    """Renvoie l'ensemble des fichiers dans un dossier

    Args:
        nameFolder (str): Le nom du dossier

    Returns:
        list[str]: La liste des nom des fichiers
    """
    try:
        files = [file for file in os.listdir(nameFolder) if os.path.isfile(os.path.join(nameFolder, file))]
        return files
    except FileNotFoundError:
        print(f"Le dossier '{nameFolder}' n'existe pas.")
        

def RGBMediumCode(nameFolder: str, nameImage: str)->tuple[int, int, int]:
    """Fais la moyenne du code RGB de l'image

    Args:
        nameFolder (str): nom du dossier
        nameImage (str): nom du fichier image

    Returns:
        tuple[int, int, int]: code RGB
    """
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
  

def imageSize(nameFolder:str, nameFile:str)->tuple[int, int]:
    """Reccupère la taille d'une image

    Args:
        nameFolder (str): nom du dossier
        nameFile (str): nom du fichier image

    Returns:
        tuple[int, int]: taille (w,h)
    """
    path=os.path.join(nameFolder, nameFile)
    with Image.open(path) as img:
        width, height = img.size
    return width, height


def profileCreator(nameFolder: str, nameImage:str)->dict:
    """Créer le profil d'une image donnée

    Args:
        nameFolder (str): nom du dossier
        nameImage (str): nom du fichier image

    Returns:
        dict: profil de l'image avec ses données
    """
    profile=dict()
    profile['Name']=nameImage
    profile['RGB']=RGBMediumCode(nameFolder, nameImage)
    profile['LAB']=RGBtoLAB(profile['RGB'])
    profile['Size']=imageSize(nameFolder, nameImage)
    return profile

def profilesCreator(nameFolder: str)->list[dict]:
    """Génére la liste des profils des images d'un dossiers

    Args:
        nameFolder (str): nom du dossier

    Returns:
        list[dict]: la liste des profils image
    """
    path=os.path.join('Images', nameFolder)
    filesImages=nameImageCollector(nameFolder)
    profiles=[]
    for file in filesImages:
        profile=profileCreator(nameFolder, file)
        profiles.append(profile)
    return profiles