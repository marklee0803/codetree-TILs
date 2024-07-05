arr = list(map(int, input().split()))
cnt_arr = [0]*10
for elem in arr:
    if elem == 0:
        break
    cnt_arr[10-(elem//10)] += 1

for i in range(1, 11):
    print(f'{110 - 10 * i} - {cnt_arr[i-1]})