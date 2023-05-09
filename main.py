from res.chromosomes import *
from random import *
from ui.final_UI import *

# Constants
POPULATION_SIZE = 200
MUTATION_PROBABILITY = 0.05
GENERATIONS_NUMBER = 1000


# Main screen to draw on it
win = Screen()
win.title("N-Queen Problem")
win.bgcolor("#dfe6dc")
win.setup(600,600)
win.tracer(0)
win.setworldcoordinates(0,0,600,600)


def fitness(n: int, chromosome: list[int], max_fitness: int) -> int:
    """
    It checks for each queen if there is a conflict with the other queens or not, sum those conflicts, then
    subtract them from the max fitness to get the chromosome fitness.\n
    It loops over all the queens in the chromosome, in each iteration we loop for the other queens. If there
    is a conflict in the same column (the queens in rows i, j are in the same column), we increase the conflicts.
    If there is a conflict in the same diagonal (the absolute difference between the columns in which the queens
    in rows i, j are in is equal to the absolute difference between rows i, j), we increase the conflicts.
    """
    conflicts = 0

    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i]-chromosome[j]) == abs(i-j):
                conflicts += 1

    return int(max_fitness-conflicts)


if __name__ == "__main__":

    try:
        n = sc1(win) # Get the n as an input from the user using Turtle

        if n != 2 and n != 3: # Check if the problem can be solved or not

            max_fitness = (n * (n-1)) / 2 # get the max fitness can be reached for n
            
            # Generate the initial population
            population = [generate_chromosome(n) for _ in range(POPULATION_SIZE)]
            
            # Evaluate the fitness value for each chromosome
            fitness_values = [fitness(n, chromosome, max_fitness) for chromosome in population]
            
            # Save the fittest found chromosome, it's used when there is no solution found
            fittest_found = population[fitness_values.index(max(fitness_values))]
            
            generation = 0


            # while max_fitness != fitness(fittest_found, max_fitness):
            while generation != GENERATIONS_NUMBER and max_fitness != fitness(n, fittest_found, max_fitness):
                population = generate_population(POPULATION_SIZE, n, MUTATION_PROBABILITY, population, fitness_values)
                fitness_values = [fitness(n, chromosome, max_fitness) for chromosome in population]

                # Check if the fittest one in the current population is more fit than the saved one
                current_fittest = population[fitness_values.index(max(fitness_values))]
                if fitness(n, current_fittest, max_fitness) > fitness(n, fittest_found, max_fitness):
                    fittest_found = current_fittest
                
                generation += 1

            # Check if there is a solution in the last population to show
            if max_fitness in fitness_values:
                print(f"Solved in generation {generation}")
                solution = population[fitness_values.index(max_fitness)]
                print(f"Found solution = {solution}")
                
                # Use Turtle to show the solution
                sc2_solution(generation)
                sc2(n, solution)

            else:
                print(f"No solution is found in {GENERATIONS_NUMBER} generations!!")
                print(f"Fittest found solution = {fittest_found}")
                
                # Use Turtle to show the solution
                sc2_limit(generation, fitness(n, fittest_found, max_fitness))
                sc2(n, fittest_found)

        else:
            # tell the user that the problem can't be solved
            print(f"Sorry, the problem can't be solved when N = {n}")
            no_solution(n)


    except:
        print("Unexpected Error!!")

    update()
    done()

