from tkinter import*
import datetime

def convert():
    data=inch_data.get()
    print(data)
    if data !='':
        put_str=str(int(data)*2.54)
        put_data.configure(text=put_str)

windows =Tk()
windows.title('text')

canvas=Canvas(windows,width=300,height=300)
canvas.pack()

msg=Label(windows,text='請輸入英吋', font=('Arial', 12))
msg.pack()

inch_data=Entry(windows, text='')
inch_data.pack()

put_data=Label(windows, text='')
put_data.pack()

btn=Button(windows, text="轉成公分", command=convert, bg="red")
btn.pack()

windows.mainloop()