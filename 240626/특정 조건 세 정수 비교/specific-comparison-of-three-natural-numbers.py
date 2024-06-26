temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

if a <= b and a <= c : 
    print(1,end=' ')
else: 
    print(0, end=' ')

if a == b and a ==c and b ==c :
    print(1)
else: 
    print(0)