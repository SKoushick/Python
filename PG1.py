##import pymysql
##
##db_connection = pymysql.connect(
##  host="localhost",
##  user="root",
##  password="Kousi7023",
##  database="online_shopping"
##)
##my_database = db_connection.cursor()
##print("connected successfully")


import tkinter
from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image



top=tk.Tk()
top.title('HII')
top.geometry("1200x1200")

img =Image.open('C:/Users/Admin/Pictures/naruto-shippuden-sasuke-chidori-fbo62gvp0dvv6ko2.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(top, image=bg)
label.place(x = 0,y = 0)


title=Label(top,text="ミ★Imagecon online shoping★彡",font=("Times New Roman",40,"bold"),bg="#7df9ff",fg="red")
title.place(x=250,y=20)

address=Label(top,text="New Bus Stand, Salem - 636004",font=("Times New Roman",20,"bold"),bg="#7df9ff",fg="red").place(x=430,y=90)

    
copyrght=Label(top,text="@2023 imagecon online shoping - Salem",font=("Times New Roman",15,"bold"),bg="green").place(x=490,y=600)

top.mainloop()


