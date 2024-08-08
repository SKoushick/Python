class product:
    def __init__(self,name,quantity,):
        self.quantity=quantity
        self.name=name
    def pn(self):
        print("PRODUCT name is ",self.name)
    def pq(self):
        print("QUANTITY OF PURCHASE IS ",self.quantity)

        
        
class customer:
     def __init__(self,cname,cnumber,cadd):
         self.cname=cname
         self.cnumber=cnumber
         self.cadd=cadd
     def nmae(self):
         priint("CUSTOMER name is ",self.cname)
     def number(self):
         priint("CUSTOMER number is ",self.cnumber)    
     def add(self):
         priint("CUSTOMER address is ",self.cadd)

def v():
    global x
    x=0
    print("to update product detials press 1 ")
    y=int(input("TO ENTER customer detials press 2 "))
    if y==1:
        p=product(name=input("ENTER product name "),quantity=int(input("ENTER the quantity in numbers")))
        l=int(input("ENTER the price of the product"))
        print()
        x+=l
        u=int(input("IF you want to add another product press 1 or press 0 "))
        if u==1:
            p=product(name=input("ENTER product name "),quantity=int(input("ENTER the quantity in numbers")))
            c=int(input("ENTER the price of the product "))
            print()
            x+=c
        print("TOTAL amount to be paid by the customer is ",x)    
    elif y==2:
        c=customer(cname=input("ENTER customers name "),cnumber=int(input("ENTER customers number ")),cadd=input("ENTER customers address"))
        print()
            
    else:
        print("ENTER A valid key")
        v()      
v()                
                
