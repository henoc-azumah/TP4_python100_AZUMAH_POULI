code_erreurs = [404, 500]


def affiche_stat(lvalide):

    requests_total = len(lvalide)
    nombres_get = 0
    nombres_post = 0
    nombres_erreurs = 0
    somme_tps = 0
    codes = {}

    # parcours des logs
    for ligne in lvalide:

        # GET / POST
        if ligne["methode"] == "GET":
            nombres_get += 1
        elif ligne["methode"] == "POST":
            nombres_post += 1

        # code HTTP
        code = int(ligne["code"])

        if code in code_erreurs:
            nombres_erreurs += 1

        codes[code] = codes.get(code, 0) + 1

        # temps
        somme_tps += ligne["temps"]

    # moyenne
    moyenne = somme_tps / requests_total if requests_total > 0 else 0

    # dictionnaire compatible partie 9
    stats = {
        "total": requests_total,
        "get": nombres_get,
        "post": nombres_post,
        "erreurs": nombres_erreurs,
        "moyenne": moyenne,
        "codes": codes
    }

    # affichage propre (optionnel)
    print("\n===== STATISTIQUES GLOBALES =====")
    print(f"Total requêtes : {requests_total}")
    print(f"GET : {nombres_get} | POST : {nombres_post}")
    print(f"Erreurs (404/500) : {nombres_erreurs}")
    print(f"Temps moyen : {moyenne:.2f} ms")

    print("\nCodes HTTP :")
    for c, n in codes.items():
        print(f"{c} : {n}")

    return stats