sum = 0
cnt = 0
while True:
    n = int(input())
    sum += n
    cnt += 1
    if n >= 30:
        break
print(f'{sum/cnt:.2f})