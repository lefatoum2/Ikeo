from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def clientRegister():
    id_type = cliInfo1.get()
    id_raison = cliInfo2.get()
    adresse_client = cliInfo3.get()
    id_ville = cliInfo4.get()

    insertBooks = "insert into " + cliTable + " values('" + id_type + "','" + id_raison + "','" + adresse_client + "','"+ id_ville + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Client ajouté ")
    except:
        messagebox.showinfo("Error", "Error Database")


    root.destroy()


def addCli():
    global cliInfo1, cliInfo2, cliInfo3, cliInfo4, Canvas1, con, cur, cliTable, root

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
    cliTable = "clients(id_type,id_raison, adresse_client ,id_ville)"  # cli Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ajouter un client", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Type
    lb1 = Label(labelFrame, text="Type : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    cliInfo1 = Entry(labelFrame)
    cliInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Raison
    lb2 = Label(labelFrame, text="Raison : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    cliInfo2 = Entry(labelFrame)
    cliInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Adresse
    lb3 = Label(labelFrame, text="Adresse : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    cliInfo3 = Entry(labelFrame)
    cliInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # ID Ville
    lb4 = Label(labelFrame, text=" ID Ville: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    cliInfo4 = Entry(labelFrame)
    cliInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="Enregistrez", bg='#d1ccc0', fg='black', command=clientRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quitter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
