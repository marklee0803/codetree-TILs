n = int(input())
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(1 + 3 * n * (i// 2) + j, end=' ')
        else:
            print(n + 2 + 3 * n * (i - 1) // 2+ 2*j,end=' ')
    print()