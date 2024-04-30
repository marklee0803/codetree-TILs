a = list(map(int, input().split()))

num = 0 
for i in a: 
 if i % 3 == 0:
    print(a[num-1])
    break
 num += 1