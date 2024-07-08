n = int(input())
arr = list(map(int, input().split()))
new_arr = []

while True:
    if n == 1 :
        print(arr)
        break
    for i in range(n-1):
        for j in range(n):
            if i < j:

                 a = arr[j] - arr[i]
                 new_arr.append(a)
          


max_arr = 0



for elem in new_arr:
    if max_arr < elem:
        max_arr = elem
if max_arr>0:
    print(max_arr)
else:
    print(0)