##la partie 2 depend entierement de la parie 1 donc je vais mettre la parti 1 en haut et continuer avec la partie 2
              ##partie1

import os
import csv
 # Vérifie que toutes les valeurs sont remplies
def ligne_valide(ligne):
   for valeur in ligne.values():
        if valeur is None or valeur.strip() == "":
            return False
        return True
   

def lire_log_data(log_data):
    fichiers_csv=[]
    ##acceder au dossier log_data/
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
    
            
##                      partie2
def valid_ligne(fichier_csv):
    lvalide =[]
    linvalide =[]
    with open(fichier_csv, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                donnees = ligne.split("|")

                if len(donnees) != 6:
                    print(f" ligne incorrect: {ligne}")
                    linvalide.append(ligne)

                    continue
                else:
                    try:
                        date = donnees[0].strip()
                        adresse_ip = donnees[1].strip()
                        methode = donnees[2].strip()
                        url = donnees[3].strip()
                        code = int(donnees[4].strip())
                        temps = int(donnees[5].strip().replace("ms", ""))

                        donnees_ligne = {
                            "date": date,
                            "ip": adresse_ip,
                            "methode": methode,
                            "code": code,
                            "temps": temps,
                            "url": url
                            #"fichier" :"fichier_a.csv"
                        }

                        lvalide.append(donnees_ligne)
                    except ValueError:
                        print("La valeur est incorrecte sur une ligne")
            return linvalide ,lvalide
            
   

