n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0]*9

for i in range(n):
    cnt_arr[i] += 1

for i in cnt_arr:
    print(i)