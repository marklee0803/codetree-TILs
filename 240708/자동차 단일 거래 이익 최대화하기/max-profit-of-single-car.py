n = int(input())
arr = list(map(int, input().split()))
new_arr = []
for i in range(n):
    for j in range(n):
         if i < j:

             a = arr[j] - arr[i]
             new_arr.append(a)



max_arr = new_arr[0]

for elem in new_arr:
    if max_arr < elem:
        max_arr = elem

print(max_arr)