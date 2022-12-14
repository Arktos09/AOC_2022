import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    txt = read_input_text()
    for ix, option in enumerate(zip(*(txt[i:] for i in range(4)))):
        if len(set(option)) == 4:
            print(ix + 4)
            break

def part_b():
    txt = read_input_text()
    for ix, option in enumerate(zip(*(txt[i:] for i in range(14)))):
        if len(set(option)) == 14:
            print(ix + 14)
            break

part_a()
part_b()