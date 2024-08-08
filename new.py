from tkinter import *
from PIL import ImageTk, Image  

app = Tk()
app.title("Welcome")
img =Image.open('C://Users//Admin//OneDrive//Pictures//Camera Roll.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("900x900")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = "Hello kittens",
               font=("Times New Roman", 24))

label2.pack(pady = 50)

# Execute tkinter
app.mainloop()
