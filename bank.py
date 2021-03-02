# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:00:17 2020

@author: admin
"""

class Bank:
    __ano=0
    __cname=''
    __balance=0.0
    def create(self,n,m,p):
        self.__ano=n
        self.__cname=m
        self.__balance=p
    def withdraw(self):
            b=float(input("plz enter amount to be withdraw"))
            if b>self.__balance:
                print("withdraw is not possible")
            else:
                self.__balance=self.__balance-b
                print("balance after withdraw is",self.__balance)
    def deposit(self):
            b=float(input("plz enter amount to be deposited"))
            self.__balance=self.__balance+b
            print("balance after deposit is",self.__balance)
    def display(self):
        print("u r account details")
        print("account number",self.__ano)
        print("account holder name",self.__cname)
        print("Balance amount is",self.__balance)
l=[]
acm=0
while True:
    print("Enter u r choice 1-create 2-depsoit 3-withdarw 4-display")
    x=int(input())
    if x==1:
         y,z=input("enter name and balance").split()
         acm+=1
         b=Bank()
         b.create(acm,y,int(z))
         l.append(b)
         print(" u r account is created")
         print(l)
    elif x==2:
        p=int(input("enter account no"))
        for j in range(len(l)):
            if j+1==p:
                l[j].deposit()
                break
        else:
            print("account number not exists")
            
    elif x==3:
         p=int(input("enter account no"))
         for j in range(len(l)):
             if j+1==p:
                 l[j].withdraw()
                 break
         else:
            print("account number not exists")  
            
    elif x==4:
         p=int(input("enter account no"))
         for j in range(len(l)):
             if j+1==p:
                 l[j].display()
                 break
         else:
            print("account number not exists")
    else:
        print("invalid choice")
        break
