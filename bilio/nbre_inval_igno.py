##le nombre de lignes invalides ignorées
import os
import csv
 
def ligne_valide(ligne):
   for valeur in ligne.values():
        if valeur is None or valeur.strip() == "":
            return False
        return True
   

def lire_log_data(log_data):
    fichiers_csv=[]
    ##acceder au dossier log_data
    liste = os.listdir(log_data)
    ##parcourir le dossier pour trouver les fichier .csv
    for fichier in liste:
        if fichier.endswith(".csv"):
         print(fichier)
         chemin = os.path.join(log_data, fichier)
         with open(chemin,"r",encoding="utf-8")as f:
            contenu = csv.DictReader(f)
            for ligne in contenu:
               if ligne_valide(ligne):
                 fichiers_csv.append(ligne)
    return fichiers_csv
if __name__ == '__main__':
   lire_log_data("log_data")
   print(f"voici{ lire_log_data("log_data")}")
    
            
##                      partie5
def valid_ligne(fichier_csv):
    linvalide_ignorer =0
    with open(fichier_csv, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                donnees = ligne.split("|")

                if len(donnees) != 6:
                    linvalide_ignorer +=1
            return linvalide_ignorer  