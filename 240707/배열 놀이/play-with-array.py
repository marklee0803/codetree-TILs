temp = input().split()
n, q = int(temp[0]), int(temp[1])
arr = list(map(int, input().split()))

for _ in range(q):
    about_n = input().split()
    k = int(about_n[0])
    if k == 1:
        print(about_n[1])
    elif k == 2 :
        print(arr.index(int(about_n[1]))+1)
    elif k == 3:
        for elem in arr[int(about_n[1])-1:int(about_n[2])]:
            print(elem,end=' ')