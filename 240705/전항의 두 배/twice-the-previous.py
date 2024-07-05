arr = list(map(int, input().split()))
for _ in range(3,11):
    arr.append(2*arr[-2]+arr[-1])
for i in arr:
    print(i,end=' ')