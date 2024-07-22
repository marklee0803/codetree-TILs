n = int(input())
count = 0
count2= 0
for i in range(n):
    a = input()
    b = len(a)
    count += b
    if i[0] == 'a':
        count2 += 1
print(count, count2)