arr = list(map(int, input().split()))
sum = 0
cnt = 0
for value in arr:
    if value == 0:
        break
    sum += value
    cnt += 1
print(f'{sum} {sum/cnt:.1f}')