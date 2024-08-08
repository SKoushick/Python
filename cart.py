


def cart():
    s=cursor.execute('SELECT * FROM products')
    name = Label(top, text="---IMAGECON ONLINE SHOPPING---", bg="black", font=("Brush Script MT", 30, 'bold'),
                 fg="white")
    name.pack()
    title = Label(top, text='YOUR CART', bg="gray", font=("Arial black", 15, 'bold'),
                  fg="black").place(x=500, y=75)
    fra1 = Frame(top, bg='white', height=450, width=800)
    fra1.place(x=220, y=130)
    items = Label
    pro = ttk.Treeview(fra1, columns=(1, 2), show='headings', height='8')
    pro.pack()
    pro.heading(1, text='PRODUCT')
    pro.heading(2, text='PRICE')

    a=0
    for x in s:
        tree.insert('', a, text='',values=x)
        a=a+1
    purchase=Button(fra1,text='purchase now ',bg='brown',fg='white',command=pur)
    purchase.pack
    total=Label(fra1,text=x)
    total.pack
        


cart()

def pur():
    messagebox.askquestion("Confirm","Are you sure to purchase?")

# purchase
