arr = [[0 for _ in range(6)] for _ in range(6)]
for i in range(1, 7):
    for j in range(1, 7):
        arr[i-1][j-1] = (i, j)
for r in arr:
    print(r)
