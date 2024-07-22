arr = [input() for i in range(10)]
b = input()

for i in range(10):
    if arr[i][-1] == b:
        print(arr[i])
    else:
        print('None')