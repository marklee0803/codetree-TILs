n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0]*n

for i in arr:
    cnt_arr[i] += 1

for i in cnt_arr:
    print(i,end=' ')