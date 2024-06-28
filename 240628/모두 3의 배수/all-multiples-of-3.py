s = True
for i in range(5):
    n = int(input())
    if n % 3 != 0:
        s = False 
if s == True:
    print(1)
else:
    print(0)