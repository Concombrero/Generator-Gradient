from tool import*

def closestProfileRGB(initialProfile:dict, profiles:list[dict])->dict:
    """Recupère le profil le plus proche de l'autre parmis une liste en

    Args:
        initialProfile (dict): le profil que l'on veut approcher
        profiles (list[dict]): liste des profils

    Returns:
        dict: profil qui se rapproche le plus de celui voulu
    """
    closestProfil=None
    minDistance=float('infinity')
    for profile in profiles:
        if distanceDatas(initialProfile['LAB'], profile['LAB'])<minDistance:
            minDistance=distanceDatas(initialProfile['LAB'], profile['LAB'])
            closestProfil=profile
    return closestProfil

def sortProfiles(initialProfile:dict, profiles:list[dict])->list[dict]:
    """Trie la liste des profil en commencant par un profil particulier donner

    Args:
        initialProfile (dict): le profil par lequel commence la liste 
        profiles (list[dict]): les profils à rajouter à la liste

    Returns:
        list[dict]: la liste trié
    """
    sortProfiles=[initialProfile]
    while profiles:
        closestProfile=closestProfileRGB(initialProfile, profiles)
        sortProfiles.append(closestProfile)
        profiles.remove(closestProfile)
    return sortProfiles

def errorList(profiles: list[dict])->float:
    """Calcule le total des distance entre les profils

    Args:
        profiles (list:[dict]): la liste des profils

    Returns:
        float: la distance totale
    """
    error=0
    for i in range(len(profiles)-1):
        error+=distanceDatas(profiles[i]['LAB'], profiles[i+1]['LAB'])
    return error

def optimalSort(profiles: list[dict])->list[dict]:
    """Pour une liste de profils données donne la liste ou il y a le moins de distance entre les couleurs

    Args:
        profiles (list[dict]): liste des profils à trié

    Returns:
        list[dict]: la meilleure  liste trié
    """
    bestList=None
    minDistance=float('infinity')
    for initialProfiles in profiles:
        tempList=profiles.copy()
        tempList.remove(initialProfiles)
        sortedList=sortProfiles(initialProfiles, tempList)
        if errorList(sortedList)<minDistance:
            minDistance=errorList(sortedList)
            bestList=sortedList
    return bestList

def sortCentroids(clusters:dict)->list[dict]:
    """Organise les centroides dans l'ordre 

    Args:
        clusters (dict): 

    Returns:
        list[dict]: centroides du cluster dans l'ordre
    """
    profiles=[]
    for cluster in clusters:
        profile={'LAB': tuple(cluster)}
        profiles.append(profile)
    sortedCentroids=optimalSort(profiles)
    return sortedCentroids

def organisedGrid(profiles: list[dict], clusters:dict):
    """Ressort la liste des profils ordonnée entre eux et selon les centroides

    Args:
        profiles (list[dict]): listes des profils images
        sortedCentroids (list[dict]): les centroides triée
    """
    sortedCentroids=sortCentroids(clusters)
    sortedGrid=[]
    for centroid in sortedCentroids:
        sortedProfiles=optimalSort([profile for profile in profiles if 'LAB Cluster' in profile and profile['LAB Cluster'] == centroid['LAB']])
        sortedGrid.append(sortedProfiles)
    return sortedGrid
