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