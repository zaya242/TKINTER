from tkinter import *

window=Tk()

window.title("My first Tkinter window")
window.geometry("600x580")

label1=Label(text="Welcome",fg="red",bg="cornflowerblue",height=9,width=9)
button1=Button(text="Click Here",fg="darkcyan")
entry1=Entry()
text1=Text(bg="darkslateblue")
frame=Frame(master=window,relief=RAISED,borderwidth=7)
label2=Label(master=frame,text="Inside frame")


label1.pack()
entry1.pack()
button1.pack()

frame.pack()
label2.pack()
text1.pack()
window.mainloop()