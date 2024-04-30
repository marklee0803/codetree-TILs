arr = list(map(int, input().split()))

a = list()
for elem in arr:
	if elem == 0:
	     break
         


even_arr = []
for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)
even_arr.remove(0)
print(len(even_arr),sum(even_arr))


arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

# 배열에 0이 있는지 확인합니다. 0이 나오지 않았을 경우 짝수의 개수와 합을 구합니다.
for elem in arr:
	if elem == 0:
		break
	if elem % 2 == 0:
		sum_val += elem
		cnt += 1

print(cnt, sum_val)