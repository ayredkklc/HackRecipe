import tkinter as tk
from os import name
from tkinter import *
import main2

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

        exitButton = Button(self, text="Exit", command=self.exitProgram)
        exitButton.place(x=0, y=0)




        #enterButton =

    #def doSomething(self, a, b):




    def exitProgram(self):
        exit()

    '''def howManyIngr(self):



        #ingredients = txtfld.get()
        return ingredients'''


    def clickSearchButton(self):
        text = Label(self, text="What are you craving?")
        text.place(x=175, y=100)
        txtfld = Entry(root, text="", bd=2)
        txtfld.place(x=190, y=130)
        txtfld.get()
        variable = StringVar()
        variable.set(txtfld.get())
        #ing = self.howManyIngr()

        text2 = Label(self, text="enter the ingredients?")
        text2.place(x=150, y=150)
        txtfld2 = Entry(root, text="", bd=2)
        txtfld2.place(x=190, y=175)
        variable2 = StringVar()
        variable2.set(txtfld2.get())


        labelww = Label(self, text = main2.list_recipes_print(variable, variable2))
        labelww.place(x=200, y=100)
        '''variable = StringVar()
        variable.set(txtfld2.get())  # You can use a variable with a string here or any string
        label = Label(self, textvariable=variable)
        label.grid(row=50, column=90)'''
        #enterBUtton = Button(self, text="Enter", command=self.doSomething(mainIng, totIng))
        #enterBUtton.place(x=50, y=50)



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