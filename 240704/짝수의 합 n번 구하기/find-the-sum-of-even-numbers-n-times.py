n = int(input())
for i in range(n):
    temp = input().split()
    a , b = int(temp[0]),int(temp[1])
    sum = 0
    for j in range(a, b+1, 2):
        if a % 2 == 0:
            sum += i 
        else:
            sum += i+1
    print(sum)