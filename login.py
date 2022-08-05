from tkinter import*
import mysql.connector as con

def clic(widget):

    print(widget['fg'])

    if widget['fg']=="grey":
        widget['fg']=="black"
        widget.delete(0,END)



def get():
    root.destroy()
    cat()

    email=t.get()
    print("email",email)

    Password=t1.get()
    print("password",Password)

    conn=con.connect(host="localhost",user="root",password="",database="chandu")

    if conn.is_connected():
        print('connect')
    else:
        print('error')

    cur=conn.cursor()

    sql="select * from login where email='"+email+"' and password='"+Password+"'"

    # sql="insert into Facebook(first,last,mobile,password,dateofbirth,gender) values('"+first+"','"+last+"','"+mobile+"','"+password+"','"+dateofbirth+"','"+gender+"')"
    cur.execute(sql)
    res=cur.fetchall()
    print(res)
    conn.commit()

    for i in res:
        print(i)


root=Tk()
root.title("login")
root.geometry("500x500")

t=StringVar()
t1=StringVar()

def get1():

    f=Frame(root)
    f.pack()

    a=Label(f,text="FaceBook",fg="blue",font=('blue',20,'bold'))
    a.grid(row=0,column=30)

    n=Label(f,text="Create a new account",fg="black",font=('black',15,'bold'))
    n.grid(row=10,column=30)

    
    e=Entry(root,textvariable=t,fg="grey")
    e.place(x=30,y=110,height=40,width=430)
    e.insert(0,"Mobile number or email address")
    e.bind("<FocusIn>",lambda x:clic(e))

   
    c=Entry(root,textvariable=t1,fg="grey")
    c.place(x=30,y=170,height=40,width=430)
    c.insert(0,"password")
    c.bind("<FocusIn>",lambda x:clic(c))


    l=Button(root,text="LOGIN",font="bold",fg="blue",command=get)
    l.place(x=190,y=250)



    mainloop()

def cat():
    root1=Tk()
    root.title("login")
    root1.geometry("500x500")

    mainloop()

get1()

