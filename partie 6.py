import os
import csv

def ligne_valide(ligne):
    for valeur in ligne.values():
        if valeur is None or str(valeur).strip() == "":
            return False
    return True

def est_erreur_http(ligne):
    try:
        return int(ligne['status_code']) >= 400
    except:
        return False

def analyse_par_fichier(log_data):
    liste = os.listdir(log_data)

    total_lignes    = 0
    total_valides   = 0
    total_invalides = 0

    for fichier in sorted(liste):
        if not fichier.endswith(".csv"):
            continue

        chemin = os.path.join(log_data, fichier)

        nb_lues     = 0
        nb_valides  = 0
        nb_invalides= 0
        nb_erreurs  = 0
        temps_total = 0.0

        with open(chemin, "r", encoding="utf-8") as f:
            contenu = csv.DictReader(f , delimiter='|')
            for ligne in contenu:
                nb_lues += 1
                if ligne_valide(ligne):
                    nb_valides += 1
                    if est_erreur_http(ligne):
                        nb_erreurs += 1
                    try:
                        temps_total += float(ligne['response_time'])
                    except:
                        pass
                else:
                    nb_invalides += 1

        temps_moyen = temps_total / nb_valides if nb_valides > 0 else 0.0

        # Affichage par fichier
        print(f"\n{'='*40}")
        print(f"  Fichier       : {fichier}")
        print(f"  Lignes lues   : {nb_lues}")
        print(f"  Valides       : {nb_valides}")
        print(f"  Invalides     : {nb_invalides}")
        print(f"  Erreurs HTTP  : {nb_erreurs}")
        print(f"  Temps moyen   : {temps_moyen:.2f} ms")

        total_lignes    += nb_lues
        total_valides   += nb_valides
        total_invalides += nb_invalides

    # Résumé global
    print(f"\n{'='*40}")
    print(f"  TOTAL")
    print(f"  Lignes lues   : {total_lignes}")
    print(f"  Valides       : {total_valides}")
    print(f"  Invalides     : {total_invalides}")
    print(f"{'='*40}\n")


if __name__ == "__main__":
    analyse_par_fichier("log_data")