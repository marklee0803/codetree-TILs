cnt = 0
sum = 0
for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        sum += i
        cnt += 1
print(f'{sum} {sum/cnt}')