n = int(input())
for i in range(n):
    temp = input().split()
    a , b = int(temp[0]), int(temp[1])
    
    s = 1
    for i in range(a, b+1):
        s *= i
    print(s)