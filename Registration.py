from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql


top=Tk()

top.title("LOGIN SAMPLE") 

top.geometry("400x250")
title=Label(top,text="ミ★Imagecon online shoping★彡",font=("Times New Roman",40,"bold"),bg="white",fg="red")
title.place(x=250,y=20)

address=Label(top,text="New Bus Stand, Salem - 636004",font=("Times New Roman",20,"bold"),bg="white",fg="red").place(x=430,y=90)

    
copyrght=Label(top,text="@2023 imagecon online shoping - Salem",font=("Times New Roman",15,"bold"),bg="white").place(x=490,y=600)

    
        
label_0=Label(top,text="REGISTRATION DETAILS",font=("Calibri",25),bg="#2F2F4F",fg="white")
label_0.place(x=515,y=150)
        
label_1=Label(top,text="FIRST NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_1.place(x=230,y=220)
ebb_1=Entry(top)
ebb_1.place(x=440,y=229,width=220,height=23)
        
label_2=Label(top,text="LAST NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_2.place(x=690,y=220)
ebb_2=Entry(top)
ebb_2.place(x=940,y=229,width=220,height=23)
        
label_3=Label(top,text="GENDER",font=("Calibri",20),bg="#2F2F4F",fg="white").place(x=230,y=260)
data=tk.StringVar()
ebb=ttk.Combobox(top,textvariable = data)

ttk.Label((ebb,text-"select gender:"),font =("times new roman",10).grid(column=1,row=3,padx=10,pady=25))
ebb.current()
ebb["values"]=("MALE","FEMALE","TRANSGENDER")
ebb.grid(column=1,row=3)
label_4=Label(top,text="DATE OF BIRTH",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_4.place(x=690,y=260)
ebb_4=Entry(top)
ebb_4.place(x=940,y=269,width=220,height=23)
        
label_5=Label(top,text="ACC NO",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_5.place(x=230,y=300)
ebb_5=Entry(top)
ebb_5.place(x=440,y=309,width=220,height=23)
        
label_6=Label(top,text="ACC TYPE",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_6.place(x=690,y=300)
data2=tk.StringVar()
ebb_6=ttk.Combobox(top,textvariable = data2)
ebb_6["values"]=("Current Account","Saving Account",)
ebb_6['state']="readonly"
ebb_6.place(x=940,y=309,width=220,height=23)
        
label_7=Label(top,text="MOBILE NO",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_7.place(x=230,y=340)
ebb_7=Entry(top)
ebb_7.place(x=440,y=349,width=220,height=23)
            
label_8=Label(top,text="E-MAIL ID",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_8.place(x=690,y=340)
ebb_8=Entry(top)
ebb_8.place(x=940,y=349,width=220,height=23)
            
label_9=Label(top,text="INITIAL AMOUNT",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_9.place(x=230,y=380)
ebb_9=Entry(top)
ebb_9.place(x=440,y=389,width=220,height=23)
            
label_10=Label(top,text="USER NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_10.place(x=230,y=440)
ebb_10=Entry(top)
ebb_10.place(x=440,y=449,width=220,height=23)
            
label_11=Label(top,text="PASSWORD",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_11.place(x=230,y=480)
ebb_11=Entry(top)
ebb_11.place(x=440,y=489,width=220,height=23)
            
label_12=Label(top,text="CONFIRM PASSWORD",font=("Calibri",20),bg="#2F2F4F",fg="white")
label_12.place(x=690,y=480)
ebb_12=Entry(top)
ebb_12.place(x=940,y=489,width=220,height=23)

top.mainloop()
