cnt = 65
n = int(input())
for i in range(n):
    for j in range(n):
        if j<i:
            print(' ',end=' ')
        else:
            print(chr(cnt),end=' ')
            
            if cnt == 90:
                cnt = 64
            cnt += 1