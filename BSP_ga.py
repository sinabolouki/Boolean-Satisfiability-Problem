import random
import time


def is_true(arg, values):
    res = False
    # print(list(arg))
    for i in arg:
        if i > 0:
            res = res or values[i - 1]
        else:
            res = res or not values[-i - 1]
    return res


def fitness_func(args, values):
    result = 0
    for arg in args:
        if is_true(arg, values):
            result += 1
    return result


def random_first_population(n, pop_size):
    first_pop = []
    i = 0
    while i < pop_size:
        pop = []
        j = 0
        while j < n:
            if random.random() < 0.5:
                pop.append(False)
            else:
                pop.append(True)
            j += 1
        first_pop.append(pop)
        i += 1
    return first_pop


def random_select(args, population, fits, is_first):
    choices = []
    i = 0
    while i < len(population):
        if is_first:
            fit = fitness_func(args, population[i])
            fits[i] = fit
        else:
            fit = fits[i]
        choices += [i] * fit
        i += 1
    pop = population[random.choice(choices)]
    return pop


def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:]


def is_false(args, population, fits):
    l = len(args)
    for i in fits:
        if i == l:
            return False
    return True


def is_mutate():
    if random.random() < 0.001:
        return True
    else:
        return False


def mutate(child):
    n = len(child)
    c = random.randint(0, n - 1)
    child[c] = not child[c]


start = time.time()
f = open("s3.txt", "r")
n, k = map(int, f.readline().split())
variables = [False] * n
args = []
pop_num = 1000
for i in range(k):
    arg = list(map(int, f.readline().split()))
    args.append(arg)
population = random_first_population(n, pop_num)
fits = [0] * pop_num
# print(args)
# print(time.time() - start)
max_fit = 0
fit_var = 0
while is_false(args, population, fits) and time.time() - start < 300:
    new_pop = []
    i = 0
    while i < len(population):
        x = random_select(args, population, fits, True)
        y = random_select(args, population, fits, False)
        child = reproduce(x, y)
        # print(child == x, child == y)
        if is_mutate():
            # print("mutated")
            mutate(child)
        new_pop.append(child)
        i += 1
    max_of_fit = max(fits)
    if max_fit < max_of_fit:
        max_fit = max_of_fit
        fit_var = population[fits.index(max_fit)]
    population = new_pop
    # print(max_of_fit)
    # print(time.time() - start)

print("time: ", time.time() - start)
print("max fitness: ", max_fit)
print("variables: ", fit_var)

