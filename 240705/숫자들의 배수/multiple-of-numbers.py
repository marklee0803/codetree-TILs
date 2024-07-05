n = int(input())
arr = []
cnt = 0
i = 1
while  True:
    
    arr.append(i*n)
    if cnt == 2 :
        break
        
    i += 1
    
    if i*n % 5 == 0:
        cnt += 1
    


for elem in arr:
    print(elem,end=' ')