cnt = 9
n = int(input())
for i in range(n):
    for i in range(n):
        print(cnt,end='')
        if cnt == 1:
            cnt = 10
        cnt -= 1
    print()