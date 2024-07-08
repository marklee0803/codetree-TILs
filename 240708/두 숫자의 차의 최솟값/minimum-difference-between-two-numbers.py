n = int(input())
arr = list(map(int, input().split()))
new_arr = []
for i in range(n-1):
    for j in range(n-1):
        if j > i :
            a = arr[j] - arr[i]
            new_arr.append(a)


min_arr = new_arr[0]

for elem in new_arr:
    if elem< min_arr:
        min_arr = elem
print(min_arr)