arr = list(map(int, input().split()))
sum = 0
cnt = 0
for value in arr:
    if value == 0:
        break
    if value % 2 == 0:
        sum += value
        cnt += 1
print(cnt, sum)