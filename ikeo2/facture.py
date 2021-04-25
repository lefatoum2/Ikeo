from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Database
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Table
factTable = "facture"

# Listes
allBid = []


def fact1():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    Label(labelFrame2,
          text="%-40s%-40s%-40s%-40s" % ('nom_produit', 'ref_produit', 'aband_produit', 'desription_produit'),
          bg='black', fg='white').place(
        relx=0.1, rely=0.7)
    Label(labelFrame2,
          text="-----------------------------------------------------------------------------------------------------------------------------",
          bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getProducts = "select * from " + factTable + " where id_cli = '" + bid + "'"
    try:
        cur.execute(getProducts)
        con.commit()
        for i in cur:
            Label(labelFrame2, text="%-40s%-40s%-40s%-40s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")



    print(bid)
    print(issueto)

    allBid.clear()


def searchfact():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status, labelFrame2, y

    root = Tk()
    root.title("Ikeo")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # ID Client
    lb1 = Label(labelFrame, text="ID Client: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Date de la facture
    lb2 = Label(labelFrame, text="Date de la facture : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)


    # Affichage
    labelFrame2 = Frame(root, bg='black')
    labelFrame2.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)
    y = 0.25



    #Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=fact1)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()