'''
AZUMAH Kokou henoc / Etudiant licence physique 
POULI Heritier / Etudiant licence mathematiques  
''' 

import os

from partie1 import lire_log_data
from partie2 import valid_ligne
from partie3 import affiche_stat
from partie4 import securite_analyse
from partie5 import analyse_avancee
from partie6 import analyse_par_fichier
from partie7 import exporter_lignes_invalides
from partie8 import menu
from partie9 import generer_rapport

def main():

    etat = {
        "logs": [],
        "invalides": [],
        "stats": {},
        "securite": {},
        "avancee": {},
        "resume": {}
    }

    dossier = "log_data"

    # =========================
    # RECUPERATION DES FICHIERS CSV
    # =========================
    fichiers = [
        os.path.join(dossier, f)
        for f in os.listdir(dossier)
        if f.endswith(".csv")
    ]

    print("\nFichiers trouvés :")
    for f in fichiers:
        print(f)

    # =========================
    # CHARGEMENT ET NETTOYAGE
    # =========================
    for fichier in fichiers:
        invalides, valides = valid_ligne(fichier)

        etat["logs"].extend(valides)
        etat["invalides"].extend(invalides)

    print("\n==============================")
    print("Chargement terminé")
    print("Logs valides :", len(etat["logs"]))
    print("Logs invalides :", len(etat["invalides"]))
    print("==============================\n")

    # =========================
    # MENU
    # =========================
    while True:

        choix = menu()

        if choix == "1":
            etat["stats"] = affiche_stat(etat["logs"])

        elif choix == "2":
            etat["securite"] = securite_analyse(etat["logs"])

        elif choix == "3":
            etat["avancee"] = analyse_avancee(etat["logs"])

        elif choix == "4":
            etat["resume"] = analyse_par_fichier(dossier)

        elif choix == "5":

            # si stats pas encore calculées → on les calcule automatiquement
            if not etat["stats"]:
                etat["stats"] = affiche_stat(etat["logs"])

            if not etat["securite"]:
                etat["securite"] = securite_analyse(etat["logs"])

            if not etat["avancee"]:
                etat["avancee"] = analyse_avancee(etat["logs"])

            if not etat["resume"]:
                etat["resume"] = analyse_par_fichier("log_data")

            generer_rapport(
                etat["stats"],
                etat["securite"],
                etat["avancee"],
                etat["resume"]
            )

        elif choix == "6":
            exporter_lignes_invalides(etat["invalides"])

        elif choix == "7":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()