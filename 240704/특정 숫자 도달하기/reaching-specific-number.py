arr = list(map(int, input().split()))
sum = 0 
cnt = 0
for i in range(len(arr)) :
    sum += arr[i] 
    cnt += 1
    if i >= 250:
        arr.pop(i)
print(f'{sum} {sum/cnt:.1f}')