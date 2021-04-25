from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def prodRegister():
    nom_produit = prodInfo1.get()
    ref_produit = prodInfo2.get()
    aband_produit = prodInfo3.get()
    desription_produit = prodInfo4.get()

    insertBooks = "insert into " + cliTable + " values('" + nom_produit + "','" + ref_produit + "','" + aband_produit + "','"+ desription_produit + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Produit ajouté ")
    except:
        messagebox.showinfo("Error", "Error Database")


    root.destroy()


def addProd():
    global prodInfo1, prodInfo2, prodInfo3, prodInfo4, Canvas1, con, cur, cliTable, root

    root = Tk()
    root.title("Ikeo")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase = "ikeo"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    cliTable = "produits(nom_produit,ref_produit,aband_produit,desription_produit)"  # cli Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ajouter un produit", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Nom
    lb1 = Label(labelFrame, text="Nom : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    prodInfo1 = Entry(labelFrame)
    prodInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Ref
    lb2 = Label(labelFrame, text="Ref : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    prodInfo2 = Entry(labelFrame)
    prodInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Aband
    lb3 = Label(labelFrame, text="Abandon : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    prodInfo3 = Entry(labelFrame)
    prodInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Desc
    lb4 = Label(labelFrame, text=" Description: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    prodInfo4 = Entry(labelFrame)
    prodInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Button
    SubmitBtn = Button(root, text="Enregistrez", bg='#d1ccc0', fg='black', command=prodRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quitter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
