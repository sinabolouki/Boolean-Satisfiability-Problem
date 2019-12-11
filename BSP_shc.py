import random
import time


def is_true(arg, values):
    res = False
    for i in arg:
        if i > 0:
            res = res or values[i - 1]
        else:
            res = res or not values[-i - 1]
    return res


def height_func(args, values):
    result = 0
    for arg in args:
        if is_true(arg, values):
            result += 1
    return result


def find_neighbors(args, value):
    n = len(value)
    neighbor_heights = [0] * n
    neighbors = []
    for i in range(n):
        new_value = value.copy()
        new_value[i] = not value[i]
        neighbors.append(new_value)
        neighbor_heights[i] = height_func(args, new_value)

    return neighbors, neighbor_heights


def random_pos(value):
    n = len(value)
    pop = []
    j = 0
    while j < n:
        if random.random() < 0.5:
            pop.append(False)
        else:
            pop.append(True)
        j += 1
    return pop


def choose_successor(args, value):
    choices = []
    k = len(args)
    current_height = height_func(args, value)
    neighbors, neighbor_heights = find_neighbors(args, value)
    l = len(neighbors)
    # print(neighbor_heights)
    for i in range(l):
        if neighbor_heights[i] >= current_height:
            choices += [i] * (neighbor_heights[i] - current_height)
    if len(choices) != 0:
        successor = neighbors[random.choice(choices)]
    elif current_height != k:
        successor = random_pos(value)
    else:
        successor = value
    return successor


start = time.time()
f = open("s3.txt", "r")
n, k = map(int, f.readline().split())
variables = [False] * n
args = []
pop_num = 1000
for i in range(k):
    arg = list(map(int, f.readline().split()))
    args.append(arg)
h = height_func(args, variables)
max_h = h
max_var = variables
while h < k and time.time() - start < 300:
    variables = choose_successor(args, variables)
    h = height_func(args, variables)
    if h > max_h:
        max_h = h
        max_var = variables
    # print(h)
print("time: ", time.time() - start)
print("max height: ", max_h)
print("variables: ", max_var)

