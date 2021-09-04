from tkinter import *

def hi_fun():
    print("Hello Terry")
    display.config(text="Hello Terry", fg="green", bg="black")

windows=Tk()
windows.title("GUI")

btn=Button(windows, text="click Me", command=hi_fun, bg="red")
btn.pack()
display=Label(windows, text="")
display.pack()
windows.mainloop()