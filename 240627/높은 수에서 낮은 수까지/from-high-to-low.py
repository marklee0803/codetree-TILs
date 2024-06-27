temp = input().split()
a = int(temp[0])
b = int(temp[1])
if a>= b:
    for i in range(a, b-1, -1):
        print(i,end=' ')
else:
    for i in range(b, a-1, -1):
        print(i, end=' ')