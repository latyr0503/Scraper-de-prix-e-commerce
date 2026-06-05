"""
=======================================
Scraper de prix e-commerce - Version 1
=======================================
"""

print("=== Bienvenue dans le comparateur de prix ===")
programme_actif = True

# liste des produits
list_products = [
    {"Nom": "produit 1", "categorie": "cat 1", "prix": 10000},
    {"Nom": "produit 1 bis", "categorie": "cat 1", "prix": 20000},
    {"Nom": "produit 2", "categorie": "cat 2", "prix": 14000},
    {"Nom": "produit 2 bis", "categorie": "cat 2", "prix": 10000},
    {"Nom": "produit 3", "categorie": "cat 3", "prix": 50000},
    {"Nom": "produit 3 bis", "categorie": "cat 3", "prix": 70000},
    {"Nom": "produit 4", "categorie": "cat 4", "prix": 8000},
    {"Nom": "produit 4 bis", "categorie": "cat 4", "prix": 1000},
    {"Nom": "produit 5", "categorie": "cat 5", "prix": 11000},
    {"Nom": "produit 5 bis", "categorie": "cat 5", "prix": 13000},
]

def comparaison_prix():
    """
    fonction qui compare le prix d'un produit
    """
    print("\n=== Comparaison de prix ===\n")
    # Saisie des informations
    nom_produit = input("Nom du produit : ")
    ancien_prix = float(input("Ancien prix : "))
    nouveau_prix = float(input("Nouveau prix : "))
    seuil_alerte = float(input("Seuil d'alerte : "))

    # Calcul de la variation
    variation = nouveau_prix - ancien_prix

    print("\n===== RÉSULTAT =====\n")
    print("Produit :", nom_produit)

    # Vérification de l'évolution du prix
    if nouveau_prix < ancien_prix:
        print("Le prix a baissé.")
    elif nouveau_prix > ancien_prix:
        print("Le prix a augmenté.")
    else:
        print("Le prix est resté identique.")

    # Affichage de la différence
    print("Variation du prix :", variation)

    # Calcul du pourcentage
    if ancien_prix != 0:
        pourcentage = (variation / ancien_prix) * 100
        print(f"Variation en pourcentage : {pourcentage:.2f} %")

    # Vérification du seuil d'alerte
    if nouveau_prix <= seuil_alerte:
        print("ALERTE : le prix est sous le seuil fixé.")
    else:
        print("Le prix est encore au-dessus du seuil.")

    print("\n Fin de la comparaison")


def aide():
    """
    fonction qui affiche les informations sur le programme
    """
    print("\n===== AIDE =====\n")
    print("1 - Choisissez l'option 1 pour comparer un produit.")
    print("2 - Saisissez les prix demandés.")
    print("3 - Le programme calcule la variation.")
    print("4 - Une alerte apparaît si le prix baisse sous le seuil.")

    print("\n Fin de l'aide")


def apropos():
    """
    fonction qui affiche les informations sur le programme
    """
    print("\n===== À PROPOS =====\n")
    print("Projet pédagogique Python")
    print("Sujet : Scraper de prix e-commerce")
    print("Version actuelle : programmation procédurale")
    print("Notions utilisées :")
    print("- variables")
    print("- conditions")
    print("- boucles")
    print("- input utilisateur")

    print("\n Fin de à propos")


# nouvelle fonctionnalité
def afficher_produits():
    """
    fonction qui affiche les produits
    """
    print("\n=== Affichage des produits ===\n")
    for produit in list_products:
        print(
            f"Produit : {produit['Nom']}, Catégorie : {produit['categorie']}, Prix : {produit['prix']} FCFA"
        )
    print("\n Fin d'affichage")


def rechercher_produit():
    """
    fonction qui recherche un produit
    """
    print("\n=== Recherche de produit ===\n")
    nom_recherche = input("Nom du produit : ")
    for produit in list_products:
        if produit["Nom"] == nom_recherche:
            print(
                f"Produit : {produit['Nom']}, Catégorie : {produit['categorie']}, Prix : {produit['prix']} FCFA"
            )
            break
    else:
        print("Produit non trouvé")
    print("\n Fin de la recherche")


def filtrer_par_categorie():
    """
    fonction qui filtre les produits par catégorie
    """
    print("\n=== Filtre par catégorie ===\n")
    categorie_recherche = input("Catégorie : ")
    for produit in list_products:
        if produit["categorie"] == categorie_recherche:
            print(
                f"Produit : {produit['Nom']}, Catégorie : {produit['categorie']}, Prix : {produit['prix']} FCFA"
            )
            break
    else:
        print("Produit non trouvé")
    print("\n Fin du filtre")


def trier_par_prix():
    """
    fonction qui trie les produits par prix
    """
    print("\n=== Tri par prix inferieur à un prix donné ===\n")
    prix_utilisateur = input("Prix : ")
    prix_utilisateur = float(prix_utilisateur)
    for produit in list_products:
        if produit["prix"] <= prix_utilisateur:
            print(
                f"Produit : {produit['Nom']}, Catégorie : {produit['categorie']}, Prix : {produit['prix']} FCFA"
            )
    print("\n Fin du tri")



def main():
    programme_actif = True
    while programme_actif:
        # Affichage du menu
        print("\n============ MENU ============\n")
        print("1 - Afficher les produits")
        print("2 - Rechercher un produit")
        print("3 - Filtrer par catégorie")
        print("4 - Trier par prix")
        print("5 - Comparer le prix d'un produit")
        print("6 - Afficher l'aide")
        print("7 - À propos du programme")
        print("8 - Quitter")
        print("\n============ FIN DU MENU ============\n")

        # Demande du choix utilisateur
        choix = input("Entrez votre choix : ")
        
        match choix:
            # OPTION 1 : AFFICHER LES PRODUITS
            case "1":
                afficher_produits()

            # OPTION 2 : RECHERCHER UN PRODUIT
            case "2":
                rechercher_produit()

            # OPTION 3 : FILTRER PAR CATÉGORIE
            case "3":
                filtrer_par_categorie()

            # OPTION 4 : TRIER PAR PRIX
            case "4":
                trier_par_prix()

            # OPTION 5 : COMPARER LES PRIX D'UN PRODUIT
            case "5":
                comparaison_prix()

            # OPTION 6 : AFFICHER L'AIDE
            case "6":
                aide()

            # OPTION 7 : À PROPOS DU PROGRAMME
            case "7":
                apropos()

            # OPTION 8 : QUITTER
            case "8":
                print("\nFermeture du programme...")
                programme_actif = False

            # GESTION DES ERREURS DE MENU
            case _:
                print("\nErreur : choix invalide.")
                print("Veuillez choisir un numéro valide : 1, 2, 3, 4, 5, 6, 7 ou 8")

if __name__ == "__main__":
    main()
