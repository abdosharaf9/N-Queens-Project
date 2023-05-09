from random import *

def flip_mutation(chromosome: list[int], size: int) -> list[int]:
    """
    Flip Mutation chooses a random gene in the chromosome and flip it. If the gene is 0 it will be 1, and vice versa.
    """
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = 1 - chromosome[index]
    return chromosome


def flip_mutation_mask(chromosome: list[int], size: int) -> list[int]:
    """
    Generate a mask of 0s and 1s, then flip the chromosome according to it. If the mask ith gene is 1, the chromosome's
    ith gene will be flipped. the mask ith gene is 0, it won't change anything.
    """
    temp = [randint(0, 1) for _ in range(size)]
    # print(f"Temp chromosome = {temp}")
    for i in range(size):
        if(temp[i] == 1): chromosome[i] = 1 - chromosome[i]
    return chromosome
    

# Note: This method is used for decimal numbers!!!
def divide_mutation(chromosome: list[int], size: int) -> list[int]:
    """
    Choose a random gene in the chromosome and change its valur by dividing it by 2.
    """
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = int(chromosome[index] / 2)
    return chromosome


# Note: This method is used for decimal numbers!!!
def random_reset_mutation(chromosome: list[int], size: int) -> list[int]:
    """
    Choose a random gene and change its value by a value in the same range of chromosome values.
    """
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = randint(1, size)
    return chromosome


'''
binary_chromosome = [1, 0, 1, 0, 1, 1, 0, 1]
dicimal_chromosome = [1, 3, 5, 7, 8, 2, 4, 6]

print(f"Before = {binary_chromosome}, After = {flip_mutation(binary_chromosome, 8)}")

print("\n")

print(f"Before = {binary_chromosome}, After = {flip_mutation_randomly(binary_chromosome, 8)}")

print("\n")

print(f"Before = {dicimal_chromosome}, After = {divide_mutation(dicimal_chromosome, 8)}")

print("\n")

print(f"Before = {dicimal_chromosome}, After = {replace_mutation(dicimal_chromosome, 8)}")
'''

