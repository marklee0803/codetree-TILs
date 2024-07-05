n = int(input())
arr = [1, n]
while elem <= 100:
    arr.append(arr[-1]+arr[-2])

for value in arr:
    print(value,end=' ')