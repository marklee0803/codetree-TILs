temp = input().split()
start , end= int(temp[0]), int(temp[1])

cnt2 = 0
for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += j
            
    if cnt == i :
        cnt2 += 1
print(cnt2)