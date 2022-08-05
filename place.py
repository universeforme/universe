from tkinter import*

def press(number):
    a.insert(END,number)

def equal():
    try:
        y = str(eval(a.get()))
        a.delete(0, END)
        a.insert(0, y)
    except:
        a.messagebox.showinfo("Error", "Syntax Error")

def clear():
    a.delete(0, END)
 


window=Tk()
window.title('calculater')
window.geometry('325x400')

t=StringVar()
ff=Frame(window)
ff.place()
a=Entry(ff,textvariable=t,)
a.place(padx=30,pady=30)

f2=Frame(window)
f2.pack()
b2=Button(f2,text='7',height=3,width=7,relief=RAISED,command=lambda:press(7))
b2.pack(side=LEFT)
b2=Button(f2,text='8',height=3,width=7,relief=RAISED,command=lambda:press(8))
b2.pack(side=LEFT)

b2=Button(f2,text='9',height=3,width=7,relief=RAISED,command=lambda:press(9))
b2.pack(side=LEFT)

b2=Button(f2,text='*',height=3,width=7,relief=RAISED,command=lambda:press('*'))
b2.pack(side=LEFT)


f3=Frame(window)
f3.pack()
b3=Button(f3,text='4',height=3,width=7,relief=RAISED,command=lambda:press('4'))
b3.pack(side=LEFT)

b3=Button(f3,text='5',height=3,width=7,relief=RAISED,command=lambda:press('5'))
b3.pack(side=LEFT)

b3=Button(f3,text='6',height=3,width=7,relief=RAISED,command=lambda:press('6'))
b3.pack(side=LEFT)

b3=Button(f3,text='-',height=3,width=7,relief=RAISED,command=lambda:press('-'))
b3.pack(side=LEFT)


f4=Frame(window)
f4.pack()
b4=Button(f4,text='1',height=3,width=7,relief=RAISED,command=lambda:press('1'))
b4.pack(side=LEFT)

b4=Button(f4,text='2',height=3,width=7,relief=RAISED,command=lambda:press('2'))
b4.pack(side=LEFT)

b4=Button(f4,text='3',height=3,width=7,relief=RAISED,command=lambda:press('3'))
b4.pack(side=LEFT)

b4=Button(f4,text='+',height=3,width=7,relief=RAISED,command=lambda:press('+'))
b4.pack(side=LEFT)


f5=Frame(window)
f5.pack()
b5=Button(f5,text='//',height=3,width=7,relief=RAISED,command=lambda:press('//'))
b5.pack(side=LEFT)

b5=Button(f5,text='0',height=3,width=7,relief=RAISED,command=lambda:press('0'))
b5.pack(side=LEFT)

b5=Button(f5,text='clear',height=3,width=7,relief=RAISED,command=clear)
b5.pack(side=LEFT)

b5=Button(f5,text='=',height=3,width=7,relief=RAISED,command=equal)
b5.pack(side=LEFT)

f6=Frame(window)
f6.pack()
b6=Button(f6,text='+/-',height=3,width=7,relief=RAISED,command=lambda:press('+/-'))
b6.pack(side=LEFT)

b6=Button(f6,text='%',height=3,width=7,relief=RAISED,command=lambda:press('%'))
b6.pack(side=LEFT)

b6=Button(f6,text='.',height=3,width=7,relief=RAISED,command=lambda:press('.'))
b6.pack(side=LEFT)

b6=Button(f6,text='00',height=3,width=7,relief=RAISED,command=lambda:press('00'))
b6.pack(side=LEFT)


window.mainloop()

