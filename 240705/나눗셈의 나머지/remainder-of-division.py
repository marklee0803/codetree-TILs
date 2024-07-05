temp = input().split()
a = int(temp[0])
b = int(temp[1])

cnt_arr = [0]*(b)


while a < 1:
    a = a % b
    print(a)
    for i in range(1, b):
        if a == i:
            cnt_arr[i] += 1

print(cnt_arr)