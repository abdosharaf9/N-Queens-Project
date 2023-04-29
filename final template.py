import random

def random_chromosome(size):
    return [ random.randint(1, nq) for _ in range(nq) ]

# يعتمد ✅✅
def fitness(solution):
    n = len(solution)
    conflicts = 0

    for i in range(n):
        for j in range(i+1, n):
            if solution[i] == solution[j] or abs(solution[i]-solution[j]) == abs(i-j):
                conflicts += 1

    return maxFitness-conflicts


def probability(chromosome, maxFitness):
    return fitness(chromosome) / maxFitness


def parent_selection(population, probabilities):
    total = sum(probabilities)
    r = random.uniform(0, total)
    populationWithProbabilty = zip(population, probabilities)
    
    upto = 0
    for c, w in populationWithProbabilty:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        

def crossover(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def generate_population(population, maxFitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, maxFitness) for n in population]

    for _ in range(len(population)):
        x = parent_selection(population, probabilities)
        y = parent_selection(population, probabilities)
        child = crossover(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break

    return new_population


def print_chromosome(chrom):
    print(f"Chromosome = {chrom},  Fitness = {fitness(chrom)}")


if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: "))
    maxFitness = (nq*(nq-1))/2

    population = [random_chromosome(nq) for _ in range(50)]
    generation = 0

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print(f"=== Generation {generation} ===")
        population = generate_population(population, maxFitness)
        popFitness = max([fitness(n) for n in population])
        print(f"\nMaximum Fitness = {popFitness}")
        generation += 1

    chrom_out = []
    print(f"Solved in Generation {generation}!")
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("\nOne of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom)
            break
            
    board = []

    for x in range(nq): board.append(["x"] * nq)
        
    for i in range(nq): board[nq-chrom_out[i]][i]="Q"

    print()
    for row in board: print (" ".join(row))

# الاندكس صف والقيمة عامود
# عدد االمحاولات هو الاجيال
# الاعلى الى لقيناه