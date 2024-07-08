temp = input().split()
n , m = int(temp[0]) , int(temp[1])

arr = [[0 for i in range(m)] for i in range(n)]

num = 1 
for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num += 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()