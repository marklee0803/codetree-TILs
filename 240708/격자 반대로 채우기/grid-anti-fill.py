n = int(input())

cnt = 1 
arr = [[0 for i in range(n)] for i in range(n)]

a = 0
for i in range(n):
    for j in range(n):
        if a % 2 == 0 :

            arr[n-j-1][n-i-1] = cnt
            cnt += 1
           


        else:
            
            arr[j][n-i-1] = cnt
            cnt += 1
    a += 1
            

for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()