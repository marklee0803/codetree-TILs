n = int(input())
arr = [[0 for i in range(n)]for i in range(n)]

num = 0
for i in range(n):
    for j in range(n):
        arr[i][j] = i + num 
        num += 3 

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()