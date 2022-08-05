from tkinter import*
from tkinter import ttk
import mysql.connector as con


def clic(widget):

    print(widget['fg'])

    if widget['fg']=="grey":
        widget['fg']=="black"
        widget.delete(0,END)


def loginwindow():

    def update():
        x1=o2.get()
        print(x1)
        x2=p2.get()
        print(x2)
        x3=q2.get()
        print(x3)
        x4=r2.get()
        print(x4)
        x5=s2.get()
        print(x5)
        x6=w2.get()
        print(x6)
        x7=y2.get()
        print(x7)

        conn=con.connect(host='localhost',user='root',password='',database='chandu')

        if conn.is_connected():
            print('connect')
        else:
            print('error')

        cur=conn.cursor()

        sql="update Facebook set first='"+x2+"',last='"+x3+"',password='"+x5+"',dateofbirth='"+x6+"',gender='"+x7+"'where mobile='"+x4+"'"
        cur.execute(sql)
        cur=conn.commit()

    def delete():
            x1=o2.get()
            print(x1)
            x8=p2.get()
            print(x8)
            x9=q2.get()
            print(x9)
            x10=r2.get()
            print(x10)
            x11=s2.get()
            print(x11)
            x12=w2.get()
            print(x12)
            x13=y2.get()
            print(x13)

            conn=con.connect(host='localhost',user='root',password='',database='chandu')

            if conn.is_connected():
                print('connect')
            else:
                print('error')

            cur=conn.cursor()

            sql="delete from facebook where first='"+x8+"'"
            cur.execute(sql)
            cur=conn.commit()

    mobile=t.get()
    print("mobile=",mobile)
    password=t1.get()
    print("Password=",password)

    conn=con.connect(host='localhost',user='root',password='',database='chandu')

    if conn.is_connected():
        print('connected')
    else:
        print('Not connected')
    
    cur=conn.cursor()
    sql="select * from Facebook where mobile='"+mobile+"' and password='"+password+"'"
    cur.execute(sql)
    res=cur.fetchone()

    


    window=Tk()
    window.title("user details")
    window.geometry('500x500')
    window.resizable(True,True)


    id=res[0]
    first=res[1]
    last=res[2]
    mobile=res[3]
    password=res[4]
    dateofbirth=res[5]
    gender=res[6]

    ff=Frame(window)
    ff.pack()

    z11=StringVar()
    z12=StringVar()
    z13=StringVar()
    z14=StringVar()
    z15=StringVar()
    z16=StringVar()
    z17=StringVar()
   
    o1=Label(ff,text="id",font=('blue',15,'bold'))
    o1.grid(row=0,column=0)
    o2=Entry(ff,textvariable=z11,font=('black',16,'bold'))
    o2.grid(row=0,column=1,pady=15,padx=10)
    o2.insert(0,id)

    p1=Label(ff,text="first name",font=('blue',15,'bold'))
    p1.grid(row=2,column=0)
    p2=Entry(ff,textvariable=z12,font=('black',16,'bold'))
    p2.grid(row=2,column=1,pady=15,padx=10)
    p2.insert(0,first)

    q1=Label(ff,text="last name",font=('blue',15,'bold'))
    q1.grid(row=4,column=0)
    q2=Entry(ff,textvariable=z13,font=('black',16,'bold'))
    q2.grid(row=4,column=1,pady=15,padx=10)
    q2.insert(0,last)

    r1=Label(ff,text="mobile no",font=('blue',15,'bold'))
    r1.grid(row=6,column=0)
    r2=Entry(ff,textvariable=z14,font=('black',16,'bold'))
    r2.grid(row=6,column=1,pady=15,padx=10)
    r2.insert(0,mobile)

    s1=Label(ff,text="password",font=('blue',15,'bold'))
    s1.grid(row=8,column=0)
    s2=Entry(ff,textvariable=z15,font=('black',16,'bold'))
    s2.grid(row=8,column=1,pady=15,padx=10)
    s2.insert(0,password)

    w1=Label(ff,text="date of birth",font=('blue',15,'bold'))
    w1.grid(row=10,column=0)
    w2=Entry(ff,textvariable=z16,font=('black',16,'bold'))
    w2.grid(row=10,column=1,pady=15,padx=10)
    w2.insert(0,dateofbirth)

    y1=Label(ff,text="gender",font=('blue',15,'bold'))
    y1.grid(row=12,column=0)
    y2=Entry(ff,textvariable=z17,font=('black',16,'bold'))
    y2.grid(row=12,column=1,pady=15,padx=10)
    y2.insert(0,gender)

    v=Button(ff,text="update",font="bold",command=update)
    v.grid(row=14,column=1,pady=30,padx=30)

    v1=Button(ff,text="delete",font="bold",command=delete)
    v1.grid(row=14,column=2,pady=30,padx=30)

    

    print(res[0])




    
