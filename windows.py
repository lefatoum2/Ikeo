import tkinter as tk
import tkinter as tk
import requests
from version0.bdd import *
from version0.ikeoClass import *

HEIGHT = 900
WIDTH = 1000
db1 = BDD()

root = tk.Tk()
root.title("IKEO")


# Fonction
def ouvrir():
    pass


# Menu
menubar = tk.Menu(root)
root.config(menu=menubar)
menufichier = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Ouvrir", command=ouvrir())
menufichier.add_separator()
menufichier.add_command(label="Enregistrer")
menufichier.add_command(label="Enregistrer sous")
menufichier.add_separator()
menufichier.add_command(label="Quitter", command=root.quit)

# Taille de la fenètre d'image
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Position de l'Image d'arrière-plan qui doit être en png
background_image = tk.PhotoImage(file='2279383.png')

background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#e9967a', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Taille et position du bouton
button1 = tk.Button(frame, text="All Products", font=40, command=lambda: label.configure(text=db1.getAllProducts()))
button1.place(relx=0.8, relheight=1, relwidth=0.2)

button2 = tk.Button(frame, text="All Suppliers", font=40,
                    command=lambda: label.configure(text=db1.getFournisseurForProducts()))
button2.place(relx=0.6, relheight=1, relwidth=0.2)

button3 = tk.Button(frame, text="yes2", font=40, command=lambda: label.configure())
button3.place(relx=0.4, relheight=1, relwidth=0.2)

button4 = tk.Button(frame, text="yes3", font=40, command=lambda: label.configure())
button4.place(relx=0.2, relheight=1, relwidth=0.2)

button5 = tk.Button(frame, text="yes4", font=40, command=lambda: label.configure())
button5.place(relx=0.0, relheight=1, relwidth=0.2)

lower_frame = tk.Frame(root, bg='#e9967a', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.45, relheight=0.38, anchor='n')

# Taille du label
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
