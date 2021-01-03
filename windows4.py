import tkinter as tk
from tkinter import messagebox
from version0.bdd import BDD

db1 = BDD()


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('IKEO')
        master.geometry("700x600")
        self.create_widgets()
        self.background_image = tk.PhotoImage(file='2279383.png')
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # Set Facture
        # StringVar Facture
        self.numfact = tk.StringVar()
        self.datefact = tk.StringVar()
        self.id_cli = tk.StringVar()
        # Button Facture
        self.set_facture_btn = tk.Button(self.master, text='Enregistrez la facture', font=('Gabriola', 11),
                                         command=db1.SetFacture(self.numfact, self.datefact, self.id_cli))
        # Entry Facture
        self.numfact_entry = tk.Entry(self.master, textvariable=self.numfact)
        self.datefact_entry = tk.Entry(self.master, textvariable=self.datefact)
        self.id_cli_entry = tk.Entry(self.master, textvariable=self.id_cli)
        # Label Facture
        self.facture_label = tk.Label(self.master, text='Facture', font=('Gabriola', 14))
        self.numfact_label = tk.Label(self.master, text='numfact', font=('Gabriola', 10))
        self.id_cli_label = tk.Label(self.master, text='datefact', font=('Gabriola', 10))
        self.datefact_label = tk.Label(self.master, text='id_cli', font=('Gabriola', 10))
        # Grid Facture
        self.set_facture_btn.grid(row=0, column=1)
        self.numfact_entry.grid(row=1, column=1)
        self.datefact_entry.grid(row=2, column=1)
        self.id_cli_entry.grid(row=3, column=1)
        self.facture_label.grid(row=0, column=0)
        self.numfact_label.grid(row=1, column=0)
        self.datefact_label.grid(row=2, column=0)
        self.id_cli_label.grid(row=3, column=0)

        # Set Client
        # StringVar Client
        self.type1 = tk.StringVar()
        self.raison = tk.StringVar()
        self.adresse = tk.StringVar()
        self.id_ville = tk.StringVar()
        # Button Client
        self.set_client_btn = tk.Button(self.master, text='Enregistrez le client', font=('Gabriola', 11),
                                        command=db1.SetClient(self.type1, self.raison, self.adresse, self.id_ville))

        # Entry Client
        self.type1_entry = tk.Entry(self.master, textvariable=self.type1)
        self.raison_entry = tk.Entry(self.master, textvariable=self.raison)
        self.adresse_entry = tk.Entry(self.master, textvariable=self.adresse)
        self.id_ville_entry = tk.Entry(self.master, textvariable=self.id_ville)

        # Label Client
        self.type1_label = tk.Label(self.master, text='Type', font=('Gabriola', 10))
        self.raison_label = tk.Label(self.master, text='Raison', font=('Gabriola', 10))
        self.adresse_label = tk.Label(self.master, text='Adresse', font=('Gabriola', 10))
        self.id_ville_label = tk.Label(self.master, text='Id_ville', font=('Gabriola', 10))
        self.client_label = tk.Label(self.master, text='Client', font=('Gabriola', 14))

        # Grid Client
        self.set_client_btn.grid(row=0, column=3)

        self.type1_entry.grid(row=1, column=3)
        self.raison_entry.grid(row=2, column=3)
        self.adresse_entry.grid(row=3, column=3)
        self.id_ville_entry.grid(row=4, column=3)

        self.type1_label.grid(row=1, column=2)
        self.raison_label.grid(row=2, column=2)
        self.adresse_label.grid(row=3, column=2)
        self.id_ville_label.grid(row=4, column=2)
        self.client_label.grid(row=0, column=2)

        # Set Product
        # StringVar Product

        self.nom = tk.StringVar()
        self.ref = tk.StringVar()
        self.aband = tk.StringVar()
        self.desc = tk.StringVar()
        # Button Product
        self.set_product_btn = tk.Button(self.master, text='Enregistrez le produit', font=('Gabriola', 11),
                                         command=db1.SetProduct(self.nom, self.ref, self.aband, self.desc))

        # Entry Product
        self.nom_entry = tk.Entry(self.master, textvariable=self.nom)
        self.ref_entry = tk.Entry(self.master, textvariable=self.ref)
        self.aband_entry = tk.Entry(self.master, textvariable=self.aband)
        self.desc_entry = tk.Entry(self.master, textvariable=self.desc)
        # Label Product
        self.nom_label = tk.Label(self.master, text='Nom', font=('Gabriola', 10))
        self.ref_label = tk.Label(self.master, text='Référence', font=('Gabriola', 10))
        self.aband_label = tk.Label(self.master, text='Abandon', font=('Gabriola', 10))
        self.desc_label = tk.Label(self.master, text='Description', font=('Gabriola', 10))
        self.product_label = tk.Label(self.master, text='Product', font=('Gabriola', 14))

        # Grid Product
        self.set_product_btn.grid(row=0, column=5)

        self.nom_entry.grid(row=1, column=5)
        self.ref_entry.grid(row=2, column=5)
        self.aband_entry.grid(row=3, column=5)
        self.desc_entry.grid(row=4, column=5)

        self.nom_label.grid(row=1, column=4)
        self.ref_label.grid(row=2, column=4)
        self.aband_label.grid(row=3, column=4)
        self.desc_label.grid(row=4, column=4)
        self.product_label.grid(row=0, column=4)

        # Get Fournisseur*
        # Button Fournisseur
        self.set_fournisseur_btn = tk.Button(self.master, text='Afficher les fournisseurs', font=('Gabriola', 11),
                                             command=db1.getFournisseurForProducts())
        # Label Fournisseur
        self.fournisseur_label = tk.Label(self.master, text='Fournisseurs', font=('Gabriola', 14))

        # Grid Fournisseur
        self.set_fournisseur_btn.grid(row=6, column=3)
        self.fournisseur_label.grid(row=6, column=2)

        # Get Products
        # Button Products
        self.set_products_btn = tk.Button(self.master, text='Affichez les produits', font=('Gabriola', 11),
                                          command=db1.getAllProducts())
        # Label Products
        self.products_label = tk.Label(self.master, text='Products', font=('Gabriola', 14))

        # Grid Products
        self.set_products_btn.grid(row=6, column=5)
        self.products_label.grid(row=6, column=4)

        # Get Facture
        # StringVar Facture
        self.id_cli = tk.StringVar()
        self.date1 = tk.StringVar()
        # Entry Facture
        self.id_cli_entry = tk.Entry(self.master, textvariable=self.id_cli)
        self.date1_entry = tk.Entry(self.master, textvariable=self.date1)
        # Label Facture
        self.facture_label = tk.Label(self.master, text='Get Facture', font=('Gabriola', 14))
        self.id_cli1_label = tk.Label(self.master, text='Id_client', font=('Gabriola', 10))
        self.date1_label = tk.Label(self.master, text='Date', font=('Gabriola', 10))
        # Button Facture
        self.get_facture_btn = tk.Button(self.master, text='Affichez la facture', font=('Gabriola', 11),
                                         command=db1.facture(self.id_cli, self.date1))
        # Grid Facture
        self.id_cli_entry.grid(row=7, column=1)
        self.date1_entry.grid(row=8, column=1)
        self.facture_label.grid(row=6, column=0)
        self.id_cli1_label.grid(row=7, column=0)
        self.date1_label.grid(row=8, column=0)
        self.get_facture_btn.grid(row=6, column=1)

        # Label/listbox display
        self.list1 = tk.Listbox(self.master, height=8, width=50, border=0)
        self.list1.grid(row=9, column=1, columnspan=3,
                        rowspan=6, pady=50, padx=50)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
