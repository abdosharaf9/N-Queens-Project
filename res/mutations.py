from random import *

def flip_mutation(chromosome, size):
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = 1 - chromosome[index]
    return chromosome


def flip_mutation_randomly(chromosome, size):
    temp = [ randint(0, 1) for _ in range(size) ]
    # print(f"Temp chromosome = {temp}")
    for i in range(size):
        if(temp[i] == 1): chromosome[i] = 1 - chromosome[i]
    return chromosome
    

def divide_mutation(chromosome, size):
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = int(chromosome[index] / 2)
    return chromosome


def random_reset_mutation(chromosome, size):
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

