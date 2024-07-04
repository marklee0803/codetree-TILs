n = int(input())
for i in range(n):
    temp = input().split()
    a , b = int(temp[0]),int(temp[1])
    sum = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            sum += j
           

    print(sum)