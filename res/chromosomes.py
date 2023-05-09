from random import *
from .parent_selection import *
from .crossovers import *
from .mutations import *

def generate_chromosome(size: int):
    """
    Generates new random chromosome using sample() function from random library.
    """
    return sample(range(1, size+1), size)



def generate_population(population_size: int, chromosome_size: int, mutation_probability: float, old_population: list[list[int]], fitness_values: list[list[int]]) -> list[list[int]]:
    """
    Generate new population using the old one and its fitness values. It iterates until the new population
    reaches the desired population size, But here it only iterates the half because in each iteration we
    produce two new childs. Steps of generating new childs are as following:
    1. Select the parents using Roulette Wheel Selection method.
    2. Make crossover between these parents using Two-Point Crossover.
    3. For each child generate a random number between 0 and 1 to know if we should mutate it or not.
    4. If the mutation will happen we use the Random Reset Mutation.
    5. Add these childs to the new popultaion.
    """
    new_population = []
    
    for _ in range(int(population_size/2)):
        parent1 = roulette_wheel_selection(old_population, fitness_values, population_size)
        parent2 = roulette_wheel_selection(old_population, fitness_values, population_size)

        child1, child2 = two_point_crossover(parent1, parent2, chromosome_size)
        if random() < mutation_probability:
            child1 = random_reset_mutation(child1, chromosome_size)
        if random() < mutation_probability:
            child2 = random_reset_mutation(child2, chromosome_size)
        
        new_population.append(child1)
        new_population.append(child2)
    
    return new_population


