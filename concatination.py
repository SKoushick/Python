##l=["hello","world"]
##print(l[0]+l[1])


##import random
##
##print(random.randint(0,100))
##

##
##j=[]
##k=int(input("Enter the range:"))
##for i in range(k):
##    j=int(input("Enter the values:"))
##def Search(l,n):
##    minval=l[0]
##    counter=1
##    while(counter<n):
##        v=l[counter]
##        if(v<minval):
##            minval=v
##            idx=counter
##        else:
##            pass
##        return minval,idx
##    
##
##def sortlist(l,n):
##    counter=0
##    while (coutner<n):
##        m,idx=Search(l,n)
##        l2.append(m)
##        del l[idx]
##        n=n-1
##    return l2
##    
##def main():
##    
##    Search(j,k)
##    sortlist(j,k)
##
##
##main()

##num=1234
##t=0
##for i in range(4):
##    if num>0:
##        t=t*10+num%10
##        num//=10
##    print(t)


##student details in a dictionary

def stud():
    D={}
    while(True):
        stuid=input("Enter student id:")
        stumark=(input("Enter the mark in row with comma seperated value:"))
        yorn=input("Enter yes/no if you want to add details of another student:")
        if stuid in D:
            print(stuid,"have already inserted")
        else:
            D[stuid]=stumark.split(",")
        if yorn.lower()=="no":
            return D
    print(D)

student_data=stud()

def avg(D):
    avgm={}
    for x in D:
        l=D[x]
        s=0
        for marks in l:
            s+=int(marks)
        avgm[x]=s/len(l)
    return avgm

Avg=avg(student_data)
for x in Avg:
    
    print("student",x,"has the average of",Avg[x ])
