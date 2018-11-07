#############################################
# Author : Frédéric SPATARO                 #
# OS Windows 10, Python 3.7 32 bits         #
# Title : Mystery Number                    #
# License GPL                               #
#############################################


####################################################
# Libraries

from random import randint
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

####################################################
# Definitions

chasard=randint(1,100)
r=0

def nouvellePartie():
    global r,chasard
    chasard=randint(1,100)
    r=0
    textEssai["text"]="tries: 0"
    textReponse["text"]=""

def quitter():
    window.destroy()

def verif(evt):
    global chasard,r
    rep=saisieProposition.get()
    nj=int(rep)
    r=r+1
    textEssai["text"]="Tries: {}".format(r)
    if nj<chasard:
        textReponse["text"]="My number is higher!"
    elif nj>chasard:
        textReponse["text"]="My number is lower!"
    else:
        fin = messagebox.askyesno("End","You won in {} tries. Do you want to play again?".format(r))
        if fin==True:
            nouvellePartie()
        else:
            quitter()


####################################
# Window

window=Tk()
window.title('Mystery Number')
window.geometry('600x200')
bg=ImageTk.PhotoImage(file="./stuff/fond.png")
bg_label = Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

####################################################
# Widgets

Intro="I chose a number between 1 and 100, try to guess it." 
textIntro=Label(window,text=Intro, bg='white')
textIntro.pack()

saisieProposition=Entry(window)
saisieProposition.config(justify='center')
saisieProposition.pack()
saisieProposition.bind('<Return>',verif)

textReponse= Label(window, text="", bg='white')
textReponse.pack()

textEssai= Label(window, text="Tries: 0", bg='white')
textEssai.pack(side=BOTTOM, anchor=W)

#boutonRejouer=Button(fen,text='New game',command=nouvellePartie)
#boutonRejouer.pack(side=RIGHT)

####################################################
# Program

nouvellePartie()
window.mainloop()







