#!/usr/bin/env python3

in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()

def scrolling_window(buffer, window_size):
    for i in range(len(buffer) - window_size + 1):
        yield buffer[i: i + window_size]


def puzzle1():
    nchar=4
    signal_buffer=read_input_text()
    for i, window in enumerate(scrolling_window(signal_buffer, nchar)):
        if len(set(window)) == nchar:
            return i+nchar, window


def puzzle2():
    nchar=14
    signal_buffer = read_input_text()
    for i, window in enumerate(scrolling_window(signal_buffer, nchar)):
        if len(set(window)) == nchar:
            return i + nchar, window

if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle: first signal marker '{a[1]}' at index {a[0]}")

    b = puzzle2()
    print(f"Answer to Puzzle: first signal marker '{b[1]}' at index {b[0]}")