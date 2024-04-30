arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
	if elem == 0:
		break
	cnt += 1
arr = arr[0:cnt]
print(sum(arr),sum(arr)/cnt)