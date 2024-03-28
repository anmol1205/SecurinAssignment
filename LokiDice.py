from itertools import product, combinations

def count_occurrences(sum_count):
    counts = [0] * 11
    for i in range(2, 13):
        counts[i - 2] = sum_count.count(i)
    return tuple(counts)

def generate_sets_with_repetition(nums, size):
    sets_with_rep = list(product(nums, repeat=size))
    sets_with_1 = [s for s in sets_with_rep if 1 in s]
    return sets_with_1

def generate_sets_with_constraint(numbers, size, constraint):
    sets_no_rep = [{constraint} | set(comb) for comb in combinations(numbers - {constraint}, size - 1)]
    return sets_no_rep

def undoom_dice(sets_with_rep, sets_no_rep):
    satisfying_pairs = set()
    for rep_set, no_rep_set in product(sets_with_rep, sets_no_rep):
        sums = [sum(pair) for pair in product(rep_set, no_rep_set)]
        if all(2 <= s <= 12 for s in sums):
            sum_count = count_occurrences(sums)
            if sum_count == (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1):
                pair = (tuple(sorted(rep_set)), tuple(sorted(no_rep_set)))
                satisfying_pairs.add(pair) 
    print("Satisfying pairs are :")  
    for pair in satisfying_pairs:
        print(pair)
    
set_with_rep = generate_sets_with_repetition({1, 2, 3, 4}, 6)
set_no_rep = generate_sets_with_constraint({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 6, 1)

print("Generating satisfying pairs......")

undoom_dice(set_with_rep, set_no_rep)
print("Finished.")
