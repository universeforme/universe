from tkinter import*

def get():

    Height=float(a1.get())
    Weight=float(a2.get())
    v=Height/100
    get=Weight/(v*v)
    print(get)
    t4.set(get)
    a3.update()

window=Tk()
window.title("BMI Calculator")
window.geometry("500x500")
window.resizable(True,True)

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()


f=Frame(window)
f.pack()

l=Label(f,text="Age")
l.grid(row=1,column=0)

a=Entry(f,textvariable=t1)
a.grid(row=1,column=4,padx=10)

l=Label(f,text="Height")
l.grid(row=2,column=0,padx=10)

a1=Entry(f,textvariable=t2)
a1.grid(row=2,column=4,padx=10)

l=Label(f,text="Weight")
l.grid(row=3,column=0,padx=10)

a2=Entry(f,textvariable=t3)
a2.grid(row=3,column=4,padx=10)

b=Button(f,text="convert",command=get)
b.grid(row=4,column=5,padx=10)

l=Label(f,text="BMI")
l.grid(row=4,column=0,padx=10)

a3=Entry(f,textvariable=t4)
a3.grid(row=4,column=4,padx=10)


window.mainloop()