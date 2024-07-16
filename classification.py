from tool import*
from kclustering import*


def globalError(clusters: dict)->float:
    """Calcule l'erreur globale suite à la performation d'un algorithme de kclustering.

    Args:
        clusters (dict): clusters

    Returns:
        float: erreur globale
    """
    error=0
    for centroid, points in clusters.items():
        for point in points:
            error+=distanceDatas(centroid, point)
    return error


def bestClusteringRGB(data: np.array, k: int, numberIteration: int= 100)->dict:
    """Realise un certain nombre de kclustering et renvoie celui avec le moins d'erreur (Sur le code RGB).

    Args:
        data (np.array): tableau de points de données
        k (int): nombre de cluster
        numberIteration (int): nombre d'itération

    Returns:
        dict: meilleur clustering
    """
    bestCluster=None
    smallerError=float('infinity')
    for _ in range(numberIteration):
        clusters=kclusteringRGB(data, k)
        if globalError(clusters)<smallerError:
            smallerError=globalError(clusters)
            bestCluster=clusters
    return bestCluster

def bestClusteringLAB(data: np.array, k: int, numberIteration: int= 100)->dict:
    """Realise un certain nombre de kclustering et renvoie celui avec le moins d'erreur (Sur le code LAB).

    Args:
        data (np.array): tableau de points de données
        k (int): nombre de cluster
        numberIteration (int): nombre d'itération

    Returns:
        dict: meilleur clustering
    """
    bestCluster=None
    smallerError=float('infinity')
    for _ in range(numberIteration):
        """clusters=kclusteringLAB(data, k)
        if globalError(clusters)<smallerError:
            smallerError=globalError(clusters)
            bestCluster=clusters"""
    return bestCluster

def dataRGB(profiles:list[dict])->np.array:
    """Créer la data des codes RGB à partir d'une liste de profil d'image

    Args:
        profiles (list[dict]): liste des profils image

    Returns:
        np.array: tableau de donnée de point
    """
    data=[]
    for profile in profiles:
        codeRGB=np.array(profile['RGB'])
        data.append(codeRGB)
    return np.array(data)


def dataLAB(profiles:list[dict])->np.array:
    """Créer la data des codes LAB à partir d'une liste de profil d'image

    Args:
        profiles (list[dict]): liste des profils image

    Returns:
        np.array: tableau de donnée de point
    """
    data=[]
    for profile in profiles:
        codeLAB=np.array(profile['LAB'])
        data.append(codeLAB)
    return np.array(data)


def updateProfileRGB(profiles: list[dict], clusters: dict)->None:
    """Ajoute à chaque profil un nouvel item de clés 'Groupe RGB' et de valeur le cluster assossié 

    Args:
        profiles (list[dict]): liste des profils images
        clusters (dict): le dictionnaire de clustering
    """
    for profile in profiles:
        codeRGB=profile['RGB']
        for centroid, points in clusters.items():
            if codeRGB in [tuple(point) for point in points]:
                profile['RGB Cluster']=centroid
            
                
def updateProfileLAB(profiles: list[dict], clusters: dict)->None:
    """Ajoute à chaque profil un nouvel item de clés 'Groupe LAB' et de valeur le cluster assossié 

    Args:
        profiles (list[dict]): liste des profils images
        clusters (dict): le dictionnaire de clustering
    """
    for profile in profiles:
        codeLAB=profile['LAB']
        for centroid, points in clusters.items():
            if codeLAB in [tuple(point) for point in points]:
                profile['LAB Cluster']=centroid
                

def clusteringLAB(profiles: list[dict], k:int =5):
    """Realise le clustering selon le code LAB de nos images

    Args:
        profiles (list[dict]): liste des profils image
        k (int): nombre de cluster.
    """
    data=dataLAB(profiles)
    clusters=bestClusteringLAB(data, k)
    updateProfileLAB(profiles, clusters)
    return clusters
    
def clusteringRGB(profiles: list[dict], k:int =5):
    """Realise le clustering selon le code LAB de nos images

    Args:
        profiles (list[dict]): liste des profils image
        k (int): nombre de cluster.
    """
    data=dataRGB(profiles)
    clusters=bestClusteringRGB(data, k)
    updateProfileRGB(profiles, clusters)
    return clusters


def clusteringAll(profiles: list[dict], k:int =5):
    """Realise le clustering selon le code LAB et RGB de nos images

    Args:
        profiles (list[dict]): liste des profils image
        k (int): nombre de cluster.
    """
    clustersLAB=clusteringLAB(profiles, k)
    clusteursRGB=clusteringRGB(profiles, k)
    return clusteursRGB, clustersLAB
