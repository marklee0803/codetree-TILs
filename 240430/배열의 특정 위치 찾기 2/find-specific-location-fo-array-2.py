arr = list(map(int, input().split()))

n = len(arr)

sum_val1 = 0
for i in range(0, n, 2):
    sum_val1 += arr[i]


sum_val2 = 0
for i in range(1, n, 2):
    sum_val2 += arr[i]


if sum_val1 > sum_val2:
    print(sum_val1-sum_val2)
else: 
    print(sum_val2-sum_val1)