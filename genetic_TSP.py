import array
import random
import sys
import multiprocessing

import numpy as np

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# because we want to minimise the distance we will mark the distance between the same cities with 1000
distance_map = [[1000, 20, 42, 35],
                [20, 1000, 30, 34],
                [42, 30, 1000, 12],
                [35, 34, 12, 1000]]

START_CITY = 0


# Custom init function because we want to end in the START_CITY city.
def custom_init(icls):
    import random
    genome = list()
    for i in range(0, 3):
        genome.append(random.randrange(0, 4))
    genome.append(START_CITY)

    return icls(genome)


# Calculates the fitness of the individual.
def calculate_individual_fitness(individual):
    same_cities = {}
    distance = 0
    for i in range(0, len(individual)):
        if individual[i] == i:
            return 1000,
        if individual[len(individual)-1] != START_CITY:
            return 1000,
        if individual[i] in same_cities:
            return 1000,
        same_cities.update({individual[i]: True})

        distance += distance_map[i][individual[i]]

    return distance,


toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)
toolbox.register("attributes", random.randint, 0, 3)
toolbox.register("individual", custom_init, creator.Individual)


# main function
def main():
    global toolbox

    pool = multiprocessing.Pool(processes=32)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxPartialyMatched)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register("evaluate", calculate_individual_fitness)
    toolbox.register("map", pool.map)

    pop = toolbox.population(n=2000)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)

    random.seed(170)
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 10, stats=stats, halloffame=hof, verbose=True)

    for h in hof:
        print(h)


if __name__ == '__main__':
    main()
