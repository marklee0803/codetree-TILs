n = int(input())
for i in range(11, 11+ 2*(n-1)+ 1, 2):
    for j in range(0, 2*(n-1)+1, 2):
        print(i+j,end=' ')
    print()