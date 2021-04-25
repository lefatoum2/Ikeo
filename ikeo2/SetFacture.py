from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def factRegister():
    numero_facture = factInfo1.get()
    date_facture = factInfo2.get()
    id_client = factInfo3.get()

    insertBooks = "insert into " + factTable + " values('" + numero_facture + "','" + date_facture + "','" + id_client + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Facture ajouté ")
    except:
        messagebox.showinfo("Error", "Error Database")


    root.destroy()


def addFact():
    global factInfo1, factInfo2, factInfo3, Canvas1, con, cur, factTable, root

    root = Tk()
    root.title("Ikeo")
    root.minsize(width=400, height=800)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase = "ikeo"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    factTable = "facture(numero_facture,date_facture, id_client)"  # cli Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ajouter une facture", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Numero facture
    lb1 = Label(labelFrame, text="Numéro de facture : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    factInfo1 = Entry(labelFrame)
    factInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Date facture
    lb2 = Label(labelFrame, text=" Date de la facture: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    factInfo2 = Entry(labelFrame)
    factInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Id_client
    lb3 = Label(labelFrame, text="ID Client : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    factInfo3 = Entry(labelFrame)
    factInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)


    # Button
    SubmitBtn = Button(root, text="Enregistrez", bg='#d1ccc0', fg='black', command=factRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quitter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
