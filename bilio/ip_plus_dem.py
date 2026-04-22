def ip_plus(lvalide):
    compteur =0
    for ligne in lvalide:
        ip = ligne['ip']  
        compteur[ip] += 1
        print("Les 3 IP les plus actives :")
        for ip, nb in compteur.most_common(3):
          print(f"  {ip} : {nb} requêtes")