inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

for i in range(a, b+1) :
  if a % 2 == 1 :
     a *= 2 
  else : 
     a += 3
  print(a,end=' ')