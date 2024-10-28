import tkinter as tk


win = tk.Tk()







def nextScreen(radVar):
    print(radVar)


radVar = tk.IntVar()


radioButtonHockey = tk.Radiobutton(win, text="Hockey", variable=radVar, value=1)
radioButtonHockey.pack()


radioButtonSoccer = tk.Radiobutton(win,text='Soccer', variable=radVar, value=2)
radioButtonSoccer.pack()

nextScreen(radVar)
win.mainloop()