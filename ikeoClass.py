class Product:

    def __init__(self, id, name, ref_produit, aband_produit, description_produit, fournisseur=[]):
        self.id = id
        self.name = name
        self.ref_produit = ref_produit
        self.aband_produit = aband_produit
        self.description_produit = description_produit
        self.fournisseur = fournisseur

    def __repr__(self):
        return self.name
