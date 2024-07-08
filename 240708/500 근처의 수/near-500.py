arr = list(map(int, input().split()))
max_arr = []
min_arr =  []

for elem in arr:
    if elem>500:
        max_arr.append(elem)
    else:
        min_arr.append(elem)

a = 500
b = 500

for elem in max_arr:
    if elem > a:
        a = elem
print(a,end=' ')

for elem in min_arr:
    if elem < b :
        b = elem
print(b)