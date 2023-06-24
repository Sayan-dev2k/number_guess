from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.geometry("1400x1000")
root.title("Number guessing")
root.config(bg='#FBCEB1')
title=Label(root,text='NUMBER GUESSING GAME',font=('times new roman',50,'bold'),bg='blue',fg='white',bd=5,relief='solid').place(x=0,y=20,relwidth=1)
lbl1=Label(root,text='CHOOSE A NUMBER',font=('times new roman',25,'bold'),bg='red',fg='white')
lbl1.pack(pady=150)
score=30
attempt=1
l=[1,2,3,4,5,6,7,8,9,10]
a=random.choice(l)
b=0
def pfun():
    pass
def func():
    global score
    global attempt
    if(b>a):
        messagebox.showerror("Error","Lower number please!!!")
        score=score-5
        attempt=attempt+1
        
    elif(b<a):
    
        messagebox.showerror("Error","Upper number please!!")
        score=score-5
        attempt=attempt+1
    else:
        messagebox.showinfo("Info","You have guessed correctly")
        at=Label(root,text='Attempt',font=('times new roman',25,'bold'),bg='yellow')
        at.place(x=500,y=300)
        atm=Label(root,text=attempt,font=('times new roman',25,'bold'),bg='yellow')
        atm.place(x=800,y=300)
        if(attempt!=1):    
            ded=Label(root,text="5 points deducted for each wrong attempt",font=('times new roman',25,'bold'),bg='yellow')
            ded.place(x=900,y=300)
        if(attempt<6):
            lbl=Label(root,text="Your Score",font=('times new roman',25,'bold'),bg='#90EE90')
            lbl.place(x=500,y=400)
            maxscore=Label(root,text="Maximum score: 30",font=('times new roman',25,'bold'),bg='#90EE90')
            maxscore.place(x=900,y=400)
            sc=Label(root,text=score,font=('times new roman',25,'bold'),bg='#90EE90')
            sc.place(x=800,y=400)
        else:
            lbl=Label(root,text="score cannot be displayed",font=('times new roman',25,'bold'),bg='#90EE90')
            lbl.place(x=500,y=400)
        b1.config(command=pfun)
        b2.config(command=pfun)
        b3.config(command=pfun)
        b4.config(command=pfun)
        b5.config(command=pfun)
        b6.config(command=pfun)
        b7.config(command=pfun)
        b8.config(command=pfun)
        b9.config(command=pfun)
        b10.config(command=pfun)
        btn=Button(root,text='Exit',font=('times new roman',20),command=root.destroy)
        btn.pack(pady=150)

def fun1():
    global b
    b=1
    func()
def fun2():
    global b
    b=2
    func()
def fun3():
    global b
    b=3
    func()
def fun4():
    global b
    b=4
    func()
def fun5():
    global b
    b=5
    func()
def fun6():
    global b
    b=6
    func()
def fun7():
    global b
    b=7
    func()
def fun8():
    global b
    b=8
    func()
def fun9():
    global b
    b=9
    func()
def fun10():
    global b
    b=10
    func()
b1=Button(root,text='1',font=('times new roman',25,'bold'),command=fun1)
b1.place(x=450,y=200)
b2=Button(root,text='2',font=('times new roman',25,'bold'),command=fun2)
b2.place(x=500,y=200)
b3=Button(root,text='3',font=('times new roman',25,'bold'),command=fun3)
b3.place(x=550,y=200)
b4=Button(root,text='4',font=('times new roman',25,'bold'),command=fun4)
b4.place(x=600,y=200)
b5=Button(root,text='5',font=('times new roman',25,'bold'),command=fun5)
b5.place(x=650,y=200)
b6=Button(root,text='6',font=('times new roman',25,'bold'),command=fun6)
b6.place(x=700,y=200)
b7=Button(root,text='7',font=('times new roman',25,'bold'),command=fun7)
b7.place(x=750,y=200)
b8=Button(root,text='8',font=('times new roman',25,'bold'),command=fun8)
b8.place(x=800,y=200)
b9=Button(root,text='9',font=('times new roman',25,'bold'),command=fun9)
b9.place(x=850,y=200)
b10=Button(root,text='10',font=('times new roman',25,'bold'),command=fun10)
b10.place(x=900,y=200)


    
# score=score-5
# attempt=attempt+1


# if(attempt==1):
#     print("Your score:",score)
# elif(attempt==2):
#     print("Your score:",score)
# elif(attempt==3):
#     print("Your score:",score)
# elif(attempt==4):
#     print("Your score:",score)
# elif(attempt==5):
#     print("Your score:",score)
# else:
#     print("score cannot be displayed")
root.mainloop()