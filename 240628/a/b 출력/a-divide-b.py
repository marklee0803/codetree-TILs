변수 = input()
변수2 = 변수.split(' ')
a = int(변수2[0])
b = int(변수2[1])

m = a % b 
str = 'm'
for i in range(20):
    n = (a//b)*10 % b
    str = str+'n'
print(str)