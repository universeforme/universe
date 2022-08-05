from tkinter import*
import tkinter.messagebox

window=Tk()
window.title('tic-tak-toe')
window.resizable(False,False)
window.geometry('600x600')


click=True
count=0

btn1=StringVar()
btn2=StringVar()
btn3=StringVar()
btn4=StringVar()
btn5=StringVar()
btn6=StringVar()
btn7=StringVar()
btn8=StringVar()
btn9=StringVar()



def press(num):
    global click,count

    if click==True:

        if num==1:
            btn1.set('x')
            btn1.state[DISABLED]
        if num==2:
            btn2.set('x')
            #btn2.state[DISABLED]
        if num==3:
            btn3.set('x')
            #btn3.state[DISABLED]
        if num==4:
            btn4.set('x')
            #btn4.state[DISABLED]
        if num==5:
            btn5.set('x')
            #btn5.state[DISABLED]
        if num==6:
            btn6.set('x')
            #btn6.state[DISABLED]
        if num==7:
            btn7.set('x')
            #btn7.state[DISABLED]
        if num==8:
            btn8.set('x')
            #3btn8.state[DISABLED]
        if num==9:
            btn9.set('x')
            #btn9.state[DISABLED]
        count+=1
        click=False
        checkwin()

    else:

        if num==1:
            btn1.set('0')
            btn1.state[DISABLED]
        if num==2:
            btn2.set('0')
            #btn2.state[DISABLED]
        if num==3:
            btn3.set('0')
            #btn3.state[DISABLED]
        if num==4:
            btn4.set('0')
            #btn4.state[DISABLED]
        if num==5:
            btn5.set('0')
            #btn5.state[DISABLED]
        if num==6:
            btn6.set('0')
            #btn6.state[DISABLED]
        if num==7:
            btn7.set('0')
            #btn7.state[DISABLED]
        if num==8:
            btn8.set('0')
            #btn8.state[DISABLED]
        if num==9:
            btn9.set('0')
            #btn9.state[DISABLED]
        count+=1
        click=True
        checkwin()


Button1=Button(window,textvariable=btn1,height=5,width=10,command=lambda:press(1))
Button1.grid(row=0,column=0)

Button2=Button(window,textvariable=btn2,height=5,width=10,command=lambda:press(2))
Button2.grid(row=0,column=1)

Button3=Button(window,textvariable=btn3,height=5,width=10,command=lambda:press(3))
Button3.grid(row=0,column=2)

Button4=Button(window,textvariable=btn4,height=5,width=10,command=lambda:press(4))
Button4.grid(row=1,column=0)

Button5=Button(window,textvariable=btn5,height=5,width=10,command=lambda:press(5))
Button5.grid(row=1,column=1)

Button6=Button(window,textvariable=btn6,height=5,width=10,command=lambda:press(6))
Button6.grid(row=1,column=2)

Button7=Button(window,textvariable=btn7,height=5,width=10,command=lambda:press(7))
Button7.grid(row=2,column=0)

Button8=Button(window,textvariable=btn8,height=5,width=10,command=lambda:press(8))
Button8.grid(row=2,column=1)

Button9=Button(window,textvariable=btn9,height=5,width=10,command=lambda:press(9))
Button9.grid(row=2,column=2)

def checkwin():
    global click,count

    if( btn1.get()=='x' and btn2.get()=='x' and btn3.get()=='x' or
        btn4.get()=='x' and btn5.get()=='x' and btn6.get()=='x' or
        btn7.get()=='x' and btn8.get()=='x' and btn9.get()=='x' or
        btn1.get()=='x' and btn4.get()=='x' and btn7.get()=='x' or
        btn2.get()=='x' and btn5.get()=='x' and btn8.get()=='x' or
        btn3.get()=='x' and btn6.get()=='x' and btn9.get()=='x' or
        btn1.get()=='x' and btn5.get()=='x' and btn9.get()=='x' or
        btn3.get()=='x' and btn5.get()=='x' and btn7.get()=='x' ):
        tkinter.messagebox.showinfo('tic.tac.toe','x wins')
        click=True
        count=0
        clear()
    
        
    elif( btn1.get()=='0' and btn2.get()=='0' and btn3.get()=='0' or
          btn4.get()=='0' and btn5.get()=='0' and btn6.get()=='0' or
          btn7.get()=='0' and btn8.get()=='0' and btn9.get()=='0' or
          btn1.get()=='0' and btn4.get()=='0' and btn7.get()=='0' or
          btn2.get()=='0' and btn5.get()=='0' and btn8.get()=='0' or
          btn3.get()=='0' and btn6.get()=='0' and btn9.get()=='0' or
          btn1.get()=='0' and btn5.get()=='0' and btn9.get()=='0' or
          btn3.get()=='0' and btn5.get()=='0' and btn7.get()=='0' ):
          tkinter.messagebox.showinfo('tic.tac.toe','0 wins')
          click=True
          count=0
          clear()
        

    elif(count==9):
        tkinter.messagebox.showinfo('tic.tac.toe','tie')
        click=True
        count=0
        clear()
        
        
def clear():
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")


window.mainloop()