def accountcreate():


    def datainsert():

        first=t1.get()

        last=t2.get()

        mobile=t3.get()

        password=t4.get()

        date=t5.get()

        month=t6.get()

        year=t7.get()

        val=t8.get()

        gender=""

        if val==1:
            gender="male"
        elif val==2:
            gender="female"
        elif val==3:
            gender="custom"


        dateofbirth=date+"/"+month+"/"+year
        print("dateofbirth=",dateofbirth)

        conn=con.connect(host="localhost",user="root",password="",database="chandu")

        if conn.is_connected():
            print('connect')
        else:
            print('error')

        cur=conn.cursor()

        sql="insert into Facebook(first,last,mobile,password,dateofbirth,gender) values('"+first+"','"+last+"','"+mobile+"','"+password+"','"+dateofbirth+"','"+gender+"')"
        cur.execute(sql)
        conn.commit()

 
    root1.destroy()
    root=Tk()
    root.title("facebook account")
    root.geometry('500x500')
    root.resizable(True,True)

    t1=StringVar()
    t2=StringVar()
    t3=StringVar()
    t4=StringVar()
    t5=StringVar()
    t6=StringVar()
    t7=StringVar()
    t8=IntVar()

    f=Frame()
    f.pack()

    a=Label(f,text="FaceBook",fg="blue",font=('blue',20,'bold'))
    a.grid(row=0,column=30)

    f1=Frame()
    f1.pack()

    b=Label(f,text="Create a new account",fg="black",font=('black',15,'bold'))
    b.grid(row=10,column=30)

    t1=StringVar()
    c=Entry(root,textvariable=t1,fg="grey")
    c.place(x=30,y=65,height=30,width=200)
    c.insert(0,"First Name")
    c.bind("<FocusIn>",lambda x:clic(c))

    t2=StringVar()
    d=Entry(root,textvariable=t2,fg="grey")
    d.place(x=260,y=65,height=30,width=200)
    d.insert(0,"Last Name")
    d.bind("<FocusIn>",lambda x:clic(d))

    t3=StringVar()
    e=Entry(root,textvariable=t3,fg="grey")
    e.place(x=30,y=110,height=40,width=430)
    e.insert(0,"Mobile number or email address")
    e.bind("<FocusIn>",lambda x:clic(e))

    t4=StringVar()
    f=Entry(root,textvariable=t4,fg="grey")
    f.place(x=30,y=160,height=40,width=430)
    f.insert(0,"New password")
    f.bind("<FocusIn>",lambda x:clic(f))

    g=Label(root,text="Date of birth:",fg="black")
    g.place(x=30,y=210)

    t5=StringVar()
    h=ttk.Combobox(root,textvariable=t5,width=10)
    h.place(x=30,y=240)
    l=[]
    for i in range (1,31):
        l.append(i)
    h['values']=l
    t5.set('Date')
    h.current()

    t6=StringVar()
    i=ttk.Combobox(root,textvariable=t6,width=10)
    i.place(x=190,y=240)
    i['values']=['jan','feb','mar','apr','may','jun','jul','aug','spt','oct','nov','dec']
    t6.set('Month')
    i.current()

    t7=StringVar()
    j=ttk.Combobox(root,textvariable=t7,width=10)
    j.place(x=340,y=240)
    j['values']=[2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2000]
    t7.set('Year')
    j.current()

    g=Label(root,text="Gender:",fg="black")
    g.place(x=30,y=270)

    t8=IntVar()
    k=Radiobutton(root,text="MALE",variable=t8,value=1)
    k.place(x=30,y=300)

    k=Radiobutton(root,text="FEMALE",variable=t8,value=2)
    k.place(x=190,y=300)

    k=Radiobutton(root,text="CUSTOM",variable=t8,value=3)
    k.place(x=340,y=300)

    l=Button(root,text="SUBMIT",font="bold",fg="blue",command=datainsert)
    l.place(x=190,y=370)



root1=Tk()
root1.title("login")
root1.geometry("500x500")


f=Frame(root1)
f.pack()

a1=Label(f,text="FaceBook",fg="blue",font=('blue',20,'bold'))
a1.grid(row=0,column=30)

n1=Label(f,text="Create a new account",fg="black",font=('black',15,'bold'))
n1.grid(row=10,column=30)

t=StringVar()
e1=Entry(root1,textvariable=t,fg="grey")
e1.place(x=30,y=110,height=40,width=430)
e1.insert(0,"Mobile number or email address")
e1.bind("<FocusIn>",lambda x:clic(e1))

t1=StringVar()
c1=Entry(root1,textvariable=t1,fg="grey")
c1.place(x=30,y=170,height=40,width=430)
c1.insert(0,"password")
c1.bind("<FocusIn>",lambda x:clic(c1))


l1=Button(root1,text="LOGIN",font="bold",fg="blue",command=loginwindow)
l1.place(x=190,y=250)

l1=Button(root1,text="CREATE ACCOUNT",font="bold",fg="blue",command=accountcreate)
l1.place(x=150,y=290)

mainloop()


