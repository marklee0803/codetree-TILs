n = int(input())
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(1 + n*i + j,end=' ')
        print()
    else:
        for j in range(n):
            print(n*(i+1)- j,end=' ')
        print()