from tkinter import*
def move_canvas(event):
    key=event.keysym
    print(key)
    if key=="Right":
        canvas.move(circle,20,0)
    elif key=="Left":
        canvas.move(circle,-20,0)
    elif key=="Up":
        canvas.move(circle,0,-20)
    elif key=="Down":
        canvas.move(circle,0,20)
    elif key=="d":
        canvas.move(rec,20,0)
    elif key=="a":
        canvas.move(rec,-20,0)
    elif key=="w":
        canvas.move(rec,0,-20)
    elif key=="s":
        canvas.move(rec,0,20)

windows=Tk()
windows.title("Terry")
canvas=Canvas(windows,width=600,height=600)
canvas.pack()

img=PhotoImage(file="adv_02/crocodile2.gif")
my_img=canvas.create_image(300,300,image=img)

circle=canvas.create_oval(300,300,200,200,fill="green")
canvas.bind_all('<Key>',move_canvas)

rec=canvas.create_rectangle(250,150,300,200,fill="green")
canvas.bind_all('<Key>',move_canvas)

msg=canvas.create_text(300,100,text="Crocodile",fill="black",font=('Arial',30))

windows.mainloop()