arr = [input().split() for _ in range(5)]

for i in range(5):
    for j in range(3):
        arr[i][j] = chr(ord(arr[i][j]))
        print(arr[i][j],end=' ')
        cnt += 1
    print()