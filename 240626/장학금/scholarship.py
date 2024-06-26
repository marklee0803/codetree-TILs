temp = input().split()
j = int(temp[0])
g = int(temp[1])

if j >= 90 and g >= 95 :
    print('100000')
elif j >= 90 and g >= 90: 
    print('50000')
else: 
    print(0)