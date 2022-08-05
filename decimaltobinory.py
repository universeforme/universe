from tkinter import*

def get():
    v=t1.get()
    print("decimal no",v)

    num=int(v)
    b=bin(num)
    print("binory",b[2:])

    t2.set(b[2:])
    b3.update()


window=Tk()

window.title("repid table")
window.geometry("500x500")
window.resizable(True,True)

f=Frame()
f.grid()
l=Label(f,text="decimal")
l.grid(row=1,column=0)

t1=StringVar()
t2=StringVar()

b=Label(f,text="binary")
b.grid(row=2,column=0,padx=10)

b1=Entry(f,textvariable=t1)
b1.grid(row=1,column=4,padx=10)

b2=Button(f,text="convert",command=get) 
b2.grid(row=1,column=5,padx=10)

b3=Entry(f,textvariable=t2)
b3.grid(row=2,column=4,padx=10)

window.mainloop()