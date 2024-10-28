#Building GUI to help with average of numbers
import tkinter as tk

window = tk.Tk()
window.title("Average of Numbers")
window.geometry("300x200")


def average():
    #Get the numbers from the entry boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    num4 = float(entry4.get())
    num5 = float(entry5.get())
    #Calculate the average
    avg = (num1 + num2 + num3 + num4 + num5)/5
    #Display the average
    label = tk.Label(window, text="The average is: " + str(avg))
    label.grid(row=6, column=0)

#Create the entry boxes
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)


entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)


entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)


entry4 = tk.Entry(window)
entry4.grid(row=3, column=1)


entry5 = tk.Entry(window)
entry5.grid(row=4, column=1)


#Creating the button
button = tk.Button(window, text="Average", command=average)
button.grid(row=5, column=1)

#Create the label
label = tk.Label(window, text="Please enter 5 numbers")
label.grid(row=0, column=0)











window.mainloop()