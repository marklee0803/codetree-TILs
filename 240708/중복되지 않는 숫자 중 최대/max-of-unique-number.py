n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
cnt = True
for i in range(0, n-1):
    if arr[i] != arr[i+1]:
        print(arr[i])
        cnt = False
    else:
        continue
if cnt == True:
    print('-1')