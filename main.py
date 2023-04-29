from res.chromosomes import *
from random import *

POPULATION_SIZE = 200
MUTATION_PROBABILITY = 0.05
GENERATIONS_NUMBER = 1000

def fitness(chromosome, max_fitness):
    n = len(chromosome)
    conflicts = 0

    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i]-chromosome[j]) == abs(i-j):
                conflicts += 1

    return max_fitness-conflicts



if __name__ == "__main__":

    try:
        n = int(input("Please enter the number of queens (N) >>> "))

        if n != 2 and n != 3:
            max_fitness = (n * (n-1)) / 2
            population = [generate_chromosome(n) for _ in range(POPULATION_SIZE)]
            fitness_values = [fitness(chromosome, max_fitness) for chromosome in population]
            fittest_found = population[fitness_values.index(max(fitness_values))]
            generation = 0

            # while max_fitness not in fitness_values:
            while generation != GENERATIONS_NUMBER and max_fitness not in fitness_values:
                population = generate_population(POPULATION_SIZE, n, MUTATION_PROBABILITY, population, fitness_values, max_fitness)
                fitness_values = [fitness(chromosome, max_fitness) for chromosome in population]
                current_fittest = population[fitness_values.index(max(fitness_values))]
                if current_fittest > fittest_found:
                    fittest_found = current_fittest
                generation += 1

            if max_fitness in fitness_values:
                print(f"Solved in generation {generation}")
                solution = population[fitness_values.index(max_fitness)]
                print(f"Found solution = {solution}")
            else:
                print(f"No solution is found in {GENERATIONS_NUMBER} generations!!")
                print(f"Fittest found solution = {fittest_found}")


            # TODO: Remove this when using UI
            board = []
            for i in range(n): board.append(["x"] * n)
            for i in range(n): board[i][fittest_found[i]-1] = "Q"
            board.reverse()
            for row in board: print (" ".join(row))
        
        else:
            print(f"Sorry, the problem can't be solved when N = {n}")

    except TypeError:
        print("Please enter a valid number!!")