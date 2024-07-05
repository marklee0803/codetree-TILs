n = int(input())
arr = []
cnt = 0
i = 1
while  True:
    if cnt == 2 :
        break
    arr.append(i*n)
    i += 1
    if i*n % 5 == 0:
        cnt += 1
    if cnt == 2 :
        break


for elem in arr:
    print(elem,end=' ')