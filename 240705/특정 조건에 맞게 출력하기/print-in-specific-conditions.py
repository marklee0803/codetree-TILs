arr = list(map(int, input().split()))
new_list = []
for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 1:
        new_list.append(elem+3)
    else:
        new_list.append(elem//2)

for value in new_list:
    print(value,end=' ')