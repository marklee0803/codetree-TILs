arr = list(map(int, input().split()))
for i in range(3, 11):
    arr.append(arr[-1]+arr[-2])

for elem in arr:
    if elem < 10 :
        print(elem,end=' ')
    elif elem < 100:
        print(elem-10,end=' ')
    elif elem < 1000:
        print(elem-100,end=' ')