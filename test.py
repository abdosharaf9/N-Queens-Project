# def fitness(chromosome):
#     print(chromosome)
#     # print([chromosome.count(queen)-1 for queen in chromosome])
#     horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
#     # print(horizontal_collisions)
#     # diagonal_collisions = 0

#     n = len(chromosome)
#     left_diagonal = [0] * 2*n
#     right_diagonal = [0] * 2*n
#     for i in range(n):
#         left_diagonal[i + chromosome[i] - 1] += 1
#         right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

#     diagonal_collisions = 0
#     for i in range(2*n-1):
#         counter = 0
#         if left_diagonal[i] > 1:
#             counter += left_diagonal[i]-1
#         if right_diagonal[i] > 1:
#             counter += right_diagonal[i]-1
#         diagonal_collisions += counter / (n-abs(i-n+1))
    
#     return int(maxFitness - (horizontal_collisions + diagonal_collisions)) #28-(2+3)=23


# -----------------------------------------------------------------------------------

# def fitness(solution):
#     n = len(solution)
#     diagonal_conflicts = 0
#     column_conflicts = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if solution[i] == solution[j]:
#                 # Queens are in the same column
#                 column_conflicts += 1
#             elif abs(solution[i] - solution[j]) == abs(i - j):
#                 # Queens are in the same diagonal
#                 diagonal_conflicts += 1
#     # Return the fitness score (maximum score is 0)
#     return maxFitness-(diagonal_conflicts + column_conflicts)

# -----------------------------------------------------------------------------------


# def fitness(solution):
#     n = len(solution)
#     conflicts = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             # Check if queens are in the same row, column, or diagonal
#             if solution[i] == solution[j] or abs(solution[i]-solution[j]) == abs(i-j):
#                 conflicts += 1
#     # Return the fitness score (maximum score is 0)
#     return maxFitness-conflicts

# -----------------------------------------------------------------------------------

def fitness(solution):
    n = len(solution)
    threats = 0
    for i in range(n):
        for j in range(i+1, n):
            # Check if queens are in the same row or diagonal
            if solution[i] == solution[j] or abs(solution[i]-solution[j]) == j-i:
                threats += 1
    # Return the fitness score (maximum score is n)
    return maxFitness - threats



maxFitness = 28

# print(fitness([3, 1, 2, 7, 5, 6, 4, 8]))
print(fitness([8, 4, 6, 5, 7, 2, 1, 3]))