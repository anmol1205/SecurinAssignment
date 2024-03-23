import numpy as np

def undoom_dice(Die_A, Die_B):
    """
    Transforms the dice to meet the given conditions while maintaining the sum probabilities.
    """
    # Calculate sum probabilities for Die A
    A_probabilities = np.zeros(6*len(Die_A)+1)
    A_probabilities[0] = 1  # Start with probability 1 for sum 0
    for i in range(len(Die_A)):
        temp = np.zeros(6*len(Die_A)+1)
        for j in range(1, 7):
            temp += np.roll(A_probabilities, j)
        A_probabilities = temp / 6
    
    # Calculate sum probabilities for Die B
    B_probabilities = np.zeros(6*len(Die_B)+1)
    B_probabilities[0] = 1  # Start with probability 1 for sum 0
    for i in range(len(Die_B)):
        temp = np.zeros(6*len(Die_B)+1)
        for j in range(1, Die_B[i]+1):
            temp += np.roll(B_probabilities, j)
        B_probabilities = temp / Die_B[i]
    
    # Transformation for Die A
    max_spot = min(4, max(Die_A))  # Maximum spot allowed for Die A
    new_Die_A = [max_spot] * 6
    
    # Transformation for Die B
    new_Die_B = [1] * 6  # Start with all faces having 1 spot
    for i in range(len(Die_B)):
        for j in range(6):
            if Die_B[i] == j + 1:
                new_Die_B[i] = Die_B[i]
    
    return new_Die_A, new_Die_B

# Input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Output
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
