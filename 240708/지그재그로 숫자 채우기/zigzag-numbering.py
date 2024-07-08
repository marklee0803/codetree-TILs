temp = input().split()
n , m = int(temp[0]), int(temp[1])

arr = [[0 for i in range(m)] for i in range(n)]

cnt = 0 
for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            arr[j][i] = cnt 
            cnt += 1 
        else:
            arr[n-j-1][i] = cnt
            cnt += 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()