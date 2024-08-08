

##user_age=20 #variable
##
##
##print(type(user_age)) #int
##
##user_name='Praveen' 
##
##print(type(user_name)) #str
##
##value=15.7
##
##print(type(value)) #float
##
##
##a=10
##b=20
##c='a+b'
##print(len(c))


##player_name='Dhoni' ##str
##player_age=42
##player_runs="100"
##
##print(type(player_name)) #str
##print(type(player_age)) #int
##print(type(player_runs)) #str


##mark=75
##mark1=50
##
##print("Your Tamil Mark is:",mark)



##print("\tImagecon Academy\nThe next generation Training")
##
####print(mark, "\n" ,mark1)
##
##print(10+20) #30 addition
##
##print("ten"+"\ntwenty") #concatination

##1.Arithmetic Operator
##a=7
##b=2
##
##print(a+b) ##9
##print(a-b) #5
##print(a*b) #14
##print(a/b) #3.6
##print(a%b) #1
##print(a**b) #49
##print(a//b) #3

#2.Assignment 
##c=25
##c+=b  #c=c+b
##print(c) 
##
##
##d-=num  #d=d-num

##a=10

#3.Comparison Operator (or) Relational


##x=10
##y=12
##
##print(x==y) #equal to
##print(x!=y) #not equal to
##print(x<y) #less than
##print(x>y) #greater than
##print(x<=y) #less than or equal to
##print(x>=y) #greater than or equal to

#user input
##age=eval(input('Enter you age:'))
##
##print(type(age))
##
##print(age>18)


#1.And operator
##a=18
##
##print(a>18 and a<=18) #False
##
###2.OR
##age=22
##print((age==20 or age>20) or a>18)
##
##
###3.Not operator
##
##print (not(a>18 and a<=18))
##
##a=True
##print(not(a))


##print('pa' in 'apple') #F
##
##a=13
##b=22
####print(a&b) #and
####
####print(a|b) ##or
####
####print(a^b) ##xor
##
##c=a<<1 #left shift
##d=a>>1 #right shift
##
##print(c,d)

##a=10
##if(a==10):
##    print(a)
##    print(a)
##    print(a)
##    print(a)
##
##
##print(20)


##age=int(input('Enter Your age'))
##
##if(age>18):
##    print("You are eligible")
##else:
##    print('You are not eligible')

##
##num=int(input('Enter your Number: '))
##if(num>0):
##    print('positive')
##elif(num==0):
##    print('neutral')
##elif(num<0):
##    print('Negative')

##views=2000
##if(views==1000):
##    print('1k views')
##elif(views==1300):
##    print('1.3 k')
##elif(views==2000):
##    print('2 k')
##else:
##    print('ENter correct views')

#4.nested if statement

##if(degree=='BE'):
##    print('I need more details')
##    if(p_out==2022):
##        print('You are eligible')
##        if(arrears==0):
##            print('eligible')
##    else:
##        print('Passed out not eligible')
##else:
##    print('Your degree is not eligible')


##num=int(input('Enter your number: '))
##if(num>0):
##    print('positive')
##    if(num%2==0):
##        print('Even')
##    else:
##        print('Odd')
##elif(num==0):
##    print('Neutral')
##else:
##    print('Negative')

#infinity
##num=0 #initialize
##
##while(True): #condition
##    print(num,end=',') #statment
##    num+=2 #increment or decrement
##    
##print('The program is end')

#finite loop or Traversing

##for i in range(-10,1):
##    print(i,end=',')

##i=10
##while(i>=1):
##    print(i)
##    i-=1
##name='Python Programming '
##
##for i in name:
##    print(i)


##name='DineshKumar'
##for i in name:
##    if(i=='K'):
##        break
##    print(i,end=' ')
 
##name='DineshKumar'
##for i in name:
##    if(i=='K'):
##        continue
##    print(i,end=' ')  
##    
##name='DineshKumar'
##for i in name:
##    if(i=='K'):
##        pass
##        print('First name was End')
##    print(i,end=' ')

##for i in range(1,7):
##    if(i<=3):
##        print(i,end=', ')
##    else:
##        print(i)


a=[10,11,'tamil',10,23.5,12,45,43]

##print(type(a))
##
##for i in a:
##    print(i)
##    
####positve index
##print(a[4]) #23.5
###negative index
##print(a[-4])
#slicing

##print(a[1:6])
##
##print(a[1:])
##
##print(a[:6])

##print(a[-7:-4])

##m=[10,20,30,40,70,80]
####print(len(m))
####print(sum(m))
####print(max(m))
####print(min(m))
####del(m)
####print(m)
##m.append(10)
##print(m)
##n=[22,23]
##m.extend(n)
##print(m)
##m.insert(2,21)
##print(m)
##m.reverse()
##print(m)
##m.sort()
##print(m)
##m.remove(10)
##print(m)

#without using sum function
##s=[20,2,3]
##c=0
##for i in s:
##    c+=i
##
##print('The sum is',c)
##    
###without using len function
##s=[20,2,3]
##c=0
##for i in s:
##    c+=1
##
##print('The len is',c)

##a=1,2,3
##print(type(a))








