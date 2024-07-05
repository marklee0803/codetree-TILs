n = int(input())

arr = list(map(int, input().split()))   

even_arr = []
for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)

new_arr = even_arr[::-1]
for value in new_arr:
    print(value,end=' ')