temp1 = input().split()
temp2 = input().split()
ae = int(temp1[0])
am = int(temp1[1])
be = int(temp2[0])
bm = int(temp2[1])

if am  < bm : 
    print('B')
elif am > bm:
    print('A')
elif am == bm and ae > be :
    print('A')
else: 
    print('B')