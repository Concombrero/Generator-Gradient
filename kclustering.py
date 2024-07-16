from tool import*

def barycentre(data)->np.array:
    """Calcule le barycentre d'un lot de data

    Args:
        data (np.array): Tableau de points de données

    Returns:
        np.array: coordonnées du barycentre
    """
    l = sum(point[0] for point in data) / len(data)
    a = sum(point[1] for point in data) / len(data)
    b = sum(point[2] for point in data) / len(data)
    return np.array([l, a, b])

def initializeCentroidsRGB(dimension:int , k: int)->list[np.array]:
    """créer une liste de k centroides de dimension donnée

    Args:
        dimension (int): dimension de l'espace choisi
        k (int): nombre de centroide initialisé

    Returns:
        list[np.array]: liste des coordonnées des centroides
    """
    centroids=[]
    for i in range(k):
        centroid=[]
        for _ in range(dimension):
            coordonate=random.randint(0, 255)
            centroid.append(coordonate)
        centroids.append(np.array(centroid))
    return centroids

def initializeCentroidsLAB(dimension:int , k: int)->list[np.array]:
    """créer une liste de k centroides de dimension donnée

    Args:
        dimension (int): dimension de l'espace choisi
        k (int): nombre de centroide initialisé

    Returns:
        list[np.array]: liste des coordonnées des centroides
    """
    centroids=[]
    for i in range(k):
        centroid=[]
        coordonate=random.randint(0, 100)
        centroid.append(coordonate)
        for _ in range(dimension-1):
            coordonate=random.randint(-100, 100)
            centroid.append(coordonate)
        centroids.append(np.array(centroid))
    return centroids

def assignClusters(data: np.array, centroids: list[np.array]) -> dict:
    """Assigne chaque point de données à la centroïde la plus proche, en tenant compte de la taille maximale des clusters.

    Args:
        data (np.array): Tableau de points de données.
        centroids (list[np.array]): Liste des centroïdes.
        max_size (int): Taille maximale pour chaque cluster.

    Returns:
        dict: Dictionnaire des clusters avec les indices des centroïdes comme clés et les listes de points comme valeurs.
    """
    maxSize=len(data)//len(centroids)
    clusters = {i: [] for i in range(len(centroids))}
    for point in data:
        distances = sorted([(distanceDatas(point, centroid), index) for index, centroid in enumerate(centroids)])
        
        for _, closestCentroideIndex in distances:
            if len(clusters[closestCentroideIndex]) < maxSize:
                clusters[closestCentroideIndex].append(point)
                break
    
    return clusters

def updateCentroids(clusters: dict, k:int)->list[np.array]:
    """Met à jour les centroïdes en calculant le barycentre des points assignés à chaque cluster.

    Args:
        clusters (dict): Dictionnaire des clusters avec les indices des centroïdes comme clés et les listes de points comme valeurs.
        k (int): Nombre de centroïdes.

    Returns:
        list[np.array]: Tableau des nouvelles coordonnées des centroïdes.
    """
    centroids=np.zeros((k, 3))
    for cluster_index, points in clusters.items():
        centroids[cluster_index] = barycentre(points)
    return centroids

def hasConverged(oldCentroids: np.array, newCentroids: np.array, epsilon: float =1e-4)->bool:
    """Vérifie si les centroïdes ont convergé en comparant les centroïdes anciens et nouveaux.

    Args:
        oldCentroids (np.array): Tableau des anciennes coordonnées des centroïdes.
        newCentroids (np.array): Tableau des nouvelles coordonnées des centroïdes.
        epsilon (float): Seuil de convergence.

    Returns:
        bool: True si la convergence est atteinte, sinon False.
    """
    return sum([distanceDatas(oldCentroids[i], newCentroids[i]) for i in range(len(oldCentroids))])<epsilon    
    
def kclusteringRGB(data: np.array, k: int, maxIteration: int =300)->dict:
    """Applique l'algorithme K-means clustering aux données.

    Args:
        data (np.array): Liste de points de données.
        k (int): Nombre de clusters.
        maxIteration (int): Nombre maximum d'itérations.

    Returns:
        dict: Dictionnaire des clusters avec les centroïdes comme clés et les listes de points comme valeurs.
    """
    data=np.array(data)
    
    centroids=initializeCentroidsRGB(3, k)
    newCenroids=np.zeros_like(centroids)
    
    while maxIteration>0:
        clusters = assignClusters(data, centroids)
        newCenroids=updateCentroids(clusters, k)
        
        if hasConverged(centroids, newCenroids):
            break
        
        centroids=newCenroids
    
        maxIteration-=1
    
    resultClusters = {}
    for centroidIndex, points in clusters.items():
        centroidTuple = tuple(centroids[centroidIndex])
        resultClusters[centroidTuple] = points

    return resultClusters

def kclusteringLAB(data: np.array, k: int, maxIteration: int =300)->dict:
    """Applique l'algorithme K-means clustering aux données.

    Args:
        data (np.array): Liste de points de données.
        k (int): Nombre de clusters.
        maxIteration (int): Nombre maximum d'itérations.

    Returns:
        dict: Dictionnaire des clusters avec les centroïdes comme clés et les listes de points comme valeurs.
    """
    data=np.array(data)
    
    centroids=initializeCentroidsLAB(3, k)
    newCenroids=np.zeros_like(centroids)
    
    while maxIteration>0:
        clusters = assignClusters(data, centroids)
        newCenroids=updateCentroids(clusters, k)
        
        if hasConverged(centroids, newCenroids):
            break
        
        centroids=newCenroids
    
        maxIteration-=1
    
    resultClusters = {}
    for centroidIndex, points in clusters.items():
        centroidTuple = tuple(centroids[centroidIndex])
        resultClusters[centroidTuple] = points

    return resultClusters