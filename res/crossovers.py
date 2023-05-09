from random import *

def one_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose a random cut point and swap the parents' portion after the cut point.
    """
    point = randint(1, size-2)
    # print(f"Point = {point}")

    child1 = chromosome1[:point] + chromosome2[point:]
    child2 = chromosome2[:point] + chromosome1[point:]
    
    return child1, child2


def two_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose 2 random cut points and swap the parents' portion between those cut points.
    """
    points = sorted(sample(range(1, size), 2))
    point1 = points[0]
    point2 = points[1]
    # print(f"Point1 = {point1}, Point2 = {point2}")

    child1 = chromosome1[:point1] + chromosome2[point1:point2] + chromosome1[point2:]
    child2 = chromosome2[:point1] + chromosome1[point1:point2] + chromosome2[point2:]

    return child1, child2


def multi_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose n random cut points, where n is also a random number. It alternates between swapping the parents' portion
    between the points, or leave it as it is.
    """
    num_of_points = randint(1, size-2)
    points = sorted(sample(range(1, size), num_of_points))
    # print(f"Number of points = {num_of_points}, Points = {points}")
    child1 = chromosome1.copy()
    child2 = chromosome2.copy()

    for i in range(num_of_points-1):
        child1[points[i]:points[i+1]] = chromosome2[points[i]:points[i+1]]
        child2[points[i]:points[i+1]] = chromosome1[points[i]:points[i+1]]
    
    return child1, child2


def uniform_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Genrate a mask of 0s and 1s, and use it to know if we should swap genes or not. If the mask ith gene is 0,
    the ith gene in child 1 will be the ith gene in parent 2 and vice versa for child 2. If the mask ith gene
    is 1, the ith gene in child 1 will be the ith gene in parent 1 and the ith gene in child 2 will be the
    ith gene in parent 2.
    """
    mask = choices([0, 1], k=size)
    # print(f"Mask = {mask}")
    child1 = chromosome1.copy()
    child2 = chromosome2.copy()

    for i in range(size):
        if(mask[i] == 0):
            child1[i] = chromosome2[i]
            child2[i] = chromosome1[i]

    return child1, child2


def uniform_crossover_probability(chromosome1: list[int], chromosome2: list[int], size: int, crossover_probability: float) -> tuple[list[int], list[int]]:
    """
    It uses a probability to know if we should swap genes or not. We generate a random number between 0 and 1
    for each gene, and if it's less than crossover probability, the ith gene in child 1 will be the ith gene
    in parent 2 and vice versa for child 2. If the random number is bigger than crossover probability, the
    ith gene in child 1 will be the ith gene in parent 1 and the ith gene in child 2 will be the ith gene
    in parent 2.
    """
    child1 = chromosome1.copy()
    child2 = chromosome2.copy()
    
    for i in range(size):
        if random() < crossover_probability:
            child1[i] = chromosome2[i]
            child2[i] = chromosome1[i]
    
    return child1, child2


def three_parent_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> list[int]:
    """
    Generate a third chromosome with the same size and values range. If the ith gene in parent 1 equals the
    the ith gene in parent 2, the ith gene in the child will be the same as the parents. If the ith gene in
    parent 1 doesn't equal the the ith gene in parent 2, the ith gene in the child will be the ith gene in
    the temporary chromosome.
    """
    temp = choices([0, 1], k=size)
    # print(f"Temp chromosome = {temp}")
    child = []
    for i in range(size):
        if(chromosome1[i] == chromosome2[i]):
            child.append(chromosome1[i])
        else:
            child.append(temp[i])
    
    return child


# Note: This method is used for decimal numbers!!!
def three_parent_crossover_dicimal(chromosome1: list[int], chromosome2: list[int], size: int) -> list[int]:
    """
    Generate a third chromosome with the same size and values range. If the ith gene in parent 1 equals the
    the ith gene in parent 2, the ith gene in the child will be the same as the parents. If the ith gene in
    parent 1 doesn't equal the the ith gene in parent 2, the ith gene in the child will be the ith gene in
    the temporary chromosome.
    """
    temp = choices(range(1, size), k=size)
    # print(f"Temp chromosome = {temp}")
    child = []
    for i in range(size):
        if(chromosome1[i] == chromosome2[i]):
            child.append(chromosome1[i])
        else:
            child.append(temp[i])
    
    return child


# -----------------------------------------------------------------------------------
'''
chromosome1 = [1, 1, 0, 1, 0, 1, 1, 1]
chromosome2 = [0, 1, 0, 0, 1, 0, 0, 1]
print(f"chromosome1 = {chromosome1}\nchromosome2 = {chromosome2}\n")

# One point crossover:
print(f"One Point:-")
child1, child2 = one_point_crossover(chromosome1, chromosome2, 8)
print(f"Child1 = {child1}\nChild2 = {child2}\n")


# Two point crossover:
print(f"Two Point:-")
child1, child2 = two_point_crossover(chromosome1, chromosome2, 8)
print(f"Child1 = {child1}\nChild2 = {child2}\n")


# Multi Point crossover:
print(f"Multi Point:-")
child1, child2 = multi_point_crossover(chromosome1, chromosome2, 8)
print(f"Child1 = {child1}\nChild2 = {child2}\n")


# Uniform crossover:
print(f"Uniform:-")
child1, child2 = uniform_crossover(chromosome1, chromosome2, 8)
print(f"Child1 = {child1}\nChild2 = {child2}\n")


# Uniform crossover probability:
print(f"Uniform using probability:-")
child1, child2 = uniform_crossover_probability(chromosome1, chromosome2, 8, 0.3)
print(f"Child1 = {child1}\nChild2 = {child2}\n")


# Three parent crossover:
print(f"Three parent:-")
child = three_parent_crossover(chromosome1, chromosome2, 8)
print(f"Child = {child}")
'''