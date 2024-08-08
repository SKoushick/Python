class Start:
    def entry(self):
        print('you can choose the objects you need for your purupose')
        print('you can see what r all the products are there in the grocery and you can take it to the billing place')
class Products:
    def products(self):
        print('products available in the shop,,,,')
        print("product:bajji_mix,cost:150","\nproduct:saambar_mix,cost:130","\nproduct:chilli_powder,cost:160","\nproduct:everest,cost:199","\nproduct:denver,cost299","\nporduct:brut,cost:300","\nproduct:park_avenue,cost:299","\nproduct:magnet,cost:285","\nproduct:noodles,cost:40","\nproduct:grapes,cost:60","\nproduct:badam,cost:50","\n")
class Select(Products,Start):
    def selection(self):
        self.entry()
        self.products()
        su=0
        dict={'bajji_mix':150,'saambar_mix':130,'chilli_powder':160,'everest':199,'denver':299,'brut':300,'park_avenue':299,'magnet':285,'noodles':40,'grapes':60,'badam':50}
        lst=list(dict.keys())
        selected=input("enter the items youe choose:")
        no=int(input('total no of things'))
        for i in range(no):
            if selected in lst:
                su=su+dict[selected]
            elif selected=="over":
                break
            else:
                print('enter the given products shown')
        print("youre total bill is",su)
        yesorno=input('do want to continue.....?y or n:')
        how_many=int(input('enter the no of products you'))
        for i in range(how_many):
            if yesorno=="y":
                selected=input("enter the items youe choose:")
                no=int(input('enter the number of products you took'))
                for i in range(no):
                    if selected in lst:
                        su=su+dict[selected]
                    elif selected=="over":
                        break
                    else:
                        print('enter the given products shown')
                print("youre total bill is",su)
            else:
                print("thank you for coming to our shop see you again....")
try:
    obj=Select()
    obj.selection()
except:
    print('enter this program has a error')
else:
    print('billing is completed')
finally:
    print('so this is program is made up of oops concept')
