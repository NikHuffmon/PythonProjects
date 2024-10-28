import tkinter as tk
from tkinter import Checkbutton, ttk

win= tk.Tk()


selectVariableOne =tk.IntVar()
selectVariableTwo = tk.IntVar()

def testTwo():
    print(checkBoxOne.cget('text'))
    if selectVariableOne.get() == 1:
        print('On')
    else:
        print('DIE')

def radioCommand():
    radSel = radVar.get()
    if radSel == 0:
        print('Off')
    else:
        print('On')



radVar = tk.IntVar()
radVar.set(-1)

radioOne = tk.Radiobutton(win, text='Off', variable=radVar, value=0, command=radioCommand)
radioOne.pack()

radioTwo = tk.Radiobutton(win, text='On', variable=radVar, value=1, command=radioCommand)
radioTwo.pack()



checkBoxOne = tk.Checkbutton(win, text='Yes', variable=selectVariableOne, onvalue=1, offvalue=0,command=testTwo)
checkBoxOne.pack()


checkBoxTwo = tk.Checkbutton(win, text='No', variable=selectVariableTwo,onvalue=2,offvalue=3, comman=testTwo)
checkBoxTwo.pack()






win.mainloop()