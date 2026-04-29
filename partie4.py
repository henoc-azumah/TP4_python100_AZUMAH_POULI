from collections import Counter

def securite_analyse(lvalide):

    erreur_ip = {}
    compteur = {}
    tentatives_connexion = 0

    for ligne in lvalide:
        ip = ligne['ip']

        # compteur IP
        compteur[ip] = compteur.get(ip, 0) + 1

        # erreurs
        if ligne["code"] in [404, 500]:
            erreur_ip[ip] = erreur_ip.get(ip, 0) + 1

        # login
        if ligne["methode"] == "POST" and ligne["url"] == "/login":
            tentatives_connexion += 1

    # TOP 3 IP
    top3 = sorted(compteur.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\nLes 3 IP les plus actives :")
    for ip, nb in top3:
        print(ip, ":", nb)

    print("\nAnalyse sécurité")

    for ip, nb in erreur_ip.items():
        if nb >= 3:
            print(ip, "est suspecte")

    return erreur_ip, tentatives_connexion, top3