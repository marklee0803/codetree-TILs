cnt = 65
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(cnt+j,end='')
    print()