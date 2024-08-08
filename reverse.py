a='deeplearning'
b='aeiouAEIOU'
u=[]
for i in a:
    if i in b:
        u.append(i)
print(u)
u.reverse()
print(u)
for k in a:
    if k in b:
        a.replace(u)
print(a)
