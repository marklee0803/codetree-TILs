n = int(input())
arr = []
cnt = 0
i = 1
while  True:
    
    arr.append(i*n)
    if cnt == 2 :
        break
    if i*n % 5 == 0:
        cnt += 1
    
    i += 1
    
  
    


for elem in arr:
    print(elem,end=' ')