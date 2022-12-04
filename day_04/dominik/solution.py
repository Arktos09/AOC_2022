#!/usr/bin/env python3
import numpy as np

in_file = "input.txt"


def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def split_range(range_string):
    range_split = range_string.split("-")
    return range(int(range_split[0]), int(range_split[1]) + 1)


def dupletten_check(pair):
    elve_a, elve_b = pair.split(",")
    elve_a = split_range(elve_a)
    elve_b = split_range(elve_b)

    max_range = max([max(elve_a), max(elve_b)])
    check_arr = np.zeros((2, max_range))

    for i, elve in enumerate([elve_a, elve_b]):
        for zone in elve:
            check_arr[i][zone - 1] = 1
    included_range = min([len(elve_a), len(elve_b)])
    return check_arr, included_range


def puzzle1():
    pairs = load_input_list()
    result_sum = 0
    for pair in pairs:
        check_arr, included_range = dupletten_check(pair)
        if included_range == np.count_nonzero(sum(check_arr) == 2):
            result_sum += 1
    return result_sum


def puzzle2():
    pairs = load_input_list()
    result_sum = 0
    for pair in pairs:
        check_arr, _ = dupletten_check(pair)
        if np.count_nonzero(sum(check_arr) == 2) >= 1:
            result_sum += 1

    return result_sum


if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle a is a total of: {a}")
    b = puzzle2()
    print(f"Answer to Puzzle b is a total of: {b}")
