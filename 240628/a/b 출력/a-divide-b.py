변수 = input().split()
a = int(변수[0])
b = int(변수[1])

m = a % b

for i in range(20):
   k = (a//b)*10 % b 
   k = 10 * k - b*k
   a = print('k',end='')
n = str(m)+str(a)