temp1 = input().split()
temp2 = input().split()
temp3 = input().split()
ay = temp1[0]
at = float(temp1[1])
by = temp2[0] 
bt = float(temp2[1])
cy = temp3[0]
ct = float(temp3[1])


if ay == 'Y' and at >= 37:
    if by == 'Y' and bt >= 37: 
        print('E')
    else:
        if cy == 'Y' and ct >= 37: 
            print('E')
        else: 
            print('N')
else: 
    if (by == 'Y' and bt >= 37) and (cy == 'Y' and ct >= 37)
        print('E')
    else: 
        print('N')