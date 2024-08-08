##--------------------Window Frame--------------------------------
##
##from tkinter import*
##
##top=Tk() ##application creation
##
##top.title("GUI WINDOW") ##title
##
##top.geometry("400x400")  ##default size
##
##top.config(bg="#48ACCD")  ##look(hexadecimal color codes)

##top.mainloop() ##closing the application
##
##
##----------------------Buttons------------------------------------
##
##from tkinter import*
##
##top=Tk()
##
##top.geometry("400x250")
##
##top.config(bg='pink')
##
##btn1=Button(top,text="Black",fg="red")
##btn1.pack(side=LEFT)
##
##btn2=Button(top,text="White",fg="Green")
##btn2.pack(side=RIGHT)
##
##btn3=Button(top,text="Orange",fg="blue")
##btn3.pack(side=TOP)
##
##def ss():
##    print('Welcome')
##
##btn4=Button(top,text="Red",fg="black")
##btn4.pack(side=BOTTOM)
##
##btn5=Button(top,text="OK",width=10,activebackground="yellow",
##            
##            font=("Times New Roman",20,"bold"),foreground="white",
##            
##            background="green",command=ss).place(x=0,y=0)
##
##
##top.mainloop()
##
##
##-----------------Label & Entry Box------------------
##
##from tkinter import*
##
##top=Tk()
##
##top.geometry("400x250")
##
##name=Label(top,text="Name").place(x=30,y=50)
##
##email=Label(top,text="Email").place(x=30,y=100)
##
##password=Label(top,text="Password").place(x=30,y=150)
##
##n1=Entry(top).place(x=80,y=50)
##
##n2=Entry(top).place(x=80,y=100)
##
##n3=Entry(top).place(x=100,y=150)
##
##top.mainloop()
##
####----------------------Messagebox--------------------------
##
##from tkinter import*
##from tkinter import messagebox
##
##top=Tk()
##
##def fun():
##    messagebox.showinfo("Hello","Thankyou for your Submission")
##    
##def fun1():
##    messagebox.showerror("Hello","Something Wrong")
##b1=Button(top,text="Submit",command=fun)
##b1.pack()
##b2=Button(top,text="Cancel",command=fun1)
##b2.pack()
##top.mainloop()
    
##------------------------checkbutton--------------------------------
##Select more than one option
##
##from tkinter import *   
##  
##top = Tk()  
##  
##top.geometry("200x200")
##
##lbl=Label(top,text="Select your Language").place(x=500,y=20)
##  
##checkvar1 = IntVar()  
##  
##checkvar2 = IntVar()  
##  
##checkvar3 = IntVar()  
##  
##chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1,
##                      onvalue = 1, offvalue = 0, height = 2, width = 10)  
##  
##chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
##  
##chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
##  
##chkbtn1.pack()  
##  
##chkbtn2.pack()
##
##chkbtn3.pack()  
##  
##top.mainloop()
##
##-------------------------ListBox--------------------
##
##from tkinter import*
##
##top=Tk()
##
##top.geometry("1200x1200")
##
##top.config(bg="lightpink")
##
##lbl=Label(top,text="A list of Font Styles :",bg="black",fg="white")
##
##lbl.pack()
##
##lbox=Listbox(top,bg="yellow")
##
##lbox.insert(1,"Arial")
##
##lbox.insert(2,"Calibri")
##
##lbox.insert(3,"Courier New")
##
##lbox.insert(4,"Times New Roman")
##
##lbox.pack()
##
##top.mainloop()
##
##
##---------------Radio Button----------------------
##
##from tkinter import *  
##  
##def selection():  
##   selection = "You selected the option " + str(radio.get())  
##   label.config(text = selection)  
##  
##top = Tk()  
##top.geometry("300x150")  
##radio = IntVar()  
##lbl = Label(text = "Favourite programming language:")  
##lbl.pack()  
##R1 = Radiobutton(top, text="C", variable=radio, value=1,  
##                  command=selection)  
##R1.pack( anchor = W )  
##  
##R2 = Radiobutton(top, text="C++", variable=radio, value=2,  
##                  command=selection)  
##R2.pack( anchor = W )  
##  
##R3 = Radiobutton(top, text="Java", variable=radio, value=3,  
##                  command=selection)  
##R3.pack( anchor = W)  
##  
##label = Label(top)  
##label.pack()  
##top.mainloop()  
##
##-----------------combo box-----------------
##
import tkinter as tk
from tkinter import ttk
  
# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
  
# label text for title
ttk.Label(window, text = "Months", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()
##
##
##-----------------Canvas Button------------------------
##
##from tkinter import *   
##  
##top = Tk()  
##  
##top.geometry("200x200")  
##    
##c = Canvas(top,bg = "pink",height = 200,width = 200)  
##  
##arc = c.create_arc((5,10,150,200),start = 0,extent = 90*2, fill= "black")  
##  
##c.pack()  
##  
##top.mainloop()
##
##
##
##
##
##
##
##
##---------create a frame inside the main page--------

##from tkinter import*
##from tkinter import messagebox
##
##top=Tk()
##
##top.title("LOGIN SAMPLE") 
##
##top.geometry("400x250")
##
##def msg():
##    messagebox.showinfo("Hello","Thankyou for your Submission")
##
##def nxt():
####second page
##    f1=Frame(top,height=1250,width=1200,bg='pink')
##    f1.pack(fill=X)
##
##    btn=Button(f1,text="Next",width=10,
##            
##            font=("Times New Roman",10,"bold"),foreground="white",
##            
##            background="lightblue",command=msg).place(x=25,y=125)
##
##    btn=Button(f1,text="Back",width=10,
##            
##            font=("Times New Roman",10,"bold"),foreground="white",
##            
##            background="lightblue",command=f1.destroy).place(x=150,y=125)
##
####first page
##name=Label(top,text="Name").place(x=30,y=50)
##
##password=Label(top,text="Password").place(x=30,y=100)
##
##n1=Entry(top).place(x=100,y=50)
##
##n2=Entry(top).place(x=100,y=100)
##
##btn5=Button(top,text="OK",width=10,activebackground="yellow",
##            
##            font=("Times New Roman",10,"bold"),foreground="white",
##            
##            background="green",command=nxt).place(x=25,y=125)
##
##top.mainloop()
