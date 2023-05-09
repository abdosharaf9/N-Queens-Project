from random import *

def roulette_wheel_selection(population: list[int], fitness_values: list[int], population_size: int) -> list[int]:
    """
    Roulette Wheel is a Parent Selection technique. The chromosome is selected according to its fitness probability.
    The wheel position is generated as a random number between 0 and 1, because we are dealing with probabilities.
    """
    fitness_sum = sum(fitness_values)
    fitness_probs = [(fitness / fitness_sum) for fitness in fitness_values]
    wheel_position = uniform(0, 1)
    comulative_prob = 0

    for i in range(population_size):
        comulative_prob += fitness_probs[i]
        if comulative_prob >= wheel_position:
            return population[i]
        

# -----------------------------------------------------------------------------------

def tournament_selection():
    pass

# -----------------------------------------------------------------------------------
def rank_selection():
    pass

# -----------------------------------------------------------------------------------
def boltzmann_selection():
    pass

# -----------------------------------------------------------------------------------
def random_selection():
    pass

# -----------------------------------------------------------------------------------
def stochastic_universal_sampling():
    pass