n = int(input())
arr = list(map(int, input().split()))
max_arr = arr[0]
for elem in arr:
    if elem > max_arr:
        max_arr = elem

arr.pop(arr.index(max_arr))

second_max_arr = arr[0]
for elem in arr:
    if elem > second_max_arr:
        second_max_arr = elem

print(max_arr, second_max_arr)