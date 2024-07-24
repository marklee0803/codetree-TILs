n = input()
cnt_ee = 0
cnt_eb = 0
for i in range(len(n)-1):
    if n[i] == n[i+1] == e:
        cnt_ee +=1 
    if n[i] == e and n[i+1] == b:
        cnt_eb += 1

print(cnt_ee, cnt_eb)