## page 4 FOR tv

#SPEAKER
def sb():
    messagebox.showinfo("Message", "SONY 0071 ADDED TO CART")

#TWS

def tb():
    messagebox.showinfo("Message", "TRUCK AIR BUTS + ADDED TO CART")

#pendrive
def pb():
    messagebox.showinfo("Message", "ZEBRONICS ZEB 2 ADDED TO CART")

#NECKBAND
def nb():
    messagebox.showinfo("Message", "BOAT ROCKERS 260 PRO ADDED TO CART")

#watch
def wb():
    messagebox.showinfo("Message", "SAMSUNG WATCH-4 ADDED TO CART")
##
#mouse
def ab():
    messagebox.showinfo("Message", "ASUS 4.0 ADDED TO CART")    

    
from tkinter import*
import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("ONLINE SHOPPING NAME")
a.geometry("1200x1200")
a.config(bg="#7393B3")
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

    s=Label(f1,text="SPEAKER ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=40,y=20)
    s1=Label(f1,text="SONY 0071 ",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    s1.place(x=40,y=55)
    sS=Label(f1,text="1 HOUR CHARGE = 10 Hr BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=40,y=75)    
    s2=Label(f1,text="PRICE : 2500  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=40,y=100)
    s3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=40,y=125)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sb)
    btns.place(x=300,y=75)

#TWS

    i=Label(f1,text="--TWS-- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=40,y=195)
    i1=Label(f1,text="TRUCK AIR BUTS +",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    i1.place(x=40,y=230)
    i1=Label(f1,text="10 MM DRIVER 12Hr BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=250)    
    i2=Label(f1,text="PRICE : 1200  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=40,y=275)
    i3=Label(f1,text="★★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=40,y=300)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=tb)
    btni.place(x=300,y=250)
##
###paNDRIVE
    o=Label(f1,text="-PENDRIVE- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=40,y=365)
    o1=Label(f1,text="ZEBRONICS ZEB 2",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    o1.place(x=40,y=405)
    oc=Label(f1,text="256 GB ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=40,y=425)    
    o2=Label(f1,text="PRICE : 900  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=40,y=450)
    o3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=40,y=475)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=pb)
    btno.place(x=300,y=425)
##
##neckband

    s=Label(f1,text="NECKBAND",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=560,y=20)
    s1=Label(f1,text="BOAT ROCKERS 260 PRO",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    s1.place(x=560,y=55)
    sS=Label(f1,text="20MM DRIVER 1 DAY BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=560,y=75)    
    s2=Label(f1,text="PRICE : 1500  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=560,y=100)
    s3=Label(f1,text="★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=560,y=125)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=nb)
    btns.place(x=800,y=75)
##
##WATCH
    i=Label(f1,text="SMART WATCH",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=560,y=195)
    i1=Label(f1,text="SAMSUNG WATCH-4",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    i1.place(x=560,y=230)
    i1=Label(f1,text="BLUETOOTH SUPPORTED 5G",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=560,y=250)    
    i2=Label(f1,text="PRICE : 12000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=560,y=275)
    i3=Label(f1,text="★★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=560,y=300)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=wb)
    btni.place(x=800,y=250)
##
#####MOUSE
    o=Label(f1,text="-MOUSE- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=560,y=365)
    o1=Label(f1,text="ASUS 4.0",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    o1.place(x=560,y=405)
    oc=Label(f1,text="BLUETOOTH v5.0 STANDBY",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=560,y=425)    
    o2=Label(f1,text="PRICE : 800  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=560,y=450)
    o3=Label(f1,text="★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=560,y=475)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ab)
    btno.place(x=800,y=425)
    
#home buttom
    butnh=Button(f1,text='Back To Home',width=40,height=2,activebackground='#2E86C1',
                 fg='white',bg='#5DADE2',cursor='mouse',font=("Arial", 15, "bold"))
    butnh.place(x=0,y=529)
    butnc=Button(f1,text='Viwe Your Cart',width=40,height=2,activebackground='#D35400',
                 fg='white',bg='#DC7633',cursor='mouse',font=("Arial", 15, "bold"))
    butnc.place(x=500,y=529)

    
    

    
mobile()
a.mainloop()

