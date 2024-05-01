b = int(input())

arr = list(map(int, input().split()))   

arr.sort()


even_arr = []
for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)

print(even_arr[::-1])