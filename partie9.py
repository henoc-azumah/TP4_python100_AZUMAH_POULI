# partie9.py

def generer_rapport(stats, securite, avancee, resume):
    f = open("rapport.txt", "w", encoding="utf-8")

    # Titre
    f.write("===== RAPPORT D'ANALYSE =====\n\n")

    # Statistiques globales
    f.write("---- STATISTIQUES GLOBALES ----\n")
    f.write(f"Total requêtes : {stats['total']}\n")
    f.write(f"GET : {stats['get']}\n")
    f.write(f"POST : {stats['post']}\n")
    f.write(f"Erreurs : {stats['erreurs']}\n")
    f.write(f"Temps moyen : {stats['moyenne']:.2f} ms\n\n")

    # Codes HTTP
    f.write("---- REQUETES PAR CODE HTTP ----\n")
    for code in stats["codes"]:
        f.write(f"{code} : {stats['codes'][code]}\n")
    f.write("\n")

    # Sécurité
    f.write("---- SECURITE ----\n")
    f.write("Top 3 IP les plus actives :\n")
    for ip, nb in securite[2]:
        f.write(f"{ip} : {nb} requêtes\n")
    f.write("\n")

    # Analyse avancée
    f.write("---- ANALYSE AVANCEE ----\n")

    f.write("Top 5 URLs :\n")
    for url, nb in avancee[0]:
        f.write(f"{url} : {nb}\n")

    f.write("\nRequête la plus lente :\n")
    f.write(f"{avancee[1]}\n")

    f.write("\nFichier avec le plus de lignes valides :\n")
    f.write(f"{avancee[2]}\n\n")

    # Résumé fichiers
    f.write("---- RESUME PAR FICHIER ----\n")
    for fichier in resume:
        f.write(f"{fichier} : {resume[fichier]}\n")

    f.close()