temp = input().split()
a = int(temp[0])
b = int(temp[1])
prod = 1
for i in range(a , b+1):
    prod *= i 
print(prod)