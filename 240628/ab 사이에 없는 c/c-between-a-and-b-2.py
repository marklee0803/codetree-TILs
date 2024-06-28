temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
w = True

for i in range(a, b+1):
    if i % c == 0:
        w = False
    
if w == True:
    print('YES')
else:
    print('NO')