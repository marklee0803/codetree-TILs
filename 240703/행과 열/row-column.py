temp = input().split()
a = int(temp[0])
b = int(temp[1])
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i*j,end=' ')
    print()