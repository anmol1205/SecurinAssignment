from itertools import combinations_with_replacement
import random

def generate_sets(numbers, size):
    sets = []
    for _ in range(size ** len(numbers)):
        current_set = []
        for _ in range(size):
            current_set.append(random.choice(numbers))
        sets.append(tuple(current_set))
    return set(sets)

def find_sums(s):
    sums = {}
    for pair in combinations_with_replacement(s, 2):
        s = sum(pair)
        sums[s] = sums.get(s, 0) + 1
    return sums

def undoom_dice(sets, distribution, tolerance=0.1):
    matching_sets = []
    for s in sets:
        sums = find_sums(s)
        if all(abs(sums.get(k, 0) - v) <= tolerance for k, v in distribution.items()):
            matching_sets.append(s)
    return matching_sets

set1_numbers = [1, 2, 3, 4]
set2_numbers = list(range(1, 12))
set_size = 6

set1 = generate_sets(set1_numbers, set_size)
set2 = generate_sets(set2_numbers, set_size)

desired_distribution = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
tolerance = 0.4

matching_sets_1 = undoom_dice(set1, desired_distribution.copy(), tolerance)
matching_sets_2 = undoom_dice(set2, desired_distribution.copy(), tolerance)

if matching_sets_1:
    print("Matching sets from set 1:")
    for s in matching_sets_1:
        print(s)

if matching_sets_2:
    print("Matching sets from set 2:")
    for s in matching_sets_2:
        print(s)
