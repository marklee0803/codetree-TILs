arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if value % 3 == 0:
        break
    else:
        cnt += 1
print(arr[cnt])