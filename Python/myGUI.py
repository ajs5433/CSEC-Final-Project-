import sys
from tkinter import *
from PyQt4 import QtGui


class myGUI():
#myAttributes

    def __init__(self, master):
        buttonsize = 16
        self.master = master
        master.title('Password Generator: Select your character')
        header = StringVar()

        #Frame
        self.topframe = Frame(master)
        self.topframe.pack(side = TOP)

        #TextBox"
        self.txtDisplay = Entry(master, textvariable = header, bd =20, insertwidth= 1, font =  30)
        self.txtDisplay.pack(side = TOP)

        #Buttons
        self.button1 = Button(master, padx = buttonsize, pady = buttonsize, bd = 8, text='', fg='Black')
        self.button1.setToolTip('this is a message')
        self.button1.pack(side=LEFT)


