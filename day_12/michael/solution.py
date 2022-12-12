import os


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

def solve(map, startloc, endloc):
    loc2steps = {startloc: 0}
    current = {startloc}
    next_current = set()
    while not endloc in loc2steps:
        for item in current:
            for dir in [1, -1, 1j, -1j]:
                nextloc = item + dir
                if (nextloc in map) and (nextloc not in loc2steps) and ((ord(map[nextloc]) - ord(map[item])) < 2):
                    loc2steps[nextloc] = loc2steps[item] + 1
                    next_current.add(nextloc)

        current = next_current
        next_current = set()

    return loc2steps[endloc]



def part_a():
    map = {rownr + colnr * 1j : letter for rownr, row in enumerate(read_input_lines()) for colnr, letter in enumerate(row)}
    startloc = [k for k ,v in map.items() if v == "S"][0]
    endloc = [k for k, v in map.items() if v == "E"][0]
    map[startloc], map[endloc] = "a", "z"

    loc2steps = {startloc: 0}
    current = {startloc}
    next_current = set()

    while not endloc in loc2steps:
        for item in current:
            for dir in [1, -1, 1j, -1j]:
                nextloc = item + dir
                if (nextloc in map) and (nextloc not in loc2steps) and ((ord(map[nextloc]) - ord(map[item])) < 2):
                    loc2steps[nextloc] = loc2steps[item] + 1
                    next_current.add(nextloc)

        current = next_current
        next_current = set()

    print(loc2steps[endloc])


def part_b():
    # we flip it around so we start at z and the first a we find is our solution. rule is you can only step down 1 step
    map = {rownr + colnr * 1j: letter for rownr, row in enumerate(read_input_lines()) for colnr, letter in
           enumerate(row)}
    startloc = [k for k, v in map.items() if v == "S"][0]
    endloc = [k for k, v in map.items() if v == "E"][0]
    map[startloc], map[endloc] = "a", "z"

    loc2steps = {endloc: 0}
    current = {endloc}
    next_current = set()

    while True:
        for item in current:
            for dir in [1, -1, 1j, -1j]:
                nextloc = item + dir
                if (nextloc in map) and (nextloc not in loc2steps) and ((ord(map[nextloc]) - ord(map[item])) > -2):
                    loc2steps[nextloc] = loc2steps[item] + 1
                    next_current.add(nextloc)
                    if map[nextloc] == 'a': # a starting point found!
                        print(loc2steps[nextloc])
                        return

        current = next_current
        next_current = set()

    print(loc2steps[endloc])

part_a()
part_b()