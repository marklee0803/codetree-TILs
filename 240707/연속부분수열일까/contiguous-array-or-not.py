temp = input().split()
n1, n2 = int(temp[0]), int(temp[1])
arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))

found = False

for i in range(n1 - n2 + 1):
    if arr_n1[i:i + n2] == arr_n2:
        found = True
        break

if found:
    print('Yes')
else:
    print('No')