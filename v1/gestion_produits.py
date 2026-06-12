from data import products

class Gestion_Produits:
    def __init__(self):
        self.liste_produits = []
        for product in products:
            self.liste_produits.append(product)


    def ajouter_produit(self, produit):
        self.liste_produits.append(produit)

        
    def afficher_produits(self):
        """
        fonction qui affiche les produits
        """
        print("\n=== Affichage des produits ===\n")

        for produit in self.liste_produits:
            print(produit)


    def rechercher_produit(self, produit_reccherche):
        """
        méthode de recherche d'un produit en fonction du nom
        """
        print("\n=== Recherche de produit :", produit_reccherche, " ===\n")
        for produit in self.liste_produits:
            if produit.nom.lower() == produit_reccherche.lower():
                print(produit)
                break
        else:
            print("Produit non trouvé")

    
    def filtrer_par_categorie(self, categorie_recherche):
        """
        méthode de recherche les produits d'une catégorie
        """  
        print("\n=== Filtre par catégorie :", categorie_recherche," ===\n")
        
        resultats = []
        
        # On suppose d'abord qu'on n'a trouvé aucun produit
        produit_trouve = False

        for produit in self.liste_produits:
            if produit.categorie.lower() == categorie_recherche.lower():
                resultats.append(produit)
                produit_trouve = True  # Ici On note qu'on a trouvé au moins un produit
        for produit in resultats:
            print(produit)

        # Traitement si aucun produit n'a été trouvé : produit_trouve = False
        if not produit_trouve:
            print("Aucun produit trouvé dans la catégorie ", categorie_recherche.lower())
