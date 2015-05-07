import numpy as np

import settings


def evolve():
    population = np.array([Robby() for i in range(0, settings.POPULATION)])
    for individual in population:
        individual.live()
    new_population = list()


if __name__=='__main__':
    evolve()
