n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1+(i+1)*j,end=' ')
    print()