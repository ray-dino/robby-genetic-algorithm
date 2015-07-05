import logging
import numpy as np

import settings
from models import Robby


def evolve():
    population = np.array([Robby() for i in range(0, settings.POPULATION)])
    for gen in range(0, settings.GENERATIONS):
        for individual in population:
            individual.live()
        logging.info("Generation {}: {}".format(
            gen,
            max([r.get_fitness() for r in population])))
        new_population = list()
        while len(new_population)<settings.POPULATION:
            father, mother = np.random.choice(
                population,
                size=2,
                p=get_relative_probabilities(population))
            child1, child2 = father.mate(mother)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    alpha = get_alpha(population)
    return alpha

def get_alpha(population):
    fittest = None
    for individual in population:
        if fittest is None:
            fittest = individual
        else:
            if fittest.get_fitness() < individual.get_fitness():
                fittest = individual
    return fittest


def get_relative_probabilities(population):
    pop_fitness = [r.get_fitness() for r in population]
    min_fitness = min(pop_fitness)
    max_fitness = max(pop_fitness)
    normalized = list(
        map(
            lambda x: normalize(x, min_fitness, max_fitness),
            pop_fitness
        )
    )
    total = sum(normalized)
    return list(map(lambda x: x/total, normalized))


def normalize(x, minf, maxf):
    return (x - minf) / (maxf - minf)


if __name__=='__main__':
    logging.basicConfig(level=20)
    alpha = evolve()
    logging.info(''.join([str(int(x)) for x in alpha.get_dna().get_sequence()]))
