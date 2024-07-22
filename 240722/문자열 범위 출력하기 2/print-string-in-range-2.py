a = input()
b = int(input())
if b < len(a):
    print(a[-1:-1-b:-1])
else:
    print(a[::-1])