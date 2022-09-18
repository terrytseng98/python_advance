from tkinter import *

def show_fun():
    print("Hello Terry")
    display.config(text="show", fg="red", bg="black")
def clear_fun():
    display.config(text="", fg="white", bg="white")

windows=Tk()
windows.title("GUI")

btn1=Button(windows, text="show", command=show_fun, bg="red")
btn1.pack()

btn2=Button(windows, text="clear", command=clear_fun, bg="red")
btn2.pack()

display=Label(windows, text="")
display.pack()
windows.mainloop()