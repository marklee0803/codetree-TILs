arr = list(map(int, input().split()))
sum = 0 
cnt = 0
new_list = []
for i in arr:
    if i <= 250:
        new_list.append(i) 
for i in new_list:
    sum += i
    cnt += 1
print(f'{sum} {sum/cnt:.1f}')