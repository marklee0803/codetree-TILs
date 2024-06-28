a = int(input())
for i in range(a, 0, -1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    m = i // 8
    if m % 2 == 0:
        continue
    k = i % 7
    if k < 4 :
        continue
    print(i,end=' ')