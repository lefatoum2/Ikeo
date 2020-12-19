from version0.ikeoClass import Product
import mysql.connector


class BDD:

    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'ikeo'
        })
        cls.cursor = cls.link.cursor()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def getAllProducts(cls):
        cls.connect()
        productList = []
        query = "SELECT * FROM produits"
        cls.cursor.execute(query)
        liste = cls.cursor.fetchall()
        for row in liste:
            id = int(row[0])
            name = str(row[1])
            ref = str(row[2])
            description = str(row[3])
            aband = str(row[4])
            product = Product(id, name, ref, description, aband)
            productList.append(product)
        cls.close()
        return productList

    @classmethod
    def getFournisseurForProducts(cls):
        products = cls.getAllProducts()
        cls.connect()
        productWithFournisseur = []

        for product in products:
            query = "SELECT site_de_production.nom FROM site_de_production JOIN produit_site ON site_de_production.id_site=produit_site.id_site where produit_site.id_produit=" + str(
                product.id)
            cls.cursor.execute(query)
            liste = cls.cursor.fetchall()
            listeFournisseur = []
            for row in liste:
                name = str(row[0])
                listeFournisseur.append(name)
            product.fournisseur = listeFournisseur
            productWithFournisseur.append(product)
        cls.close()
        return productWithFournisseur

    @classmethod
    def facture(cls, id_cli, date1):
        cls.connect()
        cli1 = []
        query = " select numero_facture from facture where id_client= %s and date_facture= %s"
        value = (id_cli, date1)
        cls.cursor.execute(query, value)
        list1 = cls.cursor.fetchall()
        for lst in list1:
            cli1.append(lst)
        cls.close()
        return cli1

    @classmethod
    def SetFacture(cls, numfact, datefact, id_cli):
        cls.connect()
        value = (numfact, datefact, id_cli)
        query = "INSERT INTO facture(numero_facture, date_facture ,id_client) VALUE(%s, %s, %s)"
        cls.cursor.execute(query, value)
        cls.close()
        pass

    @classmethod
    def SetClient(cls, type1, raison, adresse, id_ville):
        cls.connect()
        value = (type1, raison, adresse, id_ville)
        query = "INSERT INTO clients(id_type, id_raison, adresse_client) VALUE(%s, %s, %s)"
        cls.cursor.execute(query, value)
        cls.close()
        pass

    @classmethod
    def SetProduct(cls, nom, ref, aband, desc):
        cls.connect()
        value = (nom, ref, aband, desc)
        query = "INSERT INTO produits(nom_produit, ref_produit, aband_produit, description_produit) VALUE(%s, %s, %s, %s)"
        cls.cursor.execute(query, value)
        cls.close()
        pass
