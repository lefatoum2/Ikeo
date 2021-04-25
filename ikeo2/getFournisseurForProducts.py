from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
con = pymysql.connect(host="localhost", user="root", password="root", database="ikeo")
cur = con.cursor()

# Enter Table Names here
# Table = "Fournisseurs"


def View3():
    root = Tk()
    root.title("Ikeo")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#808000")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFC0CB", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Fournisseurs", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-40s%-40s%-40s%-40s" % ('nom_produit', 'ref_produit', 'aband_produit','desription_produit'), bg='black', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    # Data
    products = "select * from produits"
    getProducts ="SELECT site_de_production.nom FROM site_de_production JOIN produit_site ON site_de_production.id_site=produit_site.id_site where produit_site.id_produit=" + str(products.id_produit)


    try:
        cur.execute(getProducts)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-40s%-40s%-40s" % (i[1], i[2], i[3], i[4]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quitter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()