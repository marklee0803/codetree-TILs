n  = int(input())
cnt2 = 0
for i in range(n, 0 ,-1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0 :
            cnt += 1
    if cnt == 2 :
        cnt2 += 1
        print(i,end=' ')