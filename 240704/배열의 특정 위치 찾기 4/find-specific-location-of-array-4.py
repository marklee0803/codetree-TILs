arr = list(map(int, input().split()))
sum = 0
for value in arr:
    if value == 0:
        break
    if value % 2 == 0:
        sum += value
print(sum)