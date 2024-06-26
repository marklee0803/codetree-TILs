temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

if a >=b and a >=c :
    print(a)
elif b >= a and b>=c :
    print(b)
else: 
    print(c)