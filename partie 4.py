code_erreurs =[404 ,500]
def securite_analyse(lvalide):
    ip_suspecte_trouve = False
    erreur_ip = {}
    tentatives_connexion = 0
    compteur =0

    for ligne in lvalide:
        ip = ligne['ip']  
        compteur[ip] += 1
        print("Les 3 IP les plus actives :")
        for ip, nb in compteur.most_common(3):
          print(f"  {ip} : {nb} requêtes")
        if ligne["code"] in code_erreurs:
            adresse_ip = ligne["ip"]
            erreur_ip[adresse_ip] = erreur_ip.get(adresse_ip, 0) + 1

        if ligne["methode"] == "POST" and ligne["url"] == "/login":
            tentatives_connexion += 1

    print("\nAnalyse de securite")

    for ip, nombre_essaie in erreur_ip.items():
        if nombre_essaie >= 3:
            print(f"{ip} est suspecte")
            ip_suspecte_trouve = True

    if not ip_suspecte_trouve:
        print("Aucun IP suspecte")

    print(f"Nombre de tentatives de connexion : {tentatives_connexion}")

    return tentatives_connexion