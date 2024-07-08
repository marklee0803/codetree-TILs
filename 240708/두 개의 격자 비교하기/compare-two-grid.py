temp = input().split()
n , m = int(temp[0]), int(temp[1])
arr1 = [list(map(int, input().split())) for _ in range(n)]
input()
arr2 = [list(map(int, input().split())) for _ in range(n)]
arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j] :
            arr[i][j] = 0
        else:
            arr[i][j] = 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()