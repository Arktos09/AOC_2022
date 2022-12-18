import os
from collections import defaultdict

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def get_adj(loc):
        for dim in range(3):
            for dif in [1,-1]:
                yield tuple(loc[:dim] + tuple([loc[dim] + dif]) + loc[dim + 1:])

def part_a():
    locs = {tuple([int(coord) for coord in coords.split(",")]) for coords in read_input_lines()}
    surface = 0
    for loc in locs:
        for adj_loc in get_adj(loc):
            if not adj_loc in locs:
                surface += 1
    print(surface)


def part_b():
    locs = {tuple([int(coord) for coord in coords.split(",")]) for coords in read_input_lines()}
    # coords are between 0 and 19 for each dim

    surface = 0
    visited = {(-1,-1,-1)}
    current_air = {(-1,-1,-1)}
    next_air = set()

    while current_air:
        for air in current_air:
            for adj in get_adj(air):
                if adj in locs:
                    surface += 1

                elif (max(adj) < 21) and (min(adj) > -2) and (adj not in visited):
                    visited.add(adj)
                    next_air.add(adj)
        current_air = next_air
        next_air = set()

    print(surface)

part_a()
part_b()