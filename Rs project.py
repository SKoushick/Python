from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

# ---------------sql server---------------------
db_connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123',
    database='qb'
)
my_database=db_connection.cursor()
print("Conncted successfully")

#---------------main Window--------------------
root = Tk()
root.title("BANKING SYSTEM")
root.geometry("1366x768+0+0")
root.config(bg="#2F2F4F")
root.state("zoomed")
def main():
    main=Frame(root,bg="#2F2F4F",height='1000')
    main.pack(fill= X)
    
    title_label=Label(main,text="I M A G E C O N   U N I O N   B A N K",font=("Times New Roman",40,"bold"),bg="#2F2F4F",fg="white")
    title_label.place(x=240,y=20)
    
    address_label=Label(main,text="N e w  B u s  S t a n d , S a l e m  -  6 3 6  0 0 4",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
    address_label.place(x=490,y=90)
    
    copyright_label=Label(main,text="@2022 IMAGECON UNION BANK - SALEM",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
    copyright_label.place(x=480,y=670)
    
    def login():
        login_frame=Frame(main,bg="#2F2F4F",height='1200')
        login_frame.pack(fill= X)
        
        title_label=Label(login_frame,text="I M A G E C O N   U N I O N   B A N K",font=("Times New Roman",40,"bold"),bg="#2F2F4F",fg="white")
        title_label.place(x=240,y=20)
        
        address_label=Label(login_frame,text="N e w  B u s  S t a n d , S a l e m  -  6 3 6  0 0 4",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
        address_label.place(x=490,y=90)
        
        copyright_label=Label(login_frame,text="@2022 IMAGECON UNION BANK - SALEM",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
        copyright_label.place(x=480,y=670)
           
        label_0=Label(login_frame,text="ACCOUNT LOGIN DETAILS",font=("Calibri",25),bg="#2F2F4F",fg="white")
        label_0.place(x=510,y=230)
        
        label_1=Label(login_frame,text="USER NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_1.place(x=480,y=320)
        eb_1=Entry(login_frame)
        eb_1.place(x=640,y=329,width=250,height=23)
        label_2=Label(login_frame,text="PASS WORD",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_2.place(x=480,y=390)
        eb_2=Entry(login_frame)
        eb_2.place(x=640,y=389,width=250,height=23)
        
        def check():
            user=eb_1.get()
            passs=eb_2.get()
            
            sql="SELECT * from register where username=%s and password=%s"
            my_database.execute(sql,[(user),(passs)])
            result=my_database.fetchall()
            print(result)
            def option():
                option_frame=Frame(login_frame,bg="#2F2F4F",height='1200')
                option_frame.pack(fill=X)
                
                title_label=Label(option_frame,text="I M A G E C O N   U N I O N   B A N K",font=("Times New Roman",40,"bold"),bg="#2F2F4F",fg="white")
                title_label.place(x=240,y=20)
                
                address_label=Label(option_frame,text="N e w  B u s  S t a n d , S a l e m  -  6 3 6  0 0 4",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
                address_label.place(x=490,y=90)
                
                copyright_label=Label(option_frame,text="@2022 IMAGECON UNION BANK - SALEM",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
                copyright_label.place(x=480,y=670)
                
                button_frame=Frame(option_frame,width=370,height=500,highlightbackground="white",highlightthickness=1,bg="#2F2F4F",bd=5)
                button_frame.place(x=70,y=140)
                
                main_frame=Frame(option_frame,width=840,height=500,highlightbackground="white",highlightthickness=1,bg="#2F2F4F",bd=5)
                main_frame.place(x=450,y=140)
                
                summa_frame=Frame(main_frame,width=820,height=480,bg="gray")
                summa_frame.place(x=5,y=5)
                
                Label(summa_frame,text="W E L C O M E",font=("Times New Roman",28,"bold"),bg="gray").place(x=280,y=110)
                Label(summa_frame,text="T O",font=("Times New Roman",28,"bold"),bg="gray").place(x=380,y=210)
                Label(summa_frame,text="I M A G E C O N  U N I O N  B A N K",font=("Times New Roman",28,"bold"),bg="gray").place(x=110,y=320)
                
                title_label_1=Label(button_frame,text="F E T U R E S",font=("Times New Roman",20,"bold"),bg="#2F2F4F",fg="white")
                title_label_1.place(x=100,y=15)
                
                def details():
                    details_frame=Frame(main_frame,width=820,height=480,bg="gray")
                    details_frame.place(x=5,y=5)
                    print(eb_1.get())
                    name1=result[0]
                    
                    name=name1[0]
                    initial=name1[1]
                    dob=name1[3]
                    acc=name1[4]
                    acctype=name1[5]
                    mob=name1[6]
                    mail=name1[7]
                    
                    details=Label(details_frame,text="A C C O U N T  D E T A I L S",font=("Times New Roman",28,"bold"),bg="gray").place(x=170,y=30)
                    Label(details_frame,text="H O L D E R  N A M E      -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=110)
                    Label(details_frame,text="D A T E   O F B I R T H    -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=160)
                    Label(details_frame,text="A C C O U N T  N O          -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=210)
                    Label(details_frame,text="A C C O U N T  T Y P E    -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=260)
                    Label(details_frame,text="M O B I L E  N O               -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=310)
                    Label(details_frame,text="G - M A I L  I D                 -",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=360)
                    
                    Label(details_frame,text=(name,initial),font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=110)
                    Label(details_frame,text=dob,font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=160)
                    Label(details_frame,text=acc,font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=210)
                    Label(details_frame,text=acctype,font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=260)
                    Label(details_frame,text=mob,font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=310)
                    Label(details_frame,text=mail,font=("Times New Roman",15,"bold"),bg="gray").place(x=440,y=360)                  
                    
                    # update_button=tk.Button(details_frame,text="UPDATE",font=("Times New Roman",15,"bold"),bg="gray",fg="black",bd=5)
                    # update_button.place(x=500,y=410,width=200,height=40)
                    
                details_button=tk.Button(button_frame,text="Account Details",font=("Times New Roman",15,"bold"),command=details,bg="gray",fg="black")
                details_button.place(x=80,y=70,width=220,height=40)
                
                def balance():
                    balance_frame=Frame(main_frame,width=820,height=480,bg="gray")
                    balance_frame.place(x=5,y=5)
                    name1=result[0]
                    c_amd=name1[8]
                    a_amd=c_amd-500
                                       
                    Label(balance_frame,text="B A L A N C E  E N Q U I R Y",font=("Times New Roman",28,"bold"),bg="gray").place(x=170,y=30)
                    Label(balance_frame,text="C U R R E N T  B A L A N C E         =",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=160)
                    Label(balance_frame,text="A V A I L A B L E  B A L A N C E    =",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=260)
                
                    Label(balance_frame,text=c_amd,font=("Times New Roman",15,"bold"),bg="gray").place(x=500,y=160)
                    Label(balance_frame,text=a_amd,font=("Times New Roman",15,"bold"),bg="gray").place(x=500,y=260)
                
                balance_button=tk.Button(button_frame,text="Balance Enquiry",font=("Times New Roman",15,"bold"),command=balance,bg="gray",fg="black")
                balance_button.place(x=80,y=125,width=220,height=40)
                
                def transfer():
                    transfer_frame=Frame(main_frame,width=820,height=480,bg="gray")
                    transfer_frame.place(x=5,y=5)
                    
                    Label(transfer_frame,text="F U N D  T R A N S F E R",font=("Times New Roman",28,"bold"),bg="gray").place(x=170,y=30)
                    Label(transfer_frame,text="BENEFICIARY FULL NAME",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=160)
                    Label(transfer_frame,text="BENEFICIARY ACCOUNT NO",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=210)
                    Label(transfer_frame,text="ENTER TRANSFER AMOUNT",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=260)
                    
                    sql="SELECT beneficiary_name from transfer"
                    my_database.execute(sql)
                    result1=my_database.fetchall()
                    print(result1)
                    
                    name=result1
                    
                    sql="SELECT beneficiary_acc_no from transfer"
                    my_database.execute(sql)
                    result2=my_database.fetchall()
                    print(result2)
                    
                    data1=tk.StringVar()
                    ebb_1=ttk.Combobox(transfer_frame,textvariable = data1)
                    ebb_1["values"]=name
                    ebb_1['state']="readonly"
                    ebb_1.place(x=470,y=160,width=250,height=23)
                    data2=tk.StringVar()
                    ebb_2=ttk.Combobox(transfer_frame,textvariable = data2)
                    ebb_2["values"]=result2
                    ebb_2['state']="readonly"
                    ebb_2.place(x=470,y=210,width=250,height=23)
                    ebb_3=tk.IntVar()
                    ebb_3=Entry(transfer_frame)
                    ebb_3.place(x=470,y=260,width=250,height=23)
                                        
                    def add():
                        add_frame=Frame(transfer_frame,width=820,height=480,bg="gray")
                        add_frame.place(x=5,y=5)
                        
                        Label(add_frame,text="F U N D  T R A N S F E R",font=("Times New Roman",28,"bold"),bg="gray").place(x=170,y=30)
                        Label(add_frame,text="BENEFICIARY FULL NAME",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=160)
                        Label(add_frame,text="BENEFICIARY ACCOUNT NO",font=("Times New Roman",15,"bold"),bg="gray").place(x=150,y=230)
                        
                        eb_1=Entry(add_frame)
                        eb_1.place(x=470,y=160,width=250,height=23)
                        eb_2=Entry(add_frame)
                        eb_2.place(x=470,y=230,width=250,height=23)
                        def save_add():
                            if (eb_1.get() or eb_2.get()==" "):
                                messagebox.showerror("Error", "Enter All Details")
                            elif (eb_1.get() and eb_2.get()):
                                op = messagebox.askyesno("Save", "Do you really want to save?")
                                if op > 0:
                                    sql_statement="INSERT INTO transfer (beneficiary_name,beneficiary_acc_no) values(%s,%s)"
                                    values=(eb_1.get(),eb_2.get())
                                    my_database.execute(sql_statement,values)
                                    db_connection.commit()
                                    add_frame.destroy()
                                    
                        save_button=tk.Button(add_frame,text="SAVE BENEFICIARY ",font=("Times New Roman",15,"bold"),command=save_add,bg="gray",fg="black",bd=5)
                        save_button.place(x=300,y=340,width=250,height=40)
                        
                        back_button=tk.Button(add_frame,text="BACK ",font=("Times New Roman",15,"bold"),command=add_frame.destroy,bg="gray",fg="black",bd=5)
                        back_button.place(x=300,y=400,width=250,height=40)
                        
                    
                    add_button=tk.Button(transfer_frame,text="ADD BENEFICIARY ",font=("Times New Roman",15,"bold"),command=add,bg="gray",fg="black",bd=5)
                    add_button.place(x=300,y=400,width=250,height=40)
                    
                    def fund():
                        print(result)
                        amd=result[0]
                        amd=amd[8]
                        amd=int(amd)
                        print(amd)
                        
                        t_amd=ebb_3.get()
                        t_amd=int(t_amd)
                        # f_amd=IntVar()
                        f_amd=amd-t_amd
                        
                        print(f_amd)
                        
                        op = messagebox.askyesno("Save", "Do you really want to save?")
                        
                        sql_statement = "UPDATE register SET initial_amount='2000' where password='1'"
                        my_database.execute(sql_statement)
                        db_connection.commit()
                        transfer_frame.destroy()
                        
                    fund_button=tk.Button(transfer_frame,text="FUND TRANSFER ",font=("Times New Roman",15,"bold"),command=fund,bg="gray",fg="black",bd=5)
                    fund_button.place(x=300,y=340,width=250,height=40)
                    
                    
                transfer_button=tk.Button(button_frame,text="Fund Transfer",font=("Times New Roman",15,"bold"),command=transfer,bg="gray",fg="black")
                transfer_button.place(x=80,y=180,width=220,height=40)
                
                def contact():
                    contact_frame=Frame(main_frame,width=820,height=480,bg="gray")
                    contact_frame.place(x=5,y=5)
                    
                    Label(contact_frame,text="C O N T A C T  U S",font=("Times New Roman",28,"bold"),bg="gray").place(x=230,y=30)
                    Label(contact_frame,text="ADDRESS :",font=("Times New Roman",17,"bold"),bg="gray").place(x=50,y=130)
                    Label(contact_frame,text="182/1, Angammal Colony, Chinneri Vayalkadu,",font=("Times New Roman",17),bg="gray").place(x=180,y=130)
                    Label(contact_frame,text="Pallapatti (PO), (Near New Bus Stand),",font=("Times New Roman",17),bg="gray").place(x=180,y=170)
                    Label(contact_frame,text="Salem-636009.",font=("Times New Roman",17),bg="gray").place(x=180,y=210)
                    Label(contact_frame,text="Enquiry:",font=("Times New Roman",17,"bold"),bg="gray").place(x=50,y=260)
                    Label(contact_frame,text="Customer Enquiry:",font=("Times New Roman",17,"bold"),bg="gray").place(x=50,y=310)
                    Label(contact_frame,text="Technical Support:",font=("Times New Roman",17,"bold"),bg="gray").place(x=50,y=360)
                    Label(contact_frame,text="+91 7373246001 / +91 8190064176",font=("Times New Roman",17),bg="gray").place(x=145,y=260)
                    Label(contact_frame,text="training@imageconunionbank.com",font=("Times New Roman",17),bg="gray").place(x=250,y=310)
                    Label(contact_frame,text="support@imageconunionbank.com",font=("Times New Roman",17),bg="gray").place(x=250,y=360)
                
                contact_button=tk.Button(button_frame,text="Contact Us",font=("Times New Roman",15,"bold"),command=contact,bg="gray",fg="black")
                contact_button.place(x=80,y=235,width=220,height=40)
                
                def about():
                    about_frame=Frame(main_frame,width=820,height=480,bg="gray")
                    about_frame.place(x=5,y=5)
                    
                    Label(about_frame,text="A B O U T  O U R  B A N K",font=("Times New Roman",28,"bold"),bg="gray").place(x=180,y=30)
                    Label(about_frame,text="Brand Ethos",font=("Times New Roman",22,"bold"),bg="gray").place(x=70,y=100)
                    Label(about_frame,text="To be the Professionals’ Bank of India",font=("Times New Roman",15),bg="gray").place(x=120,y=150)
                    Label(about_frame,text="Vision:",font=("Times New Roman",22,"bold"),bg="gray").place(x=70,y=180)
                    Label(about_frame,text="Building the Finest Quality Large Bank of the World in India",font=("Times New Roman",15),bg="gray").place(x=120,y=220)
                    Label(about_frame,text="Mission",font=("Times New Roman",22,"bold"),bg="gray").place(x=70,y=250)
                    Label(about_frame,text="To establish a high-quality, customer-centric, service-driven,",font=("Times New Roman",15),bg="gray").place(x=120,y=300)
                    Label(about_frame,text="private Indian Bank catering to the ‘Future Businesses of India.",font=("Times New Roman",15),bg="gray").place(x=90,y=330)
                
                about_button=tk.Button(button_frame,text="About Us",font=("Times New Roman",15,"bold"),command=about,bg="gray",fg="black")
                about_button.place(x=80,y=290,width=220,height=40)
                               
                def logout():
                    option_frame.destroy()
                    login_frame.destroy()
                    
                logout_button=tk.Button(button_frame,text="Log Out",font=("Times New Roman",15,"bold"),command=logout,bg="gray",fg="black")
                logout_button.place(x=80,y=345,width=220,height=40)
                     
            if result:
                print("Login successfully")
                option()
            else:
                messagebox.showinfo("Login",'Enter Valid Details..!!!')
                print("Tata... Bye... Bye...")
            
        login_button=tk.Button(login_frame,text="LOG IN",font=("Times New Roman",15,"bold"),command=check,bg="gray",fg="black")
        login_button.place(x=580,y=470,width=220,height=40)
        
        back_button=tk.Button(login_frame,text="BACK",font=("Times New Roman",15,"bold"),command=login_frame.destroy,bg="gray",fg="black")
        back_button.place(x=580,y=540,width=220,height=40)
    
    def signup():
        signup_frame=Frame(main,bg="#2F2F4F",height='1200')
        signup_frame.pack(fill= X)
        
        title_label=Label(signup_frame,text="I M A G E C O N   U N I O N   B A N K",font=("Times New Roman",40,"bold"),bg="#2F2F4F",fg="white")
        title_label.place(x=240,y=20)
        
        address_label=Label(signup_frame,text="N e w  B u s  S t a n d , S a l e m  -  6 3 6  0 0 4",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
        address_label.place(x=490,y=90)
        
        copyright_label=Label(signup_frame,text="@2022 IMAGECON UNION BANK - SALEM",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
        copyright_label.place(x=480,y=670)
        
        label_0=Label(signup_frame,text="REGISTRATION DETAILS",font=("Calibri",25),bg="#2F2F4F",fg="white")
        label_0.place(x=515,y=150)
        
        label_1=Label(signup_frame,text="FIRST NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_1.place(x=230,y=220)
        ebb_1=Entry(signup_frame)
        ebb_1.place(x=440,y=229,width=220,height=23)
        
        label_2=Label(signup_frame,text="LAST NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_2.place(x=690,y=220)
        ebb_2=Entry(signup_frame)
        ebb_2.place(x=940,y=229,width=220,height=23)
        
        label_3=Label(signup_frame,text="GENDER",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_3.place(x=230,y=260)
        # eb_3=Entry(signup_frame).place(x=440,y=269,width=220,height=23)
        data1=tk.StringVar()
        ebb_3=ttk.Combobox(signup_frame,textvariable = data1)
        ebb_3["values"]=("MALE",
                        "FEMALE",
                        "TRANSGENDER")
        ebb_3['state']="readonly"
        ebb_3.place(x=440,y=269,width=220,height=23)    
        
        label_4=Label(signup_frame,text="DATE OF BIRTH",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_4.place(x=690,y=260)
        ebb_4=Entry(signup_frame)
        ebb_4.place(x=940,y=269,width=220,height=23)
        
        label_5=Label(signup_frame,text="ACC NO",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_5.place(x=230,y=300)
        ebb_5=Entry(signup_frame)
        ebb_5.place(x=440,y=309,width=220,height=23)
        
        label_6=Label(signup_frame,text="ACC TYPE",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_6.place(x=690,y=300)
        data2=tk.StringVar()
        ebb_6=ttk.Combobox(signup_frame,textvariable = data2)
        ebb_6["values"]=("Current Account",
                        "Saving Account",)
        ebb_6['state']="readonly"
        ebb_6.place(x=940,y=309,width=220,height=23)
        
        label_7=Label(signup_frame,text="MOBILE NO",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_7.place(x=230,y=340)
        ebb_7=Entry(signup_frame)
        ebb_7.place(x=440,y=349,width=220,height=23)
        
        label_8=Label(signup_frame,text="E-MAIL ID",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_8.place(x=690,y=340)
        ebb_8=Entry(signup_frame)
        ebb_8.place(x=940,y=349,width=220,height=23)
        
        label_9=Label(signup_frame,text="INITIAL AMOUNT",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_9.place(x=230,y=380)
        ebb_9=Entry(signup_frame)
        ebb_9.place(x=440,y=389,width=220,height=23)
        
        label_10=Label(signup_frame,text="USER NAME",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_10.place(x=230,y=440)
        ebb_10=Entry(signup_frame)
        ebb_10.place(x=440,y=449,width=220,height=23)
        
        label_11=Label(signup_frame,text="PASSWORD",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_11.place(x=230,y=480)
        ebb_11=Entry(signup_frame)
        ebb_11.place(x=440,y=489,width=220,height=23)
        
        label_12=Label(signup_frame,text="CONFIRM PASSWORD",font=("Calibri",20),bg="#2F2F4F",fg="white")
        label_12.place(x=690,y=480)
        ebb_12=Entry(signup_frame)
        ebb_12.place(x=940,y=489,width=220,height=23)
        
        def save():
            if (ebb_1.get()=="" or ebb_2.get()=="" or ebb_3.get()=="" or ebb_4.get()=="" or ebb_5.get()=="" or ebb_6.get()=="" or ebb_7.get()=="" or ebb_8.get()=="" or ebb_9.get()=="" or ebb_10.get()=="" or ebb_11.get()=="" or ebb_12.get()==""):
                messagebox.showerror("Error", "Enter all details")
            elif (ebb_11.get()!=ebb_12.get()):
                messagebox.showerror("Error", "Check Both Password")
            elif (ebb_1.get()and ebb_2.get() and ebb_3.get() and ebb_4.get() and ebb_5.get() and ebb_6.get() and ebb_7.get() and ebb_8.get() and ebb_9.get() and ebb_10.get() and ebb_11.get() and ebb_12.get() and ebb_11.get() == ebb_12.get()):
                op = messagebox.askyesno("Save", "Do you really want to save?")
                if op > 0:
                    sql_statement="INSERT INTO register (first_Name,last_Name,gender,date_of_birth,acc_no,acc_type,mobile_no,e_mail_id,initial_amount,username,password,c_password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(ebb_1.get(),ebb_2.get(),ebb_3.get(),ebb_4.get(),ebb_5.get(),ebb_6.get(),ebb_7.get(),ebb_8.get(),ebb_9.get(),ebb_10.get(),ebb_11.get(),ebb_12.get())
                    my_database.execute(sql_statement,values)
                    db_connection.commit()
                    signup_frame.destroy()
        
        reg_button=tk.Button(signup_frame,text="REGISTER",font=("Times New Roman",15,"bold"),bg="gray",fg="black",command=save)
        reg_button.place(x=400,y=560,width=220,height=40)
            
        back_button=tk.Button(signup_frame,text="BACK",font=("Times New Roman",15,"bold"),bg="gray",fg="black",command=signup_frame.destroy)
        back_button.place(x=750,y=560,width=220,height=40)
    
    
    login_button=tk.Button(main,text="LOG IN",font=("Times New Roman",15,"bold"),command=login,bg="gray",fg="black",bd=5)
    login_button.place(x=485,y=250,width=400,height=40)
    signup_button=tk.Button(main,text="SIGN UP",font=("Times New Roman",15,"bold"),command=signup,bg="gray",fg="black",bd=5)
    signup_button.place(x=485,y=350,width=400,height=40)

main()

root.mainloop()
