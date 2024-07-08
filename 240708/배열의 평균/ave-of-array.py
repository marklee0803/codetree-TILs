arr = [list(map(int,input().split())) for i in range(2)]
sum1 = 0
sum2 = 0 
sum3 = 0

for i in range(4):
    print(f'{sum(arr[i])/2:.1f}')
sum = 0
for i in range(2):
    for j in range(4):
        sum += arr[j][i]
        print(f'{sum(arr[j][i])}/4')
    print(f'{sum/4:.1f}')

sum2 = 0
for i in range(4):
    sum2 += arr[i]
print(f'{sum2/8:.1f}')