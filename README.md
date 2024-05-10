# Genetic-and-PSO-algorithm-for-secure-domination-number
## genetic algorithm for Secure Domination Problem:
Genetic algorithms simulate the process of natural selection which means those species who can adapt to changes in their environment are able to survive and reproduce and go to next generation. It uses artificial construction of search algorithms.

## Parameters for Genetic Algorithm
1. Initial Population (initial_pop)
2. Number of Solutions (num_sol)
3. Cost obtained in current population (present_min_val)
4. Intermediate population (intermediate_pop)
5. Best Solution (best_sol)
6. Optimal Cost (optimal_val)

## Genetic Algorithm workflow
1. Initialization of population
2. Fitness Evaluation
3. Selection
4. Crossover & mutation
5. Termination Condition

## Particale Swarm Optimization for Secure Domination Problem
1. Initialize Parameters inertia weight (w), two positive constants
(c1, c2) and two random parameters within [0-1] (r1,r2)[10].
2. Intitialize Position (xi and Velocity (Vi) randomly for each particle.
3. Evaualte Fitness f(xi). If fitness Value is better than global best then update global best.
4. Calculate Particle Position and velocity using formulas.
5. Evaualte Fitness f(xi) and find the current best and update to
next iterations. Finally output is gBest (gobal best) and xi position.
6. After doing pso we get particles of the swarm in float values. we have to set the Thresholds for the particles (0,1) and need to perform the feasibility check.

## formulas :
### V(t + 1) = W * V(t) + c1 * r1 * (PB - X(t)) + c2 * r2 * (GB - X(t))
### X(t + 1) = X(t) + V(t + 1)

### where:
V - velocity, 
X - position, 
W - inertia weight, 
PB - personal best, 
GB - global best.
