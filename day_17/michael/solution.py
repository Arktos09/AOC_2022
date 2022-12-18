import os
from collections import Counter

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def simplifymap(map):
    counts = Counter((x.real for x in map))
    for k,v in counts.items():
        if v == 7:
            return {x for x in map if x.real >= v}
    return map


def part_a():
    pat = read_input_text()
    rock_types = [{1j * i for i in range(4) } , # as defined from lower left corner being 0, _
                  {1j, 1, 1j+1, 1j+2, 2j+1}, # +
                  {0, 1j, 2j, 2j+1, 2j+2}, # L
                  set(range(4)), #|
                  {0,1j,1,1j+1}] # #

    min_x, max_x = -2, 4
    highest_point = -1
    floor = -1

    map = {-1 + (x-2) * 1j  for x in range(7)}
    windix = 0

    for rocknr in range(2022):
        rock = rock_types[rocknr%5]
        rock = {point + highest_point + 4 for point in rock}
        while True:
            dwind = {">" : 1j, "<" : -1j}[pat[windix%len(pat)]]
            blownrock = {point + dwind for point in rock}
            if all((max_x >= point.imag >= min_x for point in blownrock)) and not (blownrock & map): # rock can move
                rock = blownrock
            windix += 1
            droppedrock = {point -1 for point in rock}
            if any((point.real <= floor for point in droppedrock )) or (droppedrock & map): #our rock would collide with floor or other rock
                for point in rock:
                    map.add(point)
                highest_point = max((point.real for point in map))

                break
            else:
                rock = droppedrock


    print(max(point.real for point in map) + 1)

part_a()
def part_b():


    def get_state(map, maxh, windix,pat, rockix): # flat top, windindex = 0
        top_view = []
        for xcoord in range(7):
            h = maxh
            while True:
                if h + (xcoord-2) * 1j in map:
                    top_view.append(h)
                    break
                h-=1

        top_view = tuple([h - maxh for h in top_view])
        return (top_view, windix % len(pat),rockix % 5)

    rock2score = {}
    state2rocknr = {}

    #pat = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"#
    pat = read_input_text()
    rock_types = [{1j * i for i in range(4)},  # as defined from lower left corner being 0, _
                  {1j, 1, 1j + 1, 1j + 2, 2j + 1},  # +
                  {0, 1j, 2j, 2j + 1, 2j + 2},  # L
                  set(range(4)),  # |
                  {0, 1j, 1, 1j + 1}]  # #

    min_x, max_x = -2, 4
    highest_point = -1

    map = {-1 + (x-2) * 1j  for x in range(7)}
    windix = 0
    rocknr = 0

    while True:
        rock = rock_types[rocknr % 5]
        rock = {point + highest_point + 4 for point in rock}
        while True:
            dwind = {">": 1j, "<": -1j}[pat[windix % len(pat)]]
            blownrock = {point + dwind for point in rock}
            if all((max_x >= point.imag >= min_x for point in blownrock)) and not (blownrock & map):  # rock can move
                rock = blownrock
            windix += 1
            droppedrock = {point - 1 for point in rock}
            if (droppedrock & map):  # our rock would collide with floor or other rock
                for point in rock:
                    map.add(point)
                highest_point = max((point.real for point in map))
                rocknr +=1
                rock2score[rocknr] = highest_point + 1
                state = get_state(map, highest_point, windix,pat, rocknr)
                if state in state2rocknr:
                    print("cycle found!")
                    rocks_left = 1000000000000 - rocknr
                    cycle_length = rocknr - state2rocknr[state]
                    cycles, out_of_cycles = rocks_left//cycle_length, rocks_left % cycle_length
                    cycle_value = (highest_point + 1) - rock2score[state2rocknr[state]]
                    out_of_cycle_value = rock2score[state2rocknr[state]+out_of_cycles ] - rock2score[state2rocknr[state]]
                    print(cycle_value * cycles + (highest_point + 1) + out_of_cycle_value)
                    return
                state2rocknr[state] = rocknr

                break
            else:
                rock = droppedrock

part_b()