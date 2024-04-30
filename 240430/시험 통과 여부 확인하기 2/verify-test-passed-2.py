학생수=int(input())


cnt = 0


for i in range(학생수):
    arr = list(map(int, input().split()))   
    
    if sum(arr)/4 >= 60 :
         print('pass')
         cnt += 1
    else:
         print('fail')


print(cnt)