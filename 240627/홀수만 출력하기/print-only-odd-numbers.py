n = int(input())
print(n)
for i in range (n):
    random.randrange(n)
for i in range(1,n+1):
    if i % 2 == 1 or i % 3 == 0 :
        print(i)