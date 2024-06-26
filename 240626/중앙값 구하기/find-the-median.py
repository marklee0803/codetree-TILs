temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

if a >= b:
    if b>=c:
        print(b)
    else: 
        print(c)
else: 
    if b<=c: 
        print(b)
    elif c <=a :
        print(a)
    else: 
        print(c)