
faces = 6
sum_freq = {}
for i in range(2, 13):
    sum_freq[i] = 0

for i in range(1, faces + 1):
    for j in range(1, faces + 1):
        sum_freq[i + j] += 1

total_combinations = faces ** 2

print("Probability of all possible sums occurring:")
for sum_val in range(2, 13):
    probability = sum_freq[sum_val] / total_combinations
    print(f"Sum: {sum_val}, Probability: {probability:.2f}")
