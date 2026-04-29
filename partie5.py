def analyse_avancee(lvalue):

    compteur_url = {}
    requeste_plus_lente = None

    for ligne in lvalue:
        url = ligne["url"]
        compteur_url[url] = compteur_url.get(url, 0) + 1

        # requête la plus lente
        if requeste_plus_lente is None or ligne["temps"] > requeste_plus_lente["temps"]:
            requeste_plus_lente = ligne

    # =========================
    # TOP 5 URL (corrigé)
    # =========================
    top5 = sorted(compteur_url.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Les 5 url les plus actives :")
    for url, nb in top5:
        print(url, ":", nb)

    # =========================
    # URL la plus demandée
    # =========================
    lien = max(compteur_url.items(), key=lambda x: x[1])[0]

    print("\nURL la plus demandée :", lien)

    print("\nRequête la plus lente :")
    print(requeste_plus_lente)

    return top5, requeste_plus_lente, lien