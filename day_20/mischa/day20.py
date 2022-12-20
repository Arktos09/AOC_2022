import os
import re
from collections import deque, defaultdict
from copy import deepcopy
from itertools import cycle

dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()
lines = read_input_lines()



lines_1 = [(i, int(lines[i])) for i in range(len(lines))]

lines_2 = deepcopy(lines_1)
zero_val = ""
for i in lines_1:
    move = int(i[1])
    if move == 0: #save the zero tuple for later finding it in the ordered list
        zero_val = i
    pos = lines_2.index(i)

    new_ind = ( pos+move ) % (len(lines_1)-1)
    lines_2.remove(i)
    lines_2.insert(new_ind,i)

zero_ind = lines_2.index(zero_val)
lines_2cycle = cycle(lines_2)

a,b,c = 0,0,0
for x,i in enumerate(lines_2cycle):
    if x == 1000+zero_ind:
        a= int(i[1])
    if x == 2000+zero_ind:
        b= int(i[1])
    if x == 3000+zero_ind:
        c= int(i[1])
    if x == 3001+zero_ind:
        break
print("part 1: ",a+b+c)

'''
part 2
'''

lines_1 = [(i, int(lines[i])*811589153) for i in range(len(lines))]

lines_2 = deepcopy(lines_1)
zero_val = ""
for step in range(10):
    print(step)
    for i in lines_1:
        move = int(i[1])
        if move == 0: #save the zero tuple for later finding it in the ordered list
            zero_val = i
        pos = lines_2.index(i)
        new_ind = (pos+move) % (len(lines_1)-1)
        lines_2.remove(i)
        lines_2.insert(new_ind,i)

zero_ind = lines_2.index(zero_val)
lines_2cycle = cycle(lines_2)

a,b,c = 0,0,0
for x,i in enumerate(lines_2cycle):
    if x == 1000+zero_ind:
        a= int(i[1])
    if x == 2000+zero_ind:
        b= int(i[1])
    if x == 3000+zero_ind:
        c= int(i[1])
    if x == 3001+zero_ind:
        break
print("part 2: ",a+b+c)

