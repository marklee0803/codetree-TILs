temp = input().split()
h = int(temp[0])
w = int(temp[1])
b = 10000 * w / (h * h)
print("%d"%b)
if b > 25:
    print('Obesity')