import tkinter as tk
from tkinter import ttk
from tkinter import Menu


window = tk.Tk()

socialMediaList = ['Facebook', 'Instagram', "Twitter"]

mainMenu = Menu(window)

socialMenu = Menu(mainMenu, tearoff=0)
socialMenu.add_command(label=socialMediaList[0])
socialMenu.add_command(label=socialMediaList[1])
socialMenu.add_command(label=socialMediaList[2])


mainMenu.add_cascade(label='Social Media',menu=socialMenu)

window.config(menu=mainMenu)

window.config(background='#000000')


window.mainloop()