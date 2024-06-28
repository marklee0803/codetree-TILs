n = int(input())
cnt = 0
for i in range(1 , n+1):
    if n % 4 == 0 :
        cnt += 1
    if  n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        cnt -= 1
print(cnt)