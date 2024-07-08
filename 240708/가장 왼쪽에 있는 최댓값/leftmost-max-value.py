n  = int(input())
arr = list(map(int, input().split()))

max_arr = arr[0]

k = n
while k == 1:
    for elem in arr[:k+1]:
        if elem > max_arr :
            max_arr = elem
        k = arr.index(max_arr) + 1 
        print(k,end=' ')