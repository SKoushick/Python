dct={}
command=input("enter the command:")
if command=="add contact":
    t=int(input("enter the num of conatcts must be added:"))
    for i in range(t):
        a=int(input("enter the value:"))
        b=input("enter your name:")
        dct[b]=a
    print(dct)
    comment=input("enter the comment:")
    if comment =="del":
        dct.pop(b)
        print(dct)
