arr = [list(map(int,input().split())) for i in range(2)]
sum1 = 0
sum2 = 0 
sum3 = 0

for i in range(2):
    print(f'{sum(arr[i])/4:.1f}',end=' ')
print()


for i in range(4):
    sum = 0
    for j in range(2):
        sum += arr[j][i]
        
    print(f'{sum/2:.1f}',end=' ')
print()

stotal_sum = 0
for i in range(2):
    total_sum += sum(arr[i])
    
print(f'{total_sum/8:.1f}')