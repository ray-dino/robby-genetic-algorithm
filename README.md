# Project Outline

## Board
* A 10x10 matrix where each cell has a 50% of having a can.

## DNA
* A sequence of 243 integers, each between 0-6.
* Dictates Robbie's behavior in any possible scenario.
* Can be created with random integers, or from a combination of 2 other DNAs with a small chance of mutation.

## Robby
* A "robot" initially positioned at [0,0] of the board.
* Can determine the status of his surroundings.
* Has a DNA, that dictates behavior in any the possible scenarios.
* Has a lifespan of X turns, at the end of which a fitness score is calculated.
* Can be born out of 2 other Robbies, with a new DNA that is a mix of the parents' DNAs, with a small chance of mutation.

*X = An integer setting for lifespan. Default to 200
*Fitness Score is the sum of the sub-scores per turn.
10 points for each can Robby successfully picks up.
-1 point for each can Robby fails to pick up.
-1 point if Robby tries to pick up a can when there isn't one.*

## Evolution
1. Start with P individuals (Robbies) that have random DNA.
[Repeat the ff for I generations.]
2. Calculate the fitness for each individual in the current generation.
3. Apply evolution.
* Choose 2 Robbies as parents probabilistically based on fitness.
* "Mate" the 2 Robbies to create 2 children.
4. Once the new population is of size P, return to step 2.

*P = An integer setting for the population size. Default to 200.
I = An integer setting for the number of iterations/generations. Default to 1000.
Fitness = the average fitness score for T number of tries on random boards.
T = An integer setting for the number of tries an individual gets. Default to 100.*
