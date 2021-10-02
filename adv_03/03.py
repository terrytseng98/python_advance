from tkinter import*
import datetime

def convert():
    num1=float(data1.get())
    num2=data2.get()
    num3=float(data3.get())
    print(num1, num2, num3)
    if num2=='+':
        put_data.configure(text=str(num1+num3))
    elif num2=='-':
        put_data.configure(text=str(num1-num3))
    elif num2=='*':
        put_data.configure(text=str(num1*num3))
    elif num2=='/':
        put_data.configure(text=str(num1/num2))
    else:
        put_data.configure(text='請輸入數字或運算符號')

windows =Tk()
windows.title('text')

canvas=Canvas(windows,width=300,height=300)
canvas.pack()

msg1=Label(windows,text='請輸入數字1', font=('Arial', 12))
msg1.pack()
data1=Entry(windows, text='')
data1.pack()

msg2=Label(windows,text='請輸入運算符號', font=('Arial', 12))
msg2.pack()
data2=Entry(windows, text='')
data2.pack()

msg3=Label(windows,text='請輸入數字2', font=('Arial', 12))
msg3.pack()
data3=Entry(windows, text='')
data3.pack()

put_data=Label(windows, text='')
put_data.pack()

btn=Button(windows, text="結果", command=convert)
btn.pack()

windows.mainloop()