from random import *
from .parent_selection import *
from .crossovers import *
from .mutations import *

def generate_chromosome(size):
    return sample(range(1, size+1), size)



def generate_population(population_size, chromosome_size, mutation_probability, old_population, fitness_values, max_fitness):
    new_population = []
    
    for _ in range(int(population_size/2)):
        parent1 = roulette_wheel_selection(old_population, fitness_values, population_size)
        parent2 = roulette_wheel_selection(old_population, fitness_values, population_size)

        child1, child2 = two_point_crossover(parent1, parent2, chromosome_size)
        if random() < mutation_probability:
            child1 = replace_mutation(child1, chromosome_size)
        if random() < mutation_probability:
            child2 = replace_mutation(child2, chromosome_size)
        
        new_population.append(child1)
        new_population.append(child2)
    
    return new_population


