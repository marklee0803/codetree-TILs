cnt = 65
n = int(input())
for i in range(n):
    for j in range(i+1):
        
        print(chr(cnt),end='')
        cnt += 1
        if cnt == 90:
            cnt = 65
    print()