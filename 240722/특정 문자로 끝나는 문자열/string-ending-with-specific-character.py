arr = [input() for i in range(10)]
b = input()

T = False
for i in range(10):
    if arr[i][-1] == b:
        print(arr[i])
        T = True
if T == False:
    print("None")