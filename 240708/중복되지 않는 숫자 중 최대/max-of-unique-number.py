n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
found = False

for i in range(n-1):
    if arr[i] != arr[i+1]:
        print(arr[i])
        found = True
        break

if not found:
    print('-1')