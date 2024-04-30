arr = list(map(float,input().split()))
sum = 0
for i in range(8):
    sum += float(arr[i])
print(sum/8)