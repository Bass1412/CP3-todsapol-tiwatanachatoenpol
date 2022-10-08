from tkinter import *
import math

def leftClickbutton(event):
    print("leftClick")

def rightClickButton(event):
    # print(float(textboxweight.get())/math.pow(float(textboxheigh.get())/100,2))
    result = float(textboxweight.get())/math.pow(float(textboxheigh.get())/100,2)
    if result >= 30 :
        labelResult.configure(text= "อ้วนมาก")
    elif result >= 25:
        labelResult.configure(text="อ้วน")
    elif result >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif result >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ")
    else:
        labelResult.configure(text="ผอมเกินไป")

    # rint(type(textboxweight.get()))
    # labelResult.configure(text=float(textboxweight.get())/math.pow(float(textboxheigh.get())/100,2))

mainwindown = Tk()
lableheigh = Label(mainwindown,text="ส่วนสูง(cm.)")
lableheigh.grid(row=0,column=0)
textboxheigh = Entry(mainwindown)
textboxheigh.grid(row=0,column=1)
lableweight = Label(mainwindown,text="น้ำหนัก(kg)")
lableweight.grid(row=1,column=0)
textboxweight = Entry(mainwindown)
textboxweight.grid(row=1,column=1)
calculatebutton = Button(mainwindown,text="คำนวน")
calculatebutton.grid(row=2,column=0)
labelResult = Label(mainwindown,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
calculatebutton.bind("<Button-1>",rightClickButton)



mainwindown.mainloop()