#!/usr/bin/env python3
from pprint import pprint

in_file = "input.txt"
import re
import numpy as np

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    prog_dict = {}
    cycle = 1
    for command in load_input_list():
        if m := re.match(r"noop", command):
            prog_dict[cycle] = [m[0], 0]
            cycle += 1
        if m := re.match(r"addx (\d+|-?\d+)", command):
            prog_dict[cycle] = [m[0], 0]
            prog_dict[cycle + 1] = [m[0], int(m[1])]
            cycle += 2

    register_x = 1
    compute_dict = {}
    for cycle, prog in prog_dict.items():
        command, val = prog
        compute_dict[cycle] = [command, val, register_x, register_x + val]
        register_x += val

    cycle_signal_list = [20, 60, 100, 140, 180, 220]
    result = 0
    for cycle in cycle_signal_list:
        result += int(cycle) * compute_dict[cycle][2]
    return result, compute_dict


def puzzle2(compute_dict):
    display=["."*40]*6

    for cycle in compute_dict.keys():
        row=(cycle-1) // 40
        pixel=(cycle-1)-row*40
        sprite=compute_dict[cycle][2]
        sprite_range=list(range(sprite-1,sprite+2,1))
        if pixel in sprite_range:
            display[row]= display[row][:pixel]+"#"+display[row][pixel+1:]
    return display

if __name__ == '__main__':
    a, compute = puzzle1()
    print(f"Answer to Puzzle: {a}")

    b = puzzle2(compute)
    pprint(b)
