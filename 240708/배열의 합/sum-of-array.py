n = 4
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(4):
    print(sum(arr[i]))