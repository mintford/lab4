import random
import matplotlib.pyplot as plt

def Max_Fitnes(bord_size):
    max_fitnes = 0
    i = bord_size - 1
    while(i > 0):
        max_fitnes += i
        i -= 1
    return max_fitnes

def Random_chromosom(bord_size):
    result = []
    for i in range(bord_size):
        result.append(random.randint(0,bord_size-1))
    return result

def Fitnes(chromosom):
    conflicts = 0
    n = len(chromosom)
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                if chromosom[i] == chromosom[j]:
                    conflicts += 1
                if abs(chromosom[i] - chromosom[j]) == abs(i - j):
                    conflicts += 1
    return Max_Fitnes(n) - conflicts

def Probability(chromosom, max_fitnes):
    return Fitnes(chromosom) / max_fitnes

def Random_pick(pop, probabilites):
    pop_with_prob = zip(pop, probabilites)
    total = sum(w for c, w in pop_with_prob)
    r = random.uniform(0, total)
    up_to = 0
    for c, w in zip(pop, probabilites):
        if up_to + w >= r:
            return c
        else:
            up_to += w

def Crossover(x, y):
    c = random.randint(0, len(x) - 1)
    n = len(x)
    return x[0:c] + y[c:n]

def Crossover2(x, y):
    c = len(x) / 2
    n = len(x)
    return x[0:c] + y[c:n]

def Crossover3(x, y):
    n = len(x)
    z = []
    for iter in range(n):
        if iter % 2 == 0:
            z.append(x[iter])
        else:
            z.append(y[iter])
    return z

def Mutate(x):
    c = random.randint(0, len(x) - 1)
    m = random.randint(0, len(x) - 1)
    n = len(x)
    x[c] = m
    return x

def Solve(pop):
    new_pop = []
    prob = [Probability(ind, max_fitness)for ind in pop]
    for i in range(len(pop)):
        x = Random_pick(pop, prob)
        y = Random_pick(pop, prob)
        child = Crossover(x, y)
        if random.random() < mutation_prob:
            child = Mutate(child)
        new_pop.append(child)
        if Fitnes(child) == max_fitness:
            break
    return new_pop

def Mean_fitness(pop):
    sum = 0
    for i in range(len(pop)):
        sum += Fitnes(pop[i])
    return sum / len(pop)

if __name__ == "__main__":
    n = 8
    mutation_prob = 0.5
    max_fitness = Max_Fitnes(n)
    max_pop = 500

    pop = [Random_chromosom(n) for i in range(max_pop)]
    generation = 1
    plot = []
    plt.ion()

    while not max_fitness in [Fitnes(x) for x in pop]:
        pop = Solve(pop)
        M = Mean_fitness(pop)
        plot.append(M)

        plt.clf()
        plt.plot(plot)
        plt.draw()
        plt.pause(0.01)

        print("pop №" + str(generation) + " Fitness = " + str(M))
        generation += 1
        for x in pop:

            if Fitnes(x) == max_fitness:
                print(str(Fitnes(x)))
                print(x)

    plt.ioff()
    plt.show()
