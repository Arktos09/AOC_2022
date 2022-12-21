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

def parse_robotcoststring(instr):
    robottype = instr.split()[1]
    costs = {x.split(" ")[-1] : int(x.split(" ")[-2]) for x in instr.split(" and ")}
    return (robottype, costs)

def generate_resources(liststate):
    for i in range(4):
        liststate[i + 4] += liststate[i]

def simplify_state(liststate, max_cost_per_round_per_mat, rounds_left):
    """ for resources we cannot exhaust robots and resources are inf
        shamelessly stolen from https://www.reddit.com/r/adventofcode/comments/zpnkbm/comment/j0v7gh6/"""

    for i in range(3):
        if liststate[i+4] >= (rounds_left * max_cost_per_round_per_mat[i]):
            liststate[i] = float("inf")
            liststate[i+4] = float("inf")
    return liststate

def run(instr, rounds):
    costs = instr.split(":")[-1]
    costdict = {robottype: cost for robottype, cost in [parse_robotcoststring(x) for x in costs.split(".") if x]}
    # example: {'ore': {'ore': 4}, 'clay': {'ore': 4}, 'obsidian': {'ore': 4, 'clay': 18}, 'geode': {'ore': 4, 'obsidian': 9}}
    material2index = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
    index2material = {v: k for k, v in material2index.items()}
    states = {(1, 0, 0, 0, 0, 0, 0, 0)}  # ore, clay, obsidean, geode, first robots then
    new_states = set()

    max_cost_per_round_per_mat = [max(x.get(index2material[ix]) or 0 for x in costdict.values()) or 0 for ix in
                                  range(4)]
    for round in range(rounds):

        # print(len(states))
        for state in states:
            # choice, buy something
            for robottype, ingredients in costdict.items():  # assume only one robot can be made at a time
                mat_ix = material2index[robottype]
                if (not state[mat_ix] >= max_cost_per_round_per_mat[
                    mat_ix]) or mat_ix == 3:  # we already make more than we need for this mat
                    list_state = list(state)
                    for material, n in ingredients.items():
                        list_state[4 + material2index[material]] -= n
                    if min(list_state) >= 0:  # if we can actually afford it
                        generate_resources(list_state)
                        list_state[mat_ix] += 1
                        new_states.add(tuple(simplify_state(list_state, max_cost_per_round_per_mat, (rounds+1) - round)))

            # do not buy anything
            list_state = list(state)
            generate_resources(list_state)
            new_states.add(tuple(simplify_state(list_state, max_cost_per_round_per_mat, (rounds+1) - round)))

        states = new_states
        new_states = set()
    return (max(state[-1] for state in states))


def part_a():
    result = 0
    for instix, instr in enumerate(read_input_lines()):
        result += (instix + 1) * run(instr, 24)
        print(result)



#part_a()


def part_b():
    result = 1
    for instix, instr in enumerate(read_input_lines()[:3]):
        result *= run(instr, 32)
        print(result)

part_b()
