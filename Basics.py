import cmath
#Arithmetic 

c=10
d=20
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
e=c+d
f=a+b
print(e,f)


#Greatest number

a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))
if(a>b & a>c):
    print("A is the greatest number..")
elif(b>a & b>c):
    print("B isw the greatest number..")
else:
    print("C is the greatest number..")
    
#Square root
sq_val=int(input("Enter the number need to be squared"))
print(sq_val**2)

#Quadratic Equation

a=int(input("enter the coefficiant of X^2:"))
b=int(input("Enter the coefficiant of X:"))
c=int(input("Enter the constant number:"))

dis=(b*b)-(4*a*c)
sol1=(-b-cmath.sqrt(dis))/(2*a)
sol2=(-b+cmath.sqrt(dis))/(2*a)
print("The first solution for the QEquation:",sol1)
print("The second solution for the QEquation:",sol2)

#Swaping
sample1=int(input("Enter the number1:"))
sample2=int(input("Enter the number2:"))
print("before:",sample1,sample2)
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("after",a,b)

swap(sample1,sample2)

#Random numbers
import random
print(random.randint(1,100))



#Kilometer to miles

km=int(input("Enter the kilometer:"))
print(km*1.6093)



#Celsius to fahrenheit
Cel=float(input("Enter the celsius:"))
Fh=Cel*(9/5)+32
print("Fahrenheit",Fh)

a=int(input("Enter the number:"))
if(a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("Zero")
    
