from tkinter import*

def get():
    v=t1.get()
    v1=int(v,2)
    print("decimal no",v1)

    t2.set(v1)
    b3.update()


window=Tk()
window.title("binory to decimal")
window.geometry('500x500')
window.resizable(False,False)

t1=StringVar()
t2=StringVar()

f=Frame()
f.grid()
l=Label(f,text="binory")
l.grid(row=1,column=0)


b=Label(f,text="decimal")
b.grid(row=2,column=0,padx=10)

b1=Entry(f,textvariable=t1)
b1.grid(row=1,column=4,padx=10)

b2=Button(f,text="convert",command=get)
b2.grid(row=1,column=5,padx=10)

b3=Entry(f,textvariable=t2)
b3.grid(row=2,column=4,padx=10)

window.mainloop()