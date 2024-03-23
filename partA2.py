faces = 6
dist = []
for i in range(1, faces + 1):
    row = []
    for j in range(1, faces + 1):
        row.append(i + j)
    dist.append(row)

print("Distribution of all possible combinations:")
for row in dist:
    print(row)
