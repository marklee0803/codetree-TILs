cnt = 0
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if i>j :
            print(' ',end=' ')
        else:
            cnt += 1
            print(cnt,end=' ')
            
            if cnt == 9:
                cnt = 0
    print()