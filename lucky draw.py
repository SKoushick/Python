import random
class Custom:
    def customer(self):
        a=[]
        b=int(input('enter the no of registered:'))
        for i in range(1,b+1):
            a.append(i)
        print(a)
        c=[]
        for j in range (1,11):
            c.append(random.randint(1,21))
        print(c)
        for k in range(len(a)):
            if k in c:
                print(k,'these can be given the gifts')
try:
    obj=Custom()
    obj.customer()
except:
    print('this program has an error')
else:
    print('these people are eligible for giving gifts')
