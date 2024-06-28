변수 = input().split()
a = int(변수[0])
b = int(변수[1])


print(f'{a//b}.",end=''')
a %= b 
for i in range(20):
   a *= 10
   print(a//b, end='')
   a % = b