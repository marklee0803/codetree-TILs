n = int(input())
arr = list(map(int, input().split()))
cnt = 0
k = 0
for elem in arr:
    k += 1
    if elem == 2:
        cnt += 1
    if cnt == 3:
        break

print(k)