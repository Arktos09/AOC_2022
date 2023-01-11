import os
import re
from collections import deque, defaultdict
import pandas as pd
from operator  import sub,add
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = read_input_lines()
lines = [re.findall(r"[-+]?[.]?[\d]+",x) for x in lines]
new_lines = []
for line in lines:
    l = [int(line[0]),int(line[1]),int(line[2])]
    new_lines.append(l)
lines = new_lines

def find_neighbour_cubes(x,y,z):
    neighbours = []
    for i in [[1,0,0],[0,1,0],[0,0,1]]:
        new = list(map(sub,[x,y,z],i))
        new1 = list(map(add,[x,y,z],i))
        neighbours.append(new)
        neighbours.append(new1)
    return neighbours
count = 0
for i in lines:
    temp = find_neighbour_cubes(i[0],i[1],i[2])
    for i in temp:
        if i in lines:
            count+=1

print("part 1: ",len(lines)*6-count)
