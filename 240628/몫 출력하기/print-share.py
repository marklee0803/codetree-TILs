k = 0
while True:
    n = int(input())
    if n % 2 == 1:
        continue
    else:
        m = n // 2
        print(m)
        k += 1
        if k == 3:
            break