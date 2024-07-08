n  = int(input())
arr = list(map(int, input().split()))



k = n+2
while True:
    max_arr = arr[0]
    for elem in arr[:k-1]:
        if elem > max_arr :
             max_arr = elem
    k = arr.index(max_arr) 
    print(k + 1,end=' ')

    if k == 0:
        break