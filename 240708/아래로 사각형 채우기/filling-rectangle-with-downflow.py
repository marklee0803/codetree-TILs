n = int(input())
arr = [[0 for i in range(n)]for i in range(n)]


for i in range(n):
    num = 0
    for j in range(n):
        arr[i][j] = i+1 + num 
        num += n

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()