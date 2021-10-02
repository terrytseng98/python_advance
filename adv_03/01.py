from tkinter import*
import datetime

def get_data():
    time=datetime.date.today()
    put_data.configure(text=time, fg='red')

def get_time():
    data=datetime.datetime.now().time()
    put_data.configure(text=data, fg='green')

windows =Tk()
windows.title('text')

canvas=Canvas(windows,width=300,height=300)
canvas.pack()

put_data=Label(windows, text='')
put_data.pack()

btn1=Button(windows, text="現在時間", command=get_time)
btn1.pack()

btn2=Button(windows, text="今天日期", command=get_data)
btn2.pack()

windows.mainloop()