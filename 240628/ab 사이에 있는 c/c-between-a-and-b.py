temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])

satisfied = False
for i in range (a, b+1):
    if i % c == 0 :
        satisfied = True

if satisfied == True:
    print('YES')
else:
    print('NO')