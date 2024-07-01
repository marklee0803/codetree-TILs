n = int(input())
m = 2*n - 1
for i in range(n):
    for k in range(i):
        print(' ',end=' ')

    for j in range(m-2*i):
        print('*',end=' ')

    print()