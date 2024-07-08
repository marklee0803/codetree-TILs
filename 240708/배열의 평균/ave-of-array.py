arr = [list(map(int,input().split())) for i in range(2)]
sum1 = 0
sum2 = 0 
sum3 = 0

for i in range(2):
    print(f'{sum(arr[i])/4:.1f}')
sum = 0
for i in range(4):
    for j in range(2):
        sum += arr[j][i]
        
    print(f'{sum/2:.1f}')

sum2 = 0
for i in range(2):
    sum2 += sum(arr[i])
print(f'{sum2/8:.1f}')