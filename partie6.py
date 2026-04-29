import os


def analyse_par_fichier(log_data):

    resume = {}

    liste = os.listdir(log_data)

    for fichier in sorted(liste):
        if not fichier.endswith(".csv"):
            continue

        chemin = os.path.join(log_data, fichier)

        nb_lues = 0
        nb_valides = 0
        nb_invalides = 0
        nb_erreurs = 0
        temps_total = 0

        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.readlines()

            for ligne in lignes:
                nb_lues += 1

                ligne = ligne.strip()

                # ligne vide ou invalide
                if "|" not in ligne:
                    nb_invalides += 1
                    continue

                try:
                    parts = ligne.split("|")

                    if len(parts) != 6:
                        nb_invalides += 1
                        continue

                    code = int(parts[4].strip())
                    temps = int(parts[5].strip().replace("ms", ""))

                    nb_valides += 1
                    temps_total += temps

                    if code in [404, 500]:
                        nb_erreurs += 1

                except:
                    nb_invalides += 1

        temps_moyen = temps_total / nb_valides if nb_valides > 0 else 0

        # affichage fichier
        print(f"\n{'='*40}")
        print(f"Fichier : {fichier}")
        print(f"Lignes lues : {nb_lues}")
        print(f"Valides : {nb_valides}")
        print(f"Invalides : {nb_invalides}")
        print(f"Erreurs HTTP : {nb_erreurs}")
        print(f"Temps moyen : {temps_moyen:.2f} ms")

        # stockage résumé
        resume[fichier] = {
            "lues": nb_lues,
            "valides": nb_valides,
            "invalides": nb_invalides,
            "erreurs": nb_erreurs,
            "temps_moyen": temps_moyen
        }

    print("\nAnalyse par fichier terminée ✔")

    return resume