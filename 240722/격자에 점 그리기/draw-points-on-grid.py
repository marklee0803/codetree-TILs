n , m = map(int, input().split())

placed = [[0 for _ in range(n)] for _ in range(n)]



k = 1
for _ in range(m):
    r , c = tuple(map(int, input().split()))
    placed[r-1][c-1] = k
    k += 1

for row in placed :
    for elem in row:
        print(elem, end=' ')
    print()