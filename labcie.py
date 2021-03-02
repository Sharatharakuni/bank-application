# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:49:42 2020

@author: admin
"""

import tkinter as k
from tkinter import *
import datetime
import sqlite3
import random

con=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
"""con.execute('''CREATE TABLE t
(ano INT PRIMARY KEY NOT NULL,
name CHAR(20) NOT NULL,
age INT NOT NULL,
gender CHAR(10) NOT NULL,
balance INT);''')

con.execute('''CREATE TABLE be
(ano1 INT NOT NULL,
tran CHAR(20) NOT NULL,
amt INT NOT NULL,
blance INT NOT NULL,
datetime CHAR(20) NOT NULL);''')
print('table created')"""

#con.execute("insert into t (ano,name,age,gender,balance) values(1649,'sharat',21,'male',0)")


def create(c):
   
    c.tkraise()
    global e1,gen,e2,an,s
    s=k.StringVar()
    gen=k.IntVar()
    l=k.Label(c,text="CREATE YOUR ACCOUNT",font=('Courier',20,'bold')).place(x=80,y=25)
    l1=k.Label(c,text="ENTER YOUR NAME").place(x=150,y=100)
    e1=k.Entry(c,width=20)
    e1.place(x=350,y=100)
    l2=k.Label(c,text="ENTER YOUR AGE").place(x=150,y=150)
    e2=k.Entry(c,width=10)
    e2.place(x=350,y=150)
    l2=k.Label(c,text="SELECT YOUR GENDER").place(x=150,y=200)
    r1=k.Radiobutton(c,text='MALE',variable=gen,value=1)
    r1.place(x=150,y=250)
    r2=k.Radiobutton(c,text='FEMALE',variable=gen,value=2)
    r2.place(x=150,y=300)
    b=k.Button(c,text="CREATE ACCOUNT",width=20,command=lambda:createdisplay()).place(x=200,y=350)
    b1=k.Button(c,text="BACK TO MAIN PAGE",width=20,command=lambda:display(f)).place(x=200,y=400)
def createdisplay():
    bal=0
    if e1.get()=='null':
        l4=k.Label(c,text='FIRST ENTER THE ABOVE DETAILS')
        l4.place(x=50,y=450)
    else:
        s=e1.get()
        
        an=random.randint(1000,10000)
        
        if s=='' and e2.get()=='':
            l1=k.Label(c,text='FILL THE ABOVE DETAILS FIRST',background='blue',foreground='red',font=(10)).place(x=50,y=450)
        else:
            a='YOUR ACCOUNT IS CREATED '+s+'\n YOUR ACCOUNT NUMBER IS '+str(an)
            l=k.Label(c,text=a,background='blue',foreground='black',font=(5))
            l.place(x=50,y=450)
            if gen.get()==1:
                g='male'
            elif gen.get()==2:
                g='female'
            con.execute("insert into t (ano,name,age,gender,balance) values(?,?,?,?,?)",(an,s,e2.get(),g,bal))
            con.commit()
            con.close()
def deposit(c1):
    
    global e3,e4
    c1.tkraise()
    l1=k.Label(c1,text="ENTER YOUR ACCOUNT NUMBER").place(x=100,y=100)
    con2=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    res=con2.execute("select * from t")
    l=[]
    for i in res:
        l.append(i[0])
    e3=k.Spinbox(c1,values=(l),width=20)
    e3.place(x=300,y=100)
    l2=k.Label(c1,text="ENTER AMOUNT TO BE DEPOSITED").place(x=100,y=150)
    e4=k.Entry(c1,width=20)
    e4.place(x=300,y=150)
    b=k.Button(c1,text="DEPOSIT",width=20,command=lambda:depositprint()).place(x=150,y=200)
    b1=k.Button(c1,text="BACK TO MAIN PAGE",width=20,command=lambda:display(f)).place(x=150,y=300)
def depositprint():
    a=int(e3.get())
    a4=int(e4.get())
    l1=[]
    con2=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    r=con2.execute("SELECT * FROM t")
    for i in r:
        l1.append(i[0])
    r1=con2.execute("select * from t where ano=?",(a,))
    for i in r1:
        b=i[4]
    n=datetime.datetime.now()
    ds=n.strftime("%d-%m-%Y %H:%M:%S") 
    c='credit'
    if a in l1:
        b=b+a4
        con2.execute("update t set balance=? where ano=?",(b,a))
        con2.execute("INSERT INTO be (ano1,tran,amt,blance,datetime) VALUES(?,?,?,?,?)",(a,c,a4,b,ds))
    con2.commit()
    con2.close()
    l=k.Label(c1,text='AMONT '+e4.get()+' IS DEPOSITED IN YOUR ACCOUNT',background='blue',foreground='black',font=(7)).place(x=50,y=450)
    
def withdrawl(c2):
    c2.tkraise()
    global e5,e6
    l1=k.Label(c2,text="ENTER YOUR ACCOUNT NUMBER").place(x=100,y=100)
    con3=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    res1=con3.execute("select * from t")
    a=[]
    for i in res1:
        a.append(i[0])
    e5=k.Spinbox(c2,values=(a),width=20)
    e5.place(x=300,y=100)
    l2=k.Label(c2,text="ENTER AMOUNT TO BE WITHDRAWN").place(x=100,y=150)
    e6=k.Entry(c2,width=20)
    e6.place(x=350,y=150)
    b=k.Button(c2,text="WITHDRAW",width=20,command=lambda:withdrawlprint()).place(x=150,y=200)
    b1=k.Button(c2,text="BACK TO MAIN PAGE",width=20,command=lambda:display(f)).place(x=150,y=300)
def withdrawlprint():
    a5=int(e5.get())
    a6=int(e6.get())
    l2=[]
    global l5,l6
    con3=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    r1=con3.execute("SELECT * FROM t")
    for i in r1:
        l2.append(i[0])                                                                 
    r2=con3.execute("select * from t where ano=?",(a5,))
    for i in r2:
        nb=i[4]
    n=datetime.datetime.now()
    ds=n.strftime("%d-%m-%Y %H:%M:%S") 
    d='debit'
    if a5 in l2:
        if nb>=a6:
            nb=nb-a6
            con3.execute("update t set balance=? where ano=?",(nb,a5))
            con3.execute("insert into be (ano1,tran,amt,blance,datetime) values(?,?,?,?,?)",(a5,d,a6,nb,ds))
            l5=k.Label(c2,text='amount '+e6.get()+' is withdrawn from your account ',font=(7),bg='blue',fg='black').place(x=50,y=350)
        else:
            l6=k.Label(c2,text="INSUFFICIENT BALANCE ",font=(5),bg='blue',fg='black').place(x=50,y=400)
    con3.commit()
    con3.close()
def balance(c3):
    c3.tkraise()    
    global e7,t1
    con4=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    res3=con4.execute('select * from t')
    a1=[]
    for i in res3:
        a1.append(i[0])
    l1=k.Label(c3,text="ENTER YOUR ACCOUNT NUMBER").place(x=100,y=100)
    e7=k.Spinbox(c3,values=(a1),width=20)
    e7.place(x=300,y=100)
    
    l2=k.Label(c3,text="YOUR ACCOUNT DETAILS ARE")    
    l2.place(x=100,y=150)
    t1=k.Text(c3,width=50,height=10,wrap=WORD)
    t1.place(x=50,y=180)
    b2=k.Button(c3,text='GET INFORMATION',width=20,command=lambda:balanceprint()).place(x=150,y=400)
    b1=k.Button(c3,text="BACK TO MAIN PAGE",width=20,command=lambda:display(f)).place(x=150,y=450)    
def balanceprint():
    con4=sqlite3.connect('C:\Program Files (x86)\sqlite3\s1')
    a7=int(e7.get())
    
    r3=con4.execute("select * from t where ano=?",(a7,))
    r4=con4.execute("select * from be where ano1=?",(a7,))
    t1.insert(END,'A no. name age sex  balance\n')
    for i in r3:
       t1.insert(END,i)
       t1.insert(END,'\n')
    t1.insert(END,'\nMINI STATEMENT\n\n') 
    t1.insert(END,'       amt    balnc   date and time\n')
    for i in r4:
        stn=i[1]+' '+str(i[2])+'   '+str(i[3])+'    '+str(i[4])
        t1.insert(END,stn)
        t1.insert(END,'\n')
    con4.close()
def display(f):
    f.tkraise()
      
r=k.Tk()
r.geometry('500x500')
f=k.Frame(r,bg='blue',height=500,width=500)
f.place(x=0,y=0)
c=k.Frame(r,bg='blue',height=500,width=500)
c.place(x=0,y=0)
L=k.Label(f,text="BANK SYSTEM",font=('Pristina',40,'bold'),foreground='black',bg='red').place(x=80,y=50)
b4=k.Button(f,text='CREATE ACCOUNT',command=lambda:create(c)).place(x=100,y=200)
c1=k.Frame(r,bg='blue',height=500,width=500)
c1.place(x=0,y=0)
c2=k.Frame(r,bg='blue',height=500,width=500)
c2.place(x=0,y=0)
c3=k.Frame(r,bg='blue',height=500,width=500)
c3.place(x=0,y=0)
b1=k.Button(f,text='DEPOSIT',command=lambda:deposit(c1)).place(x=100,y=250)
b2=k.Button(f,text='WITHDRAWL',command=lambda:withdrawl(c2)).place(x=100,y=300)
b3=k.Button(f,text='BALANCE ENQUIRY',command=lambda:balance(c3)).place(x=100,y=350)
display(f)
r.mainloop()