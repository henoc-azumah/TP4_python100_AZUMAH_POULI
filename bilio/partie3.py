## partie 3 statistique globale
code_erreurs =[404 ,500]
from partie2 import valid_ligne 
lvalide = valid_ligne()
def affiche_stat(lvalide):

    requests_total = len(lvalide)
    nombres_get = 0
    nombres_post = 0
    nombres_erreurs = 0
    nombres_code=0
    somme_tps = 0
    moyen_temps = 0

    for ligne in lvalide:
        if ligne["methode"] == "GET":
            nombres_get += 1
        elif ligne["methode"] == "POST":
            nombres_post += 1
        if ligne["code"] == "200":
            nombres_code += 1

        if ligne["code"] in code_erreurs:
            nombres_erreurs += 1

        somme_tps += ligne["temps"]

    if requests_total > 0:
        moyen_temps = somme_tps / requests_total

    statistique = f"\nStatistique\nNombres de total de requetes : {requests_total}\n\
Nombre de requeste GET : {nombres_get}, Nombre de requeste POST : {nombres_post}\n\
Nombre d erreurs : {nombres_erreurs}\nTemps moyen : {moyen_temps:.2f} ms,nombre de requetes par code HTTP :{nombres_code}"

    print(statistique)

if __name__ == '__main__':
  from bilio import doc2
  affiche_stat(lvalide)
    