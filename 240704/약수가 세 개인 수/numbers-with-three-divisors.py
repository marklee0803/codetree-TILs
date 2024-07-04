temp = input().split()
start, end = int(temp[0]), int(temp[1])
cnt = 0
for i in range(start,end+1):
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
print(cnt)