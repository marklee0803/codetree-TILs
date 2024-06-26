temp1 = input().split()
temp2 = input().split()
ae = int(temp1[1])
am = int(temp1[0])
be = int(temp2[1])
bm = int(temp2[0])

if am  < bm : 
    print('B')
elif am > bm:
    print('A')
elif am == bm and ae > be :
    print('A')
elif am == bm and ae < be: 
    print('B')