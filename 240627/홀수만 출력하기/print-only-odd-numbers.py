import random
n = int(input())
for i in range(n):
    a = int(input())
    
for i in range(1,n+1):
    if i % 2 == 1 or i % 3 == 0 :
        print(i)