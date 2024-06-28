temp = input().split()
a = int(temp[0])
b = int(temp[1])
s = False
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i ==0 :
        s = True
if s == True:
    print(1)
else:
    print(0)