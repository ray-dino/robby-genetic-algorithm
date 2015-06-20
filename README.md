# How to run
1. Install requirements.
```
pip install requirements.txt
```

2. Run the program.
```
python main.py
```

# Project Outline

A genetic algorithm to create an optimal "Robby": a self-directed robot tasked to pick up cans littered around a 10x10 board.

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
+10 points for each can Robby successfully picks up.
-5 if he crashes into a wall.
-1 point if Robby tries to pick up a can when there isn't one.
* Can be born out of 2 other Robbies, with a new DNA that is a mix of the parents' DNAs, with a small chance of mutation.

## Evolution
1. Start with P individuals (Robbies) that have random DNA.
[Repeat the ff for G generations.]
2. Calculate the fitness for each individual in the current generation.
3. Apply evolution.
  * Choose 2 Robbies as parents probabilistically based on fitness.
  * "Mate" the 2 Robbies to create 2 children to add to a new population.
4. Once the new population is of size P, return to step 2.

# To Do

* Concurrency
* Save the DNA of the fittest indvidual.
* Visualization showing a board and a Robby. Accepts input DNA object to determine the Robby's behavior.
