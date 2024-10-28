import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox


win = tk.Tk()

win.title('New GUI')
win.config(background='#000000')
win.geometry('800x800')

def terminateWindow():
    win.destroy()

def outputFunction():
    outputLabel.config(text = f' Hello {entryNameVariable.get()}, your order of a {radVar.get()} pizza, with {pizzaSauceComboBox.get()} sauce, \n and with toppings.')
#Creating Menu
mainMenu = tk.Menu(win)

mainMenu.add_command(label='End Session', command=terminateWindow)

win.configure(menu=mainMenu)

#Crating frame to hold title/header of page
titleFrame = tk.Frame(win)
titleFrame.pack()
#Crating welcome label to welcome users
welcomeLabel=tk.Label(titleFrame,text='Welcome to Charlie\'s pizza parlor', foreground='#ffffff',background='#000000'
, font='Arial 18')
welcomeLabel.pack()

#Crating Frame to hold all of Body
bodyFrame = tk.Frame(win)
bodyFrame.pack()

#Creating label to ask for User's name
askNameLabel= tk.Label(bodyFrame, text='What is your Name:',background='#000000',foreground='#ffffff')
askNameLabel.grid(row=0,column=0)
#Creating Entry to take users input for their name

entryNameVariable = tk.StringVar()
nameEntry = tk.Entry(bodyFrame, textvariable=entryNameVariable)
nameEntry.grid(row=0,column=1)

#Crating Label to ask what type of Pizza Crust
askPizzaCrustLabel = tk.Label(win, text='What type of Pizza Crust would you like?',
background='#000000',foreground='#ffffff')
askPizzaCrustLabel.pack()

#Creating Frame to hold RadioButtons
radioFrame=tk.Frame(win, background='#000000')
radioFrame.pack()

def pizzaCrustFunction():
    radSel = radVar.get()
    if radSel == 0:
        mBox.showinfo(title="Note", message='You have selected Thin Crust')
    elif radSel == 1:
        mBox.showinfo(title='Note', message='You have selected Thick Crust')
    elif radSel == 2:
        mBox.showinfo(title='Note', message='You have selected No Crust')
    

#Creating Radiobuttons
radVar = tk.IntVar()
radVar.set(-1)

thinCrustRadio = tk.Radiobutton(radioFrame, text='Thin Crust', variable=radVar, value=0, width=10, background='#000000', foreground='#ffffff', command=pizzaCrustFunction)
thinCrustRadio.grid(column=0,row=1)

thickCrustRadio = tk.Radiobutton(radioFrame, text='Thick Crust', variable=radVar, value=1, width=10, background='#000000', foreground='#ffffff',command=pizzaCrustFunction)
thickCrustRadio.grid(column=1,row=1)

noCrustRadio = tk.Radiobutton(radioFrame, text='No Crust', variable=radVar, value=2, width=10, background='#000000', foreground='#ffffff',command=pizzaCrustFunction)
noCrustRadio.grid(column=2,row=1)

#Creaing label to ask what type of Sauce the User wants
askPizzaSauceLabel = tk.Label(win, text='What type of Pizza Sauce would you like?',
background='#000000',foreground='#ffffff')
askPizzaSauceLabel.pack()
#Creating Frame to hold the types of Sauces
pizzaSauceFrame = tk.Frame(win, background='#000000')
pizzaSauceFrame.pack()

#Creating list that holds Pizza Sauces
pizzaSauceList = ['Maranara',' Alfredo', 'Vegetable', 'Four-Cheese']

pizzaSauceComboBox = ttk.Combobox(pizzaSauceFrame)
pizzaSauceComboBox['state'] = 'readonly'
pizzaSauceComboBox.grid(column=0,row=0)
pizzaSauceComboBox['values'] = ['Maranara', 'Alfredo', 'Vegetable', 'Four-Cheese']
pizzaSauceComboBox.set('Select Pizza Sauce')

#Creating Label to ask what toppings user wants

askPizzaToppingsLabel = tk.Label(win, text='What type of Pizza Toppings would you like?',
background='#000000',foreground='#ffffff')
askPizzaToppingsLabel.pack()

#Creating Frame to house pizza toppings

pizzaToppingFrame = tk.Frame(win, background='#000000')
pizzaToppingFrame.pack()


#Creating checkbox to house the toppings
checkVariable = tk.IntVar()

toppingList = ['Sausage', 'Peperoni', 'Extra-Cheese', 'Cheese Only', 'Bacon', 'Canadian Bacon', 'Olives', 'Pineapple', 'Mushrooms', 'Hamburger']
onCounter = 1
offCounter = 0
columnCounter = 0
checkBoxStringVar = tk.StringVar()
for i in toppingList:
    pizzaToppingCheckBox =tk.Checkbutton(pizzaToppingFrame, text=i,onvalue = onCounter, offvalue = offCounter, )
    pizzaToppingCheckBox.grid(column=0,row=columnCounter)
    onCounter = onCounter ++ 1
    offCounter = offCounter ++ 1
    columnCounter = columnCounter ++ 1

#Creating Label to tell user to select submit if order is complete
orderCompletetLabel = tk.Label(win, text='Click Submit if your order is complete',
background='#000000',foreground='#ffffff')
askPizzaCrustLabel.pack()

#Creating submit frame
submitFrame = tk.Frame(win,background="#000000")
submitFrame.pack()


dummyLabel = tk.Label(submitFrame, text='',background='#000000',foreground='#000000')
dummyLabel.grid(column=0,row=0)

submitButton = tk.Button(submitFrame, text='Submit', width=10, command=outputFunction)
submitButton.grid(column=0,row=1)


#Creating output Label

outputLabel = tk.Label(win, text='',
background='#000000',foreground='#ffffff')
outputLabel.pack()


win.mainloop()