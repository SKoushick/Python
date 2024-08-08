concept=input('enter the concept you need to see:')
if concept=='working days':
    class Work:
        def days(self):
            working_days =int(input("Enter the total number of Working days:"))
            absent_days=int(input("Enter the total number of days absent:"))
            absent_percentage=((1-absent_days/working_days)*100)
            print(absent_percentage)
            if(absent_percentage>75):
                print("You can write your exam")
            else:
                print("Sorry, you can't write this exam")
    a=Work()
    a.days()
elif concept=='grade':
    class Grade:
        def marks(self):
            A=int(input("enter the number"))
            if A<25:
                print("D -grade")
            elif A>25 and A<40:
                print("C -grade")
            elif A>40 and A<50:
                print("B -grade")
            elif A>50 and A<60:
                print("B+ -grade")
            elif A>60 and A<80:
                print("A -grade")
            else :
                print("A+ -grade")
    b=Grade()
    b.marks()
elif concept=='bonus':
    class Experience:
        def bonus(self):
            bonus1=0.10
            bonus2=0.08
            bonus3=0.05
            salary=int(input("enter the amount:"))
            experience=int(input("enter your experience:"))
            if experience>10:
                a=(salary*bonus1)
                salary= salary+a
                print(salary)

            elif experience>=6 and experience<=10:
                b=(salary*bonus2)
                salary=salary+b
                print(salary)

            elif experience<6:
                c=(salary*bonus1)
                salary= salary+c
                print(salary)
    c=Experience()
    c.bonus()    
elif concept=='discount':
    class Bonus:
        def markprice(self):
            b1=0.20
            b2=0.15
            b3=0.10
            markedprice=int(input("enter the price:"))
            if  markedprice>10000:
                a=(markedprice*b1)
                markedprice=markedprice+a
                print("the price is",markedprice)
            elif  markedprice>7000 and markedprice<=10000:
                a=(markedprice*b2)
                markedprice=markedprice+a
                print("the price is",markedprice)
            elif  markedprice<=7000:
                a=(markedprice*b3)
                markedprice=markedprice+a
                print("the price is",markedprice)
    d=Bonus()
    d.markprice()
elif concept=='percent':
    class Category:
        def percent(self):
            mark=int(input("enter the year"))
            if(mark<40):
                print("failed")
            elif(mark>=40 & mark<55):
                print("fair")
            elif(mark>=55 & mark<65):
                print("good")
            elif(mark>=65):
                print("excellent")

    e=Category()
    e.percent()
elif concept=='triangle':
    class Tri:
        def triangle(self):
            x=int(input("enter the number:"))
            y=int(input("enter the number:"))
            z=int(input("enter the number:"))
            if x == y == z:
                print("Equilateral Triangle")
            elif x == y or y == z or z == x:
                print("Isosceles Triangle")
            else:
                print("Scalene Triangle")
    f=Tri()
    f.triangle()
elif concept=='multiple':
    class Mul:
        def mulitple(self):
            a=int(input("enter the value"))
            b=int(input("enter the value"))
            print(a*b)
    g=Mul()
    g.multiple()
elif concept=='gender':
    class Gen:
        def maleorfemale(self):
            age=int(input("enter your age:"))
            gender=input("enter your gender:")
            if age>=18 and age<30:
                if gender=="Male" or "male":
                    print("your daily wage is 700")
                else:
                    print("your daily wage is 750")
            elif age>=30 and age<=40:
                if gender=="Male" or "male":
                    print("your daily wage is 800")
                else:
                    print("your daily wage is 850")
    h=Gen()
    h.maleorfemale()
elif concept=='every concept':
    class Everything(Mark,Grade,Gen,Mul,Bonus,Experience,Tri,Category):
        def all(self):
            self.maleorfemale()
            self.multiple()
            self.triangle()
            self.percent()
            self.bonus()
            self.markprice()
            self.marks()
            self.days()
    i=Everything()
    i.all()

