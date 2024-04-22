n = int(input())
i = 0
while i <= n:
    if i % 2 == 0 or i % 5 == 0 or (i % 3 == 0 and i % 9 != 0) :
        continue

    print(n) 
    i += 1