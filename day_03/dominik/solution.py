#!/usr/bin/env python3

in_file = "input.txt"


def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def prio_counter(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def puzzle1():
    backpacks = load_input_list()
    prio_sum = 0
    for bag in backpacks:
        comp1, comp2 = set(bag[:int(len(bag) / 2)]), set(bag[int(len(bag) / 2):])
        duplette = "".join(comp1.intersection(comp2))
        prio_sum += prio_counter(duplette)
    return prio_sum


def puzzle2():
    backpacks = load_input_list()
    groups = [backpacks[x:x + 3] for x in range(0, len(backpacks), 3)]
    prio_sum = 0
    for g in groups:
        prio = "".join(set(g[0]).intersection(set(g[1]),set(g[2])))
        prio_sum += prio_counter(prio)
    return prio_sum


if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to puzzle a is: {a}")
    b = puzzle2()
    print(f"Answer to puzzle b is: {b}")
