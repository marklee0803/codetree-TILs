temp = input().split()
n1 , n2 = int(temp[0]), int(temp[1])
arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))
for elem in arr_n1:
    if elem == arr_n2[0]:
        a = arr_n1.index(elem)
        break
for i in range(n2):
    if arr_n2[i] == arr_n1[a+i]:
        print('Yes')
    else:
        print('No')