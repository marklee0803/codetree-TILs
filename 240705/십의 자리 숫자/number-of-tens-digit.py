cnt_arr = [0]*10
arr = list(map(int, input().split()))
for elem in arr:
    if elem == 0:
        break
    for i in range(1, 10):
        if elem // 10 == i and elem >= 10:
            cnt_arr[i] += 1
    
for i in range(1,10):
    print(f'{i} - {cnt_arr[i]}')