### page 3 add to cart page
###anchor=tk.CENTER
#sam button

def sb():
    messagebox.showinfo("Message", "SAMSUNG S20 ADDED TO CART")

#iqoo button

def ib():
    messagebox.showinfo("Message", "IQOO Z7 ADDED TO CART")

#poco button
def ob():
    messagebox.showinfo("Message", "POCO M2 ADDED TO CART")

#redmi
def rb():
    messagebox.showinfo("Message", "REDMI C20 ADDED TO CART")

#techno
def tb():
    messagebox.showinfo("Message", "TECHNO C7A ADDED TO CART")

#realmi
def eb():
    messagebox.showinfo("Message", "REALMI M30 PRO ADDED TO CART")    

    
from tkinter import*
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("ONLINE SHOPPING NAME")

##
###title
def mobile():
    name=Label(a,text="---ONLINE SHOP NAME---",bg="black",font=("Brush Script MT",30,'bold')
       ,fg="white",width=200)
    name.pack()

#frame
    f1 = Frame(a, bg="white", width=1000, height=600)  
    f1.pack()
###samsung

    s=Label(f1,text="SUMSUNG S20 ULTRA ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=40,y=20)
    s1=Label(f1,text="16GB RAM 256GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    s1.place(x=40,y=45)
    s2=Label(f1,text="PRICE : 56000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=40,y=65)
    s3=Label(f1,text="⭐⭐⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    s3.place(x=40,y=90)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sb)
    btns.place(x=250,y=65)

#iqoo

    i=Label(f1,text="IQOO Z7 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=40,y=180)
    i1=Label(f1,text="6GB RAM 128GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=205)
    i2=Label(f1,text="PRICE : 20000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=40,y=230)
    i3=Label(f1,text="⭐⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    i3.place(x=40,y=255)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ib)
    btni.place(x=250,y=230)

#poco
    o=Label(f1,text="POCO M2  ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=40,y=345)
    o1=Label(f1,text="4GB RAM 64GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    o1.place(x=40,y=370)
    o2=Label(f1,text="PRICE : 12000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=40,y=395)
    o3=Label(f1,text="⭐⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    o3.place(x=40,y=420)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ob)
    btno.place(x=250,y=395)

#redmi
    r=Label(f1,text="REDMI C20 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    r.place(x=560,y=20)
    r1=Label(f1,text="12GB RAM 129GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    r1.place(x=560,y=45)
    r2=Label(f1,text="PRICE : 36000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    r2.place(x=560,y=65)
    r3=Label(f1,text="⭐⭐⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    r3.place(x=560,y=90)
    btnr=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=rb)
    btnr.place(x=770,y=45)

#techno
    t=Label(f1,text="TECHNO C7A ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    t.place(x=560,y=180)
    t1=Label(f1,text="8GB RAM 128GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    t1.place(x=560,y=205)
    t2=Label(f1,text="PRICE : 15000 ✨✨ ",font=("Arial", 10),
        fg="black",bg='white')
    t2.place(x=560,y=230)
    t3=Label(f1,text="⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    t3.place(x=560,y=255)
    btnt=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=tb)
    btnt.place(x=770,y=230)

#REALME
    e=Label(f1,text="REALMI M30 PRO ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    e.place(x=560,y=345)
    e1=Label(f1,text="12GB RAM 6124GB 📱 ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    e1.place(x=560,y=370)
    e2=Label(f1,text="PRICE : 33000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    e2.place(x=560,y=395)
    e3=Label(f1,text="⭐⭐⭐⭐ ",font=("Arial", 10),
        fg="black",bg='white')
    e3.place(x=560,y=420)
    btne=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=eb)
    btne.place(x=770,y=395)
    
#home buttom
    butnh=Button(f1,text='Back To Home',width=40,height=2,activebackground='#2E86C1',
                 fg='white',bg='#5DADE2',cursor='mouse',font=("Arial", 15, "bold"))
    butnh.place(x=0,y=529)
    butnc=Button(f1,text='Viwe Your Cart',width=40,height=2,activebackground='#D35400',
                 fg='white',bg='#DC7633',cursor='mouse',font=("Arial", 15, "bold"))
    butnc.place(x=500,y=529)

    
    

    
mobile()
a.mainloop()

