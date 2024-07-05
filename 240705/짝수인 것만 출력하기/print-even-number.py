n = int(input())
arr = list(map(int , input().split()))
new_arr = []
for elem in arr:
    if elem % 2 == 0:
        new_arr.append(elem)
for value in new_arr:
    print(value,end=' ')