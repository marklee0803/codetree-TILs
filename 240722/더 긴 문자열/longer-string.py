temp = input().split()
a = temp[0]
b = temp[1]
if len(a) > len(b):
    print(a, len(a))
elif len(a) < len(b):
    print(b, len(b))
else:
    print('same')