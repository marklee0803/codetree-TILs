n = int(input())
arr = list(map(float, input().split()))
sum = 0
for value in arr :
    sum += value
mean = sum/len(arr)
print(f'{mean:.1f}')
if mean >= 4.0 :
    print('Perfect')
elif mean >= 3.0:
    print('Good')
else:
    print('Poor')