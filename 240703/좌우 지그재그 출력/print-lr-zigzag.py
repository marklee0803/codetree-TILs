n = int(input())
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(1+8*i+j,end='')
        print()
    else:
        for j in range(n):
            print(8*(i+1)-j,end='')
        print()