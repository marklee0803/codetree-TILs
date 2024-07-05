cnt_arr = [0]*10
arr = list(map(int, input().split()))
for elem in arr:
    for i in range(1, 9):
        if elem // 10 == i :
            cnt_arr[i] += 1
    
for i in range(1,10):
    print(f'{i} - {cnt_arr[i]}')