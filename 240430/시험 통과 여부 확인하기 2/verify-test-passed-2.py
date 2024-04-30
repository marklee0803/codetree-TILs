arr = list(map(int, input().split()))
cnt = 0

sum = 0
for i in range(4):
    sum += int(arr[i])
sum /= 4

for i in range(lent(arr)):
    if sum >= 60 :
         print('pass')
         cnt += 1
    else:
         print('fail')


print(len(arr),cnt)