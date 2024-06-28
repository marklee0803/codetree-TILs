temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
c = True
for i in range(a, b+1):
    if i % c == 0:
        c = False
    
if c == True:
    print('YES')
else:
    print('NO')