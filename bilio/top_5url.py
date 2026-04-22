def url_plus(lvalide):
    compteur =0
    for ligne in lvalide:
        url = ligne['url']  
        compteur[url] += 1
        print("Les 5 url les plus demandeés :")
        for url, nb in compteur.most_common(5):
          print(f"  {url} : {nb} requêtes")