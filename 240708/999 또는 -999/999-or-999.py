arr = list(map(int, input().split()))
arr.pop()
max_arr = arr[0]
for elem in arr:
    if elem > max_arr:
        max_arr = elem
min_arr = arr[0]
for elem in arr:
    if elem < min_arr:
        min_arr = elem
print(max_arr,min_arr)