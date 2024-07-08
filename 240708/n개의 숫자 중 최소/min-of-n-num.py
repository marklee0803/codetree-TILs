n = int(input())
arr = list(map(int, input().split()))
min_arr = arr[0]
for elem in arr[1:]:
    if elem < min_arr:
        min_arr = elem
print(min_arr,arr.count(min_arr))