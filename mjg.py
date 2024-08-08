from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
win = Tk()  
win.geometry('400x150')  
win.title('Online shopping')

#username label and text entry box
usernameLabel = Label(win, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(win, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(win,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(win, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(win, text="Login", command=validateLogin).grid(row=4, column=0)  

win.mainloop()
