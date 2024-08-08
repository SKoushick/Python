## page 4 FOR tv

#SAM BUTTON
def sab():
    messagebox.showinfo("Message", "SUMSUNG H03 ADDED TO CART")

#amazon button

def ab():
    messagebox.showinfo("Message", "AMAZONBASIS Z100 ADDED TO CART")

#panasonic button
def ob():
    messagebox.showinfo("Message", "PANASONIC S9 ADDED TO CART")

#redmi
def rb():
    messagebox.showinfo("Message", "REDMI z720 ADDED TO CART")

#lg
def lb():
    messagebox.showinfo("Message", "LG 900 ADDED TO CART")

#realmi
def sb():
    messagebox.showinfo("Message", "SONY 3E PRO ADDED TO CART")    

    
from tkinter import*
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("ONLINE SHOPPING NAME")
a.geometry("1200x1200")
a.config(bg="#7393B3")
##
###title
def TV():
    name=Label(a,text="---ONLINE SHOP NAME---",bg="black",font=("Brush Script MT",30,'bold')
       ,fg="white",width=200)
    name.pack()

#frame
    f1 = Frame(a, bg="white", width=1000, height=600)  
    f1.pack()
###samsung

    s=Label(f1,text="SUMSUNG H03 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=40,y=20)
    s1=Label(f1,text="4K UHD 32 inchs ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    s1.place(x=40,y=45)
    sS=Label(f1,text="SMART TV ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=40,y=65)    
    s2=Label(f1,text="PRICE : 25000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=40,y=90)
    s3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=40,y=115)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sab)
    btns.place(x=300,y=65)

#amazon

    i=Label(f1,text="AMAZONBASIS Z100 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=40,y=185)
    i1=Label(f1,text="HD SCREEN 28 inches",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=210)
    i1=Label(f1,text="NORMAL TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=230)    
    i2=Label(f1,text="PRICE : 12000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=40,y=255)
    i3=Label(f1,text="★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=40,y=280)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ab)
    btni.place(x=300,y=230)
##
###panasonic
    o=Label(f1,text="PANASONIC S9  ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=40,y=355)
    o1=Label(f1,text="FULL HD 48 inches ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    o1.place(x=40,y=385)
    oc=Label(f1,text="SMART TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=40,y=405)    
    o2=Label(f1,text="PRICE : 18000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=40,y=430)
    o3=Label(f1,text="★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=40,y=455)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ob)
    btno.place(x=300,y=405)

###sony
    r=Label(f1,text="REDMI z720 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    r.place(x=560,y=20)
    r1=Label(f1,text="4K ULTRA HD 55 inches",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    r1.place(x=560,y=45)
    r1=Label(f1,text="ANDROID TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    r1.place(x=560,y=65)    
    r2=Label(f1,text="PRICE : 30000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    r2.place(x=560,y=90)
    r3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    r3.place(x=560,y=115)
    btnr=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=rb)
    btnr.place(x=800,y=65)

###LG

    l=Label(f1,text="LG 900 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    l.place(x=560,y=185)
    l1=Label(f1,text="4K UHD 32 inchs ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    l1.place(x=560,y=210)
    ll=Label(f1,text="NORMAL TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    ll.place(x=560,y=230)    
    l2=Label(f1,text="PRICE : 26000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    l2.place(x=560,y=255)
    l3=Label(f1,text="★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    l3.place(x=560,y=280)
    btnl=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=lb)
    btnl.place(x=800,y=230)

###SONY
    o=Label(f1,text="SONY 3E PRO ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=560,y=355)
    o1=Label(f1,text=" HD 32 inches ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    o1.place(x=560,y=385)
    oc=Label(f1,text="ANDROID TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=560,y=405)    
    o2=Label(f1,text="PRICE : 10000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=560,y=430)
    o3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=560,y=455)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sb)
    btno.place(x=800,y=405)    

    
#home buttom
    butnh=Button(f1,text='Back To Home',width=40,height=2,activebackground='#2E86C1',
                 fg='white',bg='#5DADE2',cursor='mouse',font=("Arial", 15, "bold"))
    butnh.place(x=0,y=529)
    butnc=Button(f1,text='Viwe Your Cart',width=40,height=2,activebackground='#D35400',
                 fg='white',bg='#DC7633',cursor='mouse',font=("Arial", 15, "bold"))
    butnc.place(x=500,y=529)

    
    

    
TV()
a.mainloop()

