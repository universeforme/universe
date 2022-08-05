# from tkinter import*

# def submit():

#     try:
#         temp=int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
#     except:
#         print('enter valid value')


# root=Tk()
# root.geometry("300x250")
# root.title("Time Counter")
  
# hour=StringVar()
# minute=StringVar()
# second=StringVar()

# hour.set('00')
# minute.set('00')
# second.set('00')
  
# hourEntry= Entry(root,textvariable=hour,width=3,font=("Arial",18,""))
# hourEntry.place(x=80,y=20)
  
# minuteEntry= Entry(root,textvariable=minute,width=3,font=("Arial",18,""))
# minuteEntry.place(x=130,y=20)
  
# secondEntry= Entry(root,textvariable=second,width=3,font=("Arial",18,""))
# secondEntry.place(x=180,y=20)

# btn = Button(root, text='START', bd='5',command=submit)
# btn.place(x = 110,y = 100)


  



# root.mainloop()

from tkinter import *

ws = Tk()
ws.geometry('400x400')
ws.title('PythonGuides: Stopwatch')
ws.config(bg='green')
ws.iconbitmap('stopwatch.ico')


counter = -1
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:             
                display="00"
            else:
                display=str(counter)

            lbl['text']=display    
            
            lbl.after(1000, count)    
            counter += 1
    count()     

def StartTimer(lbl):
    global running
    running=True
    counter_label(lbl)
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():
    global running
    start_btn['state']='normal'
    stop_btn['state']='disabled'
    reset_btn['state']='normal'
    running = False

def ResetTimer(lbl):
    global counter
    counter=-1
    if running==False:      
        reset_btn['state']='disabled'
        lbl['text']='00'
    else:                          
        lbl['text']=''

# # bg = PhotoImage(file='stopwatch.png')
# img = Label(ws, image=bg, bg='#299617')
# img.place(x=75, y=50)

lbl = Label(ws,text="00",fg="black",bg='green',font="Verdana 40 bold")
lbl.place(x=160, y=150) 

label_msg = Label(ws, text="minutes",fg="black",bg='green',font="Verdana 10 bold") 
label_msg.place(x=170, y=230)

start_btn=Button(ws,text='Start',width=8,command=lambda:StartTimer(lbl))
start_btn.place(x=10, y=350)

stop_btn = Button(ws,text='Stop',width=8,state='disabled',command=StopTimer)
stop_btn.place(x=150, y=350)

reset_btn = Button(ws,text='Reset', width=8,command=lambda:ResetTimer(lbl))
reset_btn.place(x=280, y=350)


ws.mainloop()