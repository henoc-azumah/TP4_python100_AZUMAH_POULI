def analyse_avancee(lvalue):
    compteur_url = {}
    requeste_plus_lente = None
    for ligne in lvalue:
        url = ligne["url"]
        compteur_url[url] = compteur_url.get(url, 0) + 1

        if requeste_plus_lente is None or ligne["temps"] > requeste_plus_lente["temps"]:
            requeste_plus_lente = ligne
           
        print("Les 5 url les plus actives :")
        for url, nb in compteur_url.most_common(5):
          print(f"  {url} : {nb} requêtes")

    lien = None
    value = 0

    for url, nb in compteur_url.items():
        if nb > value:
            value = nb
            lien = url

    print(f"Le url plus demande est : {lien}")
    print(f"La requeste la plus lente est faite au {requeste_plus_lente['date']} sur url {requeste_plus_lente['url']}")

    return lien, requeste_plus_lente

def url_plus(lvalide):
    compteur =0
    for ligne in lvalide:
        url = ligne['url']  
        compteur[url] += 1
        print("Les 5 url les plus demandeés :")
        for url, nb in compteur.most_common(5):
          print(f"  {url} : {nb} requêtes")



import os
def nombre_de_fichier(log_data):
    nbre_de_fichier =0
    ##acceder au dossier log_data
    liste = os.listdir(log_data)
    ##parcourir le dossier pour compter les fichiers .csv
    for fichier in liste:
        if fichier.endswith(".csv"):
         nbre_de_fichier+=1
    print(f"le nombre de fichier est {nbre_de_fichier}")          