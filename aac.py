#function for mobile 

# samsung button
def samb():
    global x
    a = 56000
    s="SAMSUNG S20"
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "SAMSUNG S20 ADDED TO CART")
    

# iqoo button
def ib():
    global x
    a = 20000
    s="IQOO Z7"
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "IQOO Z7 ADDED TO CART")
    

# poco button
def oeb():
    global x
    a = 12000
    s="POCO M2"
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "POCO M2 ADDED TO CART")
    

# redmi button
def reb():
    global x
    a = 36000
    x += a
    s="REDMI C20"
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "REDMI C20 ADDED TO CART")
    

# techno button
def tb():
    global x
    a = 12000
    s="TECHNO C7A"
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "TECHNO C7A ADDED TO CART")
    

# realme button
def eb():
    global x
    a = 33000
    s="REALMI M30 PRO"
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "REALMI M30 PRO ADDED TO CART")
    


#function for tv

#amazon button

def aab():
    global x
    s="AMAZONBASIS Z100"
    a = 12000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "AMAZONBASIS Z100 ADDED TO CART")
    

#panasonic button
def ob():
    global x
    s="PANASONIC S9"
    a = 1800
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "PANASONIC S9 ADDED TO CART")
    

#redmi
def rb():
    global x
    s="REDMI z720"
    a = 30000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "REDMI z720 ADDED TO CART")
    

#lg
def lab():
    global x
    s="LG 900"
    a =26000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "LG 900 ADDED TO CART")
    

#realmi
def sib():
    global x
    s="SONY 3E PRO"
    a = 10000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "SONY 3E PRO ADDED TO CART")


#function for accessories


def sab():
    global x
    s="SUMSUNG H03"
    a = 25000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "SUMSUNG H03 ADDED TO CART")
    

#amazon button

def ab():
    global x
    s="AMAZONBASIS Z100"
    a = 12000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "AMAZONBASIS Z100 ADDED TO CART")
    

#panasonic button
def ob():
    global x
    s="PANASONIC S9"
    a = 1800
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "PANASONIC S9 ADDED TO CART")
    

#redmi
def rb():
    global x
    s="REDMI z720"
    a = 30000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "REDMI z720 ADDED TO CART")
    

#lg
def lb():
    global x
    s="LG 900"
    a =26000
    x += a
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "LG 900 ADDED TO CART")
    

#realmi
def sb():
    global x
    s="SONY 3E PRO"
    a = 10000
    x += a  
    a=connect.cursor()
    sql='INSERT INTO itams (NAME,PRICE) VALUES (%s,%s)'
    product=(s,a)
    a.execute(sql,product)
    connect.commit()
    messagebox.showinfo("Message", "SONY 3E PRO ADDED TO CART")


    
      
        
