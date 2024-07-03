n = int(input())
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(1 + n*(i+1) + j,end='')
        print()
    else:
        for j in range(n):
            print(2 * n + n*(i+1) - j,end='')
        print()