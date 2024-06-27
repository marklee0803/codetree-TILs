import random
n = int(input())
for i in range(n):
    a = int(input())
    
    if a % 2 == 1 or a % 3 == 0 :
        print(a)