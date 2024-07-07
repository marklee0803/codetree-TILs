temp = input().split()
n, p = int(temp[0]), int(temp[1])
arr = list(map(int, input().split()))
temp2 = input().split()
a = int(temp2[1])
temp3 = input().split()
b = int(temp3[1])
temp4 = input().split()
s ,e = int(temp[1]) , int(temp[2])

print(arr[a-1])
print(index(b)+1)
for elem in arr[s:e+1]:
    print(elem, end=' ')