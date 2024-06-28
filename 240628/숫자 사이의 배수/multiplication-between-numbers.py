temp = input().split()
a = int(temp[0])
b = int(temp[1])
sum = 0
for i in range(a, b+1):
    if i % 5 == 5 or i % 7 == 0:
        sum += i
print(sum)