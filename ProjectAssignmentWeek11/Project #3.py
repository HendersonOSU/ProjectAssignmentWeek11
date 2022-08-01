from tkinter import *
def celcius():
    val=float(c.get())
    convert=(val*9/5) + 32
    f.set(convert)

def Fahrenheit():
    val=float(f.get())
    convert=(val-32)*(5/9)
    c.set(convert)
head = Tk()
head.geometry("400x100")
head.title("F/C Converter")
L1=Label(head,text="Celsius")
L2=Label(head,text="Fahrenheit")
c=StringVar()
c.set("0.0")

f=StringVar()
f.set("32.0")
E1=Entry(head,textvariable=c)
E2=Entry(head,textvariable=f)
B1=Button(head,text=">>",bg="light blue",command=celcius)
B2=Button(head,text="<<",bg="light blue",command=Fahrenheit)
L1.grid(row=0,column=0)
L2.grid(row=0,column=1)
E1.grid(row=1,column=0)
E2.grid(row=1,column=1)
B1.grid(row=2,column=0)
B2.grid(row=2,column=1)

head.mainloop()
