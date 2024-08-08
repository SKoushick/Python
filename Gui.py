from tkinter import*

top=Tk() 

top.title("GUI WINDOW") 
top.config(bg='black')
top.geometry("400x400")
name=Label(top,text="Name").place(x=30,y=50)
n1=Entry(top).place(x=80,y=50)
lbox=Listbox(top,bg="red")
lbox.insert(1,"factorial")
lbox.place(x=80,y=80)
num=0
def fact():
    n=int(input('enter the value:'))
    fact=1
    while n>0:
        fact=fact*n
        n-=1
    print(fact)
btn=Button(top,text='start',fg='red',command=fact).place(x=60,y=300)
