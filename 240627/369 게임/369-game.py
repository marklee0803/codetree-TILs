n = input()
for i in range(1, int(n)+1 , 1):
    if (i =='3' or '6' or '9' in i) or int(n) % 3 == 0  :
        print(0, end=' ')
    else: 
        print(i, end=' ')