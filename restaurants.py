from tkinter import*
from tkinter import ttk

# def clic():

    
#     no1=v2.get()
#     no2=v3.get()
#     no3=v4.get()
#     no4=v5.get()
#     no5=v6.get()

#     v1.set(no)/
#     v2.set(no1)
#     v3.set(no2)
#     v4.set(no3)
#     v5.set(no4)
#     v6.set(no5)

#     p1.update
#     p2.update
#     p3.update
#     p4.update
#     p5.update
#     p6.update
 

def onclick():

    sum=0
    
    val=t1.get()
    no=v1.get()
    if val==1:
        vv=int(no)*100
        sum=sum+vv
        v.set(sum)
        p1.update()

    # val=t1.get()
    # no=v1.get()
    # if val==1:
    #     v.set(no)
    #     p1.update()

    val1=t2.get()
    no1=v2.get()
    if val1==1:
        vv1=int(no1)*120
        sum=sum+vv1
        v.set(sum)
        p2.update()

    val2=t3.get()
    no2=v3.get()
    if val2==1:
        vv2=int(no2)*130
        sum=sum+vv2
        v.set(sum)
        p3.update()

    val3=t4.get()
    no3=v4.get()
    if val3==1:
        vv3=int(no3)*145
        sum=sum+vv3
        v.set(sum)
        p4.update()

    val4=t5.get()
    no4=v5.get()
    if val4==1:
        vv4=int(no4)*130
        sum=sum+vv4
        v.set(sum)
        p5.update()

    val5=t6.get()
    no5=v6.get()
    if val5==1:
        vv5=int(no5)*120
        sum=sum+vv5
        v.set(sum)
        p6.update()
        
    # val1=t2.get()
    # val2=t3.get()
    # val3=t4.get()
    # val4=t5.get()
    # val5=t6.get()

    # c1=100*val
    # c2=120*val1
    # c3=130*val2
    # c4=145*val3
    # c5=130*val4
    # c6=120*val5

    # sum=vv+vv1+vv2+vv3+vv4+vv5

    # v.set(sum)
    # o.update




root=Tk()
root.title("PINKY EGG")
root.geometry('600x600')
root.config(bg="black")

t1=IntVar()
t2=IntVar()
t3=IntVar()
t4=IntVar()
t5=IntVar()
t6=IntVar()

f=Frame()
f.pack()

a=Label(f,text="MENU",bg="black",fg="white")
a.grid(row=0,column=50)

b=Label(root,text="EGG CURRY    :",bg="black",fg="cyan")
b.place(x=3,y=50)

c=Label(root,text="100",bg="black",fg="orange")
c.place(x=350,y=50)

d=Label(root,text="BOILED TIKKA  :",bg="black",fg="cyan")
d.place(x=3,y=80)

e=Label(root,text="120",bg="black",fg="orange")
e.place(x=350,y=80)

f=Label(root,text="CHEESE GOTI   :",bg="black",fg="cyan")
f.place(x=3,y=110)

g=Label(root,text="130",bg="black",fg="orange")
g.place(x=350,y=110)

h=Label(root,text="DOUBLE SUNDAY :",bg="black",fg="cyan")
h.place(x=3,y=140)

i=Label(root,text="145",bg="black",fg="orange")
i.place(x=350,y=140)

j=Label(root,text="WORLD CUP    :",bg="black",fg="cyan")
j.place(x=3,y=170)

k=Label(root,text="130",bg="black",fg="orange")
k.place(x=350,y=170)

l=Label(root,text="EGG LAZIZ    :",bg="black",fg="cyan")
l.place(x=3,y=200)

m=Label(root,text="120",bg="black",fg="orange")
m.place(x=350,y=200)

b1=Checkbutton(root,variable=t1,bg="black")
b1.place(x=450,y=50)

d1=Checkbutton(root,variable=t2,bg="black")
d1.place(x=450,y=80)

f1=Checkbutton(root,variable=t3,bg="black")
f1.place(x=450,y=110)

h1=Checkbutton(root,variable=t4,bg="black")
h1.place(x=450,y=140)

j1=Checkbutton(root,variable=t5,bg="black")
j1.place(x=450,y=170)

l1=Checkbutton(root,variable=t6,bg="black")
l1.place(x=450,y=200)

n=Button(root,text="total =",bg="black",command=onclick)
n.place(x=3,y=250)

v=StringVar()

o=Entry(root,textvariable=v,bg="black",fg="white")
o.place(x=100,y=250)

v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()

p1=ttk.Combobox(root,textvariable=v1,width=5)
p1.place(x=500,y=50)
p1['values']=('1','2','3')
v1.set('egg')
p1.current()


p2=ttk.Combobox(root,textvariable=v2,width=5)
p2.place(x=500,y=80)
p2['values']=('1','2','3')
v2.set('egg')
p2.current()

p3=ttk.Combobox(root,textvariable=v3,width=5)
p3.place(x=500,y=110)
p3['values']=('1','2','3')
v3.set('egg')
p3.current()

p4=ttk.Combobox(root,textvariable=v4,width=5)
p4.place(x=500,y=140)
p4['values']=('1','2','3')
v4.set('egg')
p4.current()

p5=ttk.Combobox(root,textvariable=v5,width=5)
p5.place(x=500,y=170)
p5['values']=('1','2','3')
v5.set('egg')
p5.current()

p6=ttk.Combobox(root,textvariable=v6,width=5)
p6.place(x=500,y=200)
p6['values']=('1','2','3')
v6.set('egg')
p6.current()




root.mainloop()