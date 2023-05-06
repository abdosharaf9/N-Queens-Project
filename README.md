# N-Queens-Project

## N-Queens Problem:-
The N-Queens problem is a classic problem in computer science and mathematics that involves placing N chess queens on an N×N chessboard so that no two queens attack each other. In other words, no two queens share the same row, column, or diagonal.

The N-Queens problem has important applications in areas such as computer vision, robotics, and artificial intelligence. It is also a popular problem for algorithmic competitions and is used as a benchmark problem to compare different algorithms.

The problem is challenging because of the large number of possible solutions, especially for larger values of N. For example, there are 92 distinct solutions for N=8, while there are 2,352,985,830 distinct solutions for N=14. The problem can be solved using various search algorithms, such as backtracking, Genetic Algorithms, and simulated annealing, among others.

In this project we used the <b>Genetic Algorithms</b> search technique to solve it.


---


## Used techniques / libraries:-
<table>
    <caption>Techniques</caption>
    <tr>
        <th>Operation</th>
        <th>Technique</th>
    </tr>
    <tr>
        <td>Parent selection</td>
        <td>Roulette Wheel</td>
    </tr>
    <tr>
        <td>Crossover</td>
        <td>Two Point Crossover</td>
    </tr>
    <tr>
        <td>Mutation</td>
        <td>Random Reset Mutation</td>
    </tr>
</table>

<br>

<table>
    <caption>Libraries</caption>
    <tr>
        <th>Library</th>
        <th>Usage</th>
    </tr>
    <tr>
        <td>Turtle</td>
        <td>Drawing the GUI of the program, which is used to take the input <b>(N)</b>, or to show the algorithm output.</td>
    </tr>
    <tr>
        <td>Random</td>
        <td>Generate random numbers or lists, which is a very important thing in <b>Genetic Algorithms</b></td>
    </tr>
</table>


---


## How the algorithm works?
1. Take number of queens <b>(N)</b> from the user.
2. Calculate the max fitness we can reach, which equals (N * (N-1)) / 2.
3. Create the initial population and evaluate the fitness function for each chromosome.
4. Save the fittest chromosome (to display it if there is no solution).
5. Iterate 1000 iterations or until we find a solution (Because this algorithm may go in an infinite loop):
    - generate new population:
        * select parents.
        * make crossover between the parents.
        * mutate some of the childs (according to the mutation probability).
    - evaluate the fitness function for all chromosomes.
    - compare the current best chromosome with the saved fittest one, and save it if it fits more.
6. If there is a solution found we display it. If there is no solution found we display the fittest found one.


---


## Parent selection:
Parent selection is a term used in Genetic Algorithms that refers to the process of selecting individuals from the current population to be used in generating the offspring for the next generation. The aim of parent selection is to increase the probability of producing better offspring in the next generation. There are several methods of parent selection in Genetic Algorithms, including Roulette Wheel Selection, Tournament Selection, Rank Selection, and others.

- The choice of parent selection method depends on the problem being solved, as well as the characteristics 
of the population and fitness landscape. Some methods may work better than others for different types 
of problems, and it is often useful to experiment with different methods to find the most effective one.


<br>

### Roulette Wheel Selection:
This method selects parents based on a fitness proportionate selection  approach, where individuals with higher fitness values are more likely to be selected as parents. It involves creating a roulette wheel where each individual's slice of the wheel is proportional to its fitness value. The wheel is then spun to randomly select parents.

Roulette wheel selection is easier to implement but is noisy. The rate of evolution
depends on the variance of fitness’s in the population.

<br>

This method is implemented as follows:
1. Sum the total fitness value of each chromosome in the population. Let it be <b>S</b>
2. Calculate the probability of each chromosome, which equals chromosome fitness value / <b>S</b>.
3. Generate random number between 0 and 1, which will be the wheel spinner position. Let it be <b>R</b>
4. Caculate the comulative probability for each chromosome.
5. Choose the first chromosome with the comulative probability that is greater than or equal to <b>R</b>.

<br>

You can repeat these steps until the required number of individuals is selected.

```python
from random import *

def roulette_wheel_selection(population, fitness_values, population_size):
    fitness_sum = sum(fitness_values)
    fitness_probs = [(fitness / fitness_sum) for fitness in fitness_values]
    wheel_position = uniform(0, 1)
    comulative_prob = 0

    for i in range(population_size):
        comulative_prob += fitness_probs[i]
        if comulative_prob >= wheel_position:
            return population[i]
```


---


## Crossover:-
Crossover is a genetic operator in Genetic Algorithms that takes two parent chromosomes and produces one or more offspring chromosomes by combining the genetic information of the parents.

The idea behind crossover is to take advantage of the good qualities of both parents and produce offspring that have better fitness than either parent.

There are several different methods of crossover, including: Single-Point Crossover, Two-Point Crossover, Uniform Crossover, and others.


<br>

### Two Point Crossover:
In this crossover, two crossover points are selected, and the genetic material between these two points is swapped, while the material outside these points remains as the parents.

```python
from random import *

def two_point_crossover(chromosome1, chromosome2, size):
    points = sorted(sample(range(1, size), 2))
    point1 = points[0]
    point2 = points[1]

    child1 = chromosome1[:point1] + chromosome2[point1:point2] + chromosome1[point2:]
    child2 = chromosome2[:point1] + chromosome1[point1:point2] + chromosome2[point2:]

    return child1, child2
```

---


## Mutation:-
Mutation is an operator in Genetic Algorithms that randomly modifies a candidate solution (chromosome) to introduce new chromosome into the population. This is important in GAs to help maintain genetic diversity in the population and to prevent premature convergence to a suboptimal solution. Mutation is typically applied with a low probability (<b>Mutation Probability</b>).

The basic idea of mutation is to change a small subset of the candidate solution's genes in a random way. The exact mutation operator used depends on the encoding of the candidate solutions. For example, for binary encodings, mutation might flip a randomly selected bit. For integer or real value encodings, mutation might add or subtract a small random value to the gene. For permutation encodings (like the N-Queens problem), mutation might swap two random positions in the permutation, or change a gene with a random value in the same numbers range.

<br>


### Random Resetting Mutation
Random Resetting is an extension of the bit flip for the integer representation. In this, a random value from the set of permissible values is assigned to a randomly chosen gene.

```python
from random import *

def random_reset_mutation(chromosome, size):
    index = randint(0, size-1)
    chromosome[index] = randint(1, size)
    return chromosome
```

---


# Screenshots:-



---


# How to run this project?
First you need to have installed in your system. You can check if it's installed using this command in your CMD:
```bash
python -V
```

If it's already installed and want to know the installation path, use this command:
``` bash
where.exe python
```

If it's not installed, download it from [this link](https://www.python.org/downloads/).

<br>

Then you need to clone the repo to run the program, use the Git command `git clone` to clone it as the follows:
``` bash
git clone https://github.com/abdosharaf9/N-Queens-Project.git
```

<br>

After download the project files, you can run it using python directly with this command:
``` bash
python {project path}\main.py
```

<br>

Or, you can run it with any IDE that supports Python language like [VS Code](https://code.visualstudio.com).



---


# References:
- [Inspiration 1](https://github.com/waqqasiq/n-queen-problem-using-genetic-algorithm)
- [Inspiration 2](https://github.com/KhaledR57/QueensGeneticAlgorithm), [YouTube Video](https://youtu.be/GJXcfWaV_qg)
