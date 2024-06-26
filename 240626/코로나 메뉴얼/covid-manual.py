temp1 = input().split()
temp2 = input().split()
temp3 = input().split()
ay = temp1[0]
at = float(temp1[1])
by = temp2[0] 
bt = float(temp2[1])
cy = temp3[0]
ct = float(temp3[1])

if (ay == 'Y' and at >= 37) and (by == 'Y' and bt >= 37):
    print('E')
if (ay == 'Y' and at >= 37) and (cy == 'Y' and ct >= 37):
    print('E')
if (by == 'Y' and bt >= 37) and (cy == 'Y' and ct >= 37):
    print('E')