temp = input().split()
a = int(temp[0])
b = int(temp[1])
for i in range(1, 10):
    for j in range(b, a-1, -2):
        print(f'{j} * {i} = {j*i}',end=' ')
        if j > a : 
            print('/',end=' ')
    print()