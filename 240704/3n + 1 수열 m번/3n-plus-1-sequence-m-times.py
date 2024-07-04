m = int(input())
cnt = 0
for i in range(m):
    n = int(input())
    cnt += 1 
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1 
print(cnt)