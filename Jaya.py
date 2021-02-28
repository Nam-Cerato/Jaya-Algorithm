import numpy as np
import random

n_iterations = 100
n_populations = 25


class Population():

    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 50,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 50]) #[-50 ; 50]

    def __str__(self):
        print("i'm at :", self.position)

class Optimizer():
    def __init__(self, n_populations):
        self.n_populations = n_populations
        self.populations = []
        self.gbest  = []
        self.gbest_value = float("inf")
        self.gworst = []
        self.gworst_value = float("0")
        self.func_value = []

    def fitness(self, population):
        return population.position[0] ** 2 + population.position[1] ** 2 + 1


    def calculate(self):
        self.func_value.clear()
        for population in self.populations:
            cal = self.fitness(population)
            self.func_value.append(cal)

    def setGbest(self):
        self.gbest.clear()
        self.func_value.sort()
        print("fsort", self.func_value)
        self.gbest_value = self.func_value[0]
        print("g",self.gbest_value)
        for population in self.populations:
            fit_candicate = self.fitness(population)
            if(fit_candicate <= self.gbest_value):
                self.gbest_value = fit_candicate
                # self.gbest = population.position
                for i in range(2):
                    self.gbest.append(population.position[i])

    def setGworst(self):
        self.gworst.clear()
        self.func_value.sort()
        print("fsort", self.func_value)
        self.gworst_value = self.func_value[-1]
        print("g", self.gworst_value)
        for population in self.populations:
            fit_can = self.fitness(population)
            if(fit_can >= self.gworst_value):
                self.gworst_value = fit_can
                self.gworst.clear()
                for i in range(2):
                    self.gworst.append(population.position[i])


    def changePopulation(self):
        for i  in range(n_populations):
            new_pos_of_population = (
                    self.populations[i].position + (random.random() * (self.gbest - np.abs(self.populations[i].position) )) -
                    ( random.random() * (self.gworst - np.abs(self.populations[i].position)))
            )
            new_population = Population()
            new_population.position = new_pos_of_population
            new_fitness = self.fitness(new_population)
            if (new_fitness < self.fitness(self.populations[i])):
                self.populations[i] = new_population


    def print_pos(self):
        for population in self.populations:
            population.__str__()

start = Optimizer(n_populations)
for i in range(n_populations):
    p1 = Population()
    start.populations.append(p1)

iter = 0
while( iter < n_iterations):
    start.print_pos()
    start.calculate()
    start.setGbest()
    print("b", start.gbest)
    start.setGworst()
    print("w", start.gworst)
    print("f", start.func_value)
    print("\n")
    start.changePopulation()
    iter += 1

print("gbest is: ",start.gbest_value)
print("gbest_pos is : ", start.gbest)










