#!/usr/bin/env python3

in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    pass

def puzzle2():
    pass

if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle: {a}")

    b = puzzle2()
    print(f"Answer to Puzzle: {b}")