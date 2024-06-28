변수 = input().split()
a = int(변수[0])
b = int(변수[1])


몫 = a // b 
for i in range(20):
   p = 10 * a % b 
   p *= 10 
   print(p)