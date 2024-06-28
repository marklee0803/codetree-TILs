변수 = input()
변수2 = 변수.split(' ')
a = int(변수2[0])
b = int(변수2[1])

m = a % b

for i in range(20):
   k = (a//b)*10 % b 
   k = 10 * k - b*k
   a = print('k',end='')
n = str(m)+str(a)