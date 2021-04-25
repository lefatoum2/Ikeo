from getAllProducts import *
from SetClient import *
from SetProduct import *
from SetFacture import *
from facture import *
from getFournisseurForProducts import *

#  Database
con = pymysql.connect(host="localhost", user="root", password="root", database="ikeo")
cur = con.cursor()


root = Tk()
root.title("IKEO")
root.minsize(width=400, height=800)
root.geometry("600x500")

same = True
n = 0.25


# background image
background_image = Image.open("pexels-andrea-piacquadio-3778966.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)


# Canvas
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

# Frame
headingFrame1 = Frame(root, bg="#FFC0CB", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n IKEO", bg='black', fg='white',
                     font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# Boutons
btn1 = Button(root, text="Tous les produits", bg='black', fg='white', command=View)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Tous les fournisseurs", bg='black', fg='white', command=View3)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Facture", bg='black', fg='white', command=searchfact)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Enregistrer une facture", bg='black', fg='white', command=addFact)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Enregistrer un client", bg='black', fg='white', command=addCli)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Enregistrer un produit", bg='black', fg='white', command=addProd)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

quitBtn = Button(root, text="Quitter", bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.05)

root.mainloop()