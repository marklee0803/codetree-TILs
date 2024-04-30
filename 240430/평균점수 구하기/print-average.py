arr = list(map(float,input().split()))
sum = 0
for i in range(8):
    sum += float(arr[i])
sum /= 8
print(f'{sum:.1f}')