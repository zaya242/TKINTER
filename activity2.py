#Write a Python program to - create a Tkinter window, set title to it, and set its geometry. 
# Then add these widgets to the window - Label, Button, Entry, Frame, 
# and a Text box.

from tkinter import *

window=Tk()

window.title("My first Tkinter window")
window.geometry("600x580")

for i in range(3):
    for j in range(3):
        frame=Frame(master=window,relief=GROOVE,borderwidth=8)
        frame.grid(row=i,column=j,padx=8,pady=8)
        label=Label(master=frame,text=f"Red{i}...Blue{j}")
        label.pack()

window.mainloop()        