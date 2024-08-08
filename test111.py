from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

top=tk.Tk()
top.title("Online Purchasing")
top.geometry("1200x800")
top.config("#7df9ff")
top.state('zoomed')

def main():
    main=Frame(top,bg="#7df9ff",height='500')
    main.pack(fill=X)

    title_label=Label(main,text="ミ★Imagecon online shoping★彡",font=("Times New Roman",40,"bold"),bg="#7df9ff",fg="red")
    title_label.place(x=250,y=20)

    address_label=Label(main,text="New Bus Stand, Salem - 636004",font=("Times New Roman",20,"bold"),bg="#7df9ff",fg="red")
    address_label.place(x=490,y=90)
    
    copyright_label=Label(main,text="@2023 imagecon online shoping - Salem",font=("Times New Roman",15,"bold"),bg="#2F2F4F",fg="white")
    copyright_label.place(x=480,y=470)

    

main()
top.mainloop()

