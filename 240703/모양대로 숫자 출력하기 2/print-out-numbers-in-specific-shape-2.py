cnt = 1
n = int(input())
for i in range(n):
    for i in range(n):
        print(2*cnt,end=' ')
        if cnt == 4 :
            cnt = 0
        cnt += 1
    print()