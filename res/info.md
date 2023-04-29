# What techniques are used?
- Parent selection --> Roulette Wheel
- Crossover --> One Point
- Mutation --> Change a random gene (the mutation rate)
- Ethier iterate 500 iterations or until we find the solution (This may go in an infinite loop)
- Use the GUI to display the solution or if there is no solution we will display the best found one


# How the algorithm works?
- Enter number of queens N
- Calculate the max fitness we can reach
- create the initial population
- iterate until you found the solution or if you reach specific number of generations:
    • generate new population
        ♣ select parents
        ♣ make crossover between the parents
        ♣ mutate some of the childs
    • evaluate the fitness function for all chromosomes
    • save the best chromosome from the population (to display it if there is no solution)

---

## Parent selection methods:
1- Roulette Wheel Selection: This method selects parents based on a fitness proportionate selection 
approach, where individuals with higher fitness values are more likely to be selected as parents.
It involves creating a roulette wheel where each individual's slice of the wheel is proportional 
to its fitness value. The wheel is then spun to randomly select parents.

2- Tournament Selection: This method involves selecting individuals at random from the population 
and then choosing the one with the highest fitness value as a parent. This process is repeated to 
select multiple parents.

3- Rank Selection: This method ranks individuals in the population based on their fitness values and 
then selects parents based on their rank. Higher-ranked individuals have a greater chance of being selected as parents.

4- Stochastic Universal Sampling: This method is similar to roulette wheel selection, but instead of 
spinning the wheel multiple times, multiple individuals are selected at once by evenly spaced pointers 
on the wheel. This can help prevent premature convergence by selecting a more diverse set of parents.

5- Fitness Proportional Selection: This method selects parents based on the probability of an individual 
being selected being proportional to its fitness value. This method can be more computationally expensive 
than other methods, but can be useful in cases where the fitness landscape is highly non-linear.

- The choice of parent selection method depends on the problem being solved, as well as the characteristics 
of the population and fitness landscape. Some methods may work better than others for different types 
of problems, and it is often useful to experiment with different methods to find the most effective one.


### Roulette Wheel:
This method is implemented as follows:
1. Sum the total expected value of the individuals in the population. Let it be T.
2. Repeat N times:
    i. Choose a random integer ‘r’ between o and T.
    ii. Loop through the individuals in the population, summing the expected values, 
    until the sum is greater than or equal to ‘r’. The individual whose expected value 
    puts the sum over this limit is the one selected.
Roulette wheel selection is easier to implement but is noisy. The rate of evolution
depends on the variance of fitness’s in the population.

---

## References:
- https://github.com/waqqasiq/n-queen-problem-using-genetic-algorithm
- https://github.com/KhaledR57/QueensGeneticAlgorithm
- https://youtu.be/GJXcfWaV_qg