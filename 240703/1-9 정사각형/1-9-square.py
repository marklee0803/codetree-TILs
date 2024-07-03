n = int(input())
cnt = 1
for i in range(n):
    for i in range(n):
        print(cnt,end='')
        if cnt == 9:
            cnt = 0
        cnt += 1
        
    print()