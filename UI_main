import tkinter as tk
from os import name
from tkinter import *

from PyQt5.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

root = tk.Tk()
is_on=False



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH,expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Recipes")
        fileMenu.add_command(label="ingredients")
        fileMenu.add_command(label="Exit Program", command=self.exitProgram)
        menu.add_cascade(label="Search", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        text = Label(self,text="Welcome to the Cooking App?")
        text.place(x=175,y=50)

        searchButton = Button(self, text="Search", command=self.clickSearchButton)
        searchButton.place(x=200,y=75)

        settingButton = Button(self, text="Setting", command=self.clickSettingButton)
        settingButton.place(x=225, y=300)

    def exitProgram(self):
        exit()

    def howManyIngr(self):
        text = Label(self,text="how many ingredents do you have?")
        text.place(x=150,y=150)
        txtfld=Entry(root,text="",bd=2)
        txtfld.place(x=190,y=175)
        txtfld.get()

    def clickSearchButton(self):
        text = Label(self, text="What are you craving?")
        text.place(x=175, y=100)
        txtfld = Entry(root, text="", bd=2)
        txtfld.place(x=190, y=130)
        self.pv= txtfld.get()
        self.howManyIngr()
        txtfld.get()



    def clickSettingButton(self, is_on=False):
        calLabel = Button(root,text="Calories",fg='black',font=("Helvetica",16))
        calLabel.pack(pady = 20)
        calLabel.place(x=200,y=200)

        allLabel = Button(root,text="Allergies",fg='black',font=("Helvetica",16))
        allLabel.pack(pady = 20)
        allLabel.place(x=100,y=200)

        vegenLabel = Button(root,text="Vegan",fg='black',font=("Helvetica",16))
        vegenLabel.pack(pady = 20)
        vegenLabel.place(x=300,y=200)

root.geometry("500x500")
app = Window(root)
root.wm_title("Cooking App")
root.mainloop()
