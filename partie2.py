def valid_ligne(fichier_csv):
    lvalide = []
    linvalide = []

    with open(fichier_csv, "r", encoding="utf-8") as fichier:
        for num_ligne, ligne in enumerate(fichier, 1):
            ligne = ligne.strip()
            donnees = ligne.split("|")

            # =========================
            # CAS INVALIDE
            # =========================
            if len(donnees) != 6:
                linvalide.append({
                    "fichier": fichier_csv,
                    "ligne_num": num_ligne,
                    "contenu": ligne,
                    "raison": "nombre de colonnes incorrect"
                })
                continue

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
                }

                lvalide.append(donnees_ligne)

            except ValueError:
                linvalide.append({
                    "fichier": fichier_csv,
                    "ligne_num": num_ligne,
                    "contenu": ligne,
                    "raison": "valeur invalide"
                })

    return linvalide, lvalide