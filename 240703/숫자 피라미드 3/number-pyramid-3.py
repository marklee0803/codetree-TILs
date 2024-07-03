n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+i*j,end=' ')
    print()