# Création d'une classe Produit
class Produit:
    def __init__(self, nom_produit, categorie_produit, prix_produit):
        self.nom = nom_produit          
        self.categorie = categorie_produit  
        self.prix = prix_produit        

    # Une méthode : c'est une fonction propre à l'objet
    def __str__(self):
        return f"Produit : {self.nom}   |   Catégorie : {self.categorie}   |   Prix : {self.prix} FCFA"
