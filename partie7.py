def exporter_lignes_invalides(linvalide):
    with open("lignes_invalides.txt", "w", encoding="utf-8") as f:
        for e in linvalide:
            f.write(f"Fichier : {e['fichier']}\n")
            f.write(f"Ligne   : {e['ligne_num']}\n")
            f.write(f"Raison  : {e['raison']}\n")
            f.write(f"Contenu : {e['contenu']}\n")
            f.write("\n")

    print("Export des lignes invalides terminé.")