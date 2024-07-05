arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
cnt_arr = [0, 0 , 0, 0]
for i in range(1,4):
    for elem in arr+i:
        if elem[0] = 'Y' and elem[1] >= 37:
            cnt_arr[0] += 1
        
        elif elem[0]= 'N' and elem[1] >= 37:
            cnt_arr[1] += 1
        elif elem[0] = 'Y' :
            cnt_arr[2] += 1
        else:
            cnt_arr[3] += 1
for i in cnt_arr:
    print(i,end=' ')
for value in cnt:
    if value == 2:
        print('E')