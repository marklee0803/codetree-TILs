temp1 = input().split()
temp2 = input().split() 
aa = int(temp1[0])
ag = temp1[1]
ba = int(temp2[0])
bg = temp2[1]

if (aa >= 19 and ag == 'M') or (ba >=19 and bg == 'M'):
    print(1)