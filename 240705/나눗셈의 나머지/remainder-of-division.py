temp = input().split()
a = int(temp[0])
b = int(temp[1])

cnt_arr = [0]*(b)

while a >1 :
    t = a // b
    k = a % b
    a = t 
    for i in range(0, b):
        if k == i:
            cnt_arr[i] += 1 
sum = 0

for i in cnt_arr:
    sum += i**2
print(sum)