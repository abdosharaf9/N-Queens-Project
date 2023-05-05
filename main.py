from res.chromosomes import *
from random import *
from ui.final_UI import *

POPULATION_SIZE = 200
MUTATION_PROBABILITY = 0.05
GENERATIONS_NUMBER = 1000


#Main Screen
win = Screen()
win.title("N-Queen Problem")
win.bgcolor("#dfe6dc")
win.setup(600,600)
win.tracer(0)
win.setworldcoordinates(0,0,600,600)


def fitness(n, chromosome, max_fitness):
    conflicts = 0

    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i]-chromosome[j]) == abs(i-j):
                conflicts += 1

    return int(max_fitness-conflicts)


if __name__ == "__main__":

    try:

        n = sc1(win)

        if n != 2 and n != 3:
            max_fitness = (n * (n-1)) / 2
            population = [generate_chromosome(n) for _ in range(POPULATION_SIZE)]
            fitness_values = [fitness(n, chromosome, max_fitness) for chromosome in population]
            fittest_found = population[fitness_values.index(max(fitness_values))]
            generation = 0

            # while max_fitness != fitness(fittest_found, max_fitness):
            while generation != GENERATIONS_NUMBER and max_fitness != fitness(n, fittest_found, max_fitness):
                population = generate_population(POPULATION_SIZE, n, MUTATION_PROBABILITY, population, fitness_values)
                fitness_values = [fitness(n, chromosome, max_fitness) for chromosome in population]
                current_fittest = population[fitness_values.index(max(fitness_values))]
                if fitness(n, current_fittest, max_fitness) > fitness(n, fittest_found, max_fitness):
                    fittest_found = current_fittest
                generation += 1

            if max_fitness in fitness_values:
                print(f"Solved in generation {generation}")
                solution = population[fitness_values.index(max_fitness)]
                print(f"Found solution = {solution}")
                sc2_solution(generation)
                sc2(n, solution)

            else:
                print(f"No solution is found in {GENERATIONS_NUMBER} generations!!")
                print(f"Fittest found solution = {fittest_found}")
                sc2_limit(generation, fitness(n, fittest_found, max_fitness))
                sc2(n, fittest_found)

        else:
            print(f"Sorry, the problem can't be solved when N = {n}")
            no_solution(n)


    except:
        print("Unexpected Error!!")

    update()
    done()

