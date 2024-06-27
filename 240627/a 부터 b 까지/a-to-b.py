temp = input().split()
a = int(temp[0])
b = int(temp[1])
while a <= b:
    if a %2 == 1:
        a *= 2
    else: 
        a+=3