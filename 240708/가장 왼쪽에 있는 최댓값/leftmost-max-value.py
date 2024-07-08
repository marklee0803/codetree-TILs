n  = int(input())
arr = list(map(int, input().split()))

max_arr = arr[0]

k = n
while k == 0:
    for elem in arr[:k]:
        if elem > max_arr :
            max_arr = elem
            k = arr.index(max_arr)
            print(arr.index(max_arr),end=' ')