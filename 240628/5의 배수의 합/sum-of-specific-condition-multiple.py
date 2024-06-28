temp = input().split()
a = int(temp[0])
b = int(temp[1])
sum = 0 
if a <= b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum += i
else:
     for i in range(b , a+1):
        if i % 5 == 0:
            sum += i
print(sum)