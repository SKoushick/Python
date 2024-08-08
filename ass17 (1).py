print("SELECT a brand")
print("you can SELECT maximum brands")

 
class mobile:
     def __init__(self):
         print("WELCOLME to the WORLD of mobile")
class brand:
    def bran(a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("YOUR first brand is ",a)
            print("YOUR seconf brand is ",b)
            print("YOUR thired brand is ",c)
        elif a!=None and b!=None:
            print("YOUR first brand is ",a)
            print("YOUR seconf brand is ",b)
        elif a!=None:
            print("YOUR brand is ",a)
       
obj2=brand
def b():
     d=int(input("ENTER the number of brands you will select "))
     print()
     print("EXAMPLE 1 ,2 ,3 ")
     if (d==1):
         obj2.bran(a=input("ENTER a brand "))
     elif (d==2):
         obj2.bran(a=input("ENTER first brand "),b=input("ENTER second brand "))
     elif (d==3):
         obj2.bran(a=input("ENTER first brand "),b=input("ENTER second brand "),c=input("ENTER thired brand "))
     else:
         print("maximum 3 brands only ")
         b()
b()
obj=mobile()
class fea:
     you="YOUTUBR"
     def feature(self):
         print("AVALIABLE features")
         print("1.LONG time battery")
         print("2. hear music")
         print("3. youtube")
         print("4. download apps")

         print("5. play games")  
f=fea()
f.feature()
class batt(fea):
     b=100
     mu="SPOTIFY"
     def battery(self,b):
          print("your battery percentage is "+ str(self.b))
ba=batt()
class mus(batt):
    def music(self):
        f=int(input("PRESS 1 to know about music feature "))
        if (f==1):
             print()
             print("YOU can use "+str(self.mu)+" for MUSIC ")
        else:
            print("press a valid key ")
            music()
m=mus()
class you(fea):
    def youtube(self):
        print("WE have  ",self.you," as INBUILT")
y=you()
class dow:
    def download(self):
        print("you can download any app ")
        print("EXAMPLE")
        c=input("ENTER a app name that you want to download ")
        if c!=None:
            print(c," INSTALED successfully")
        else:
            print("enter a valid app")
            download()
d=dow()
class gam:
    def game(self):
        v=int(input("PRESS 1 to play game "))
        if (v==1):
            print("SORRY this is demo phone")
            print("PURCHASE your one mobile and play games")
        else:
            print("ENTER a valid key")
            game()
g=gam()
b=int(input("SELECT the option whuch you want to know EXAMPLE 1,2,3.. "))
def op():
    if (b==1):
        ba.battery()
    elif (b==2):
        m.music()
    elif (b==3):
        y.youtube()
    elif (b==4):
        d.download()
    elif (b==5):
        g.game()
    else:
        print("ENTER a valid key")
        op()
op()          
          
     
        
