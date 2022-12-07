#!/usr/bin/env python3
import re
from pprint import pprint
import sys
import threading

in_file = "input.txt"


def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    strout = load_input_list()
    tree = {"/": {}}
    path = "/"
    size_counter = 0
    for i, line in enumerate(strout):
        # ls command
        if line == "$ ls":
            size_counter = 0
        if m := re.match(r"(\d+) (.+)", line):
            size_counter += int(m.group(1))
            tree[path] = size_counter
        if m := re.match(r"dir (\w+)", line):
            if path not in tree.keys():
                tree[path] = 0
        # cd command for path navigation
        if m := re.match(r"\$ cd (.+)", line):
            if m.group(1) == "/":
                path = "/"
            elif m.group(1) == "..":
                path = path.rsplit("/", 1)[0]
            else:
                current_dir = m.group(1)
                path = f"{path}/{current_dir}"

    depth_dict = {}
    for k in tree.keys():
        depth_dict[k.count("/")] = []
    for k in tree.keys():
        depth_dict[k.count("/")].append(k)

    for n in reversed(range(len(depth_dict.keys()))):
        for path in depth_dict[n + 1]:
            if n >= 1:
                size_counter = tree[path]
                path = path.rsplit("/", 1)[0]
                tree[path] += size_counter

    total = 0
    for v in tree.values():
        if v <= 100000:
            total += v

    return total, tree


def puzzle2():
    # Total disk space 70000000
    # Disk space needed 30000000
    _, tree = puzzle1()
    disk_space_to_clean = 30000000 - (70000000 - tree["/"])
    filter_dirs = [size for i, size in tree.items() if size >= disk_space_to_clean]
    return min(filter_dirs)


if __name__ == '__main__':
    a, _ = puzzle1()
    print(f"Answer to Puzzle: {a}")

    b = puzzle2()
    print(f"Answer to Puzzle: {b}")
