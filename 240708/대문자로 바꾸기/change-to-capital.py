arr = [input().split() for _ in range(5)]
cnt = 65
for i in range(5):
    for j in range(3):
        arr[i][j] = chr(cnt)
        print(arr[i][j],end=' ')
        cnt += 1
    print()