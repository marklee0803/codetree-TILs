변수 = input().split()
a = int(변수[0])
b = int(변수[1])


몫 = a // b 
for i in range(20):
   k = ((a % b) * 10 )// b 
   p = ((a % b) * 10 ) % b
   
   print(k)
   k = p