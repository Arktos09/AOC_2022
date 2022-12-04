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
    result = 0
    for line in read_input_lines():
        a,b,c,d = [int(x) for x in line.replace("-", ",").split(",")]
        s1, s2 = set(range(a,b+1)),  set(range(c,d+1))
        if (not (s1-s2)) or (not (s2-s1)):
            result+=1

    print(result)


def part_b():
    result = 0
    for line in read_input_lines():
        a, b, c, d = [int(x) for x in line.replace("-", ",").split(",")]
        s1, s2 = set(range(a, b + 1)), set(range(c, d + 1))
        if s1 & s2:
            result += 1

    print(result)

part_a()
part_b()