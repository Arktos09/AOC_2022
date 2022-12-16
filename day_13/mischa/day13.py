import os
import re
from collections import deque, defaultdict
import pandas as pd
from functools import cmp_to_key
dir = os.path.dirname(__file__)
os.chdir(dir)
from json import loads
with open("input.txt") as fin:
    lines = fin.read().replace('\n\n', '\n').splitlines()

pairs = []
packets = list(map(loads, lines))
#print(len(packets))
for i in range(0,len(packets),2):
    pairs.append(packets[i:i+2])



def compare(a,b):
    a_int = isinstance(a, int)
    b_int = isinstance(b,int)
    #if both ints, -> lower comes first
    if a_int and b_int:
        return a - b #neg if a is smaller than b, so nothing has to change
        # if it returns 0 they are the same...

    # if one is an int and one is a list -> make the int into a list with 1 item
    if a_int != b_int:
        if a_int:
            return compare([a],b)
        else:
            return compare(a,[b])

    # if both lists ->   compare each item of list
    for x,y in zip(a,b):
        temp = compare(x,y)
        if temp != 0:
            return temp
    #                   lower comes first
    #                   if left list runs out of items pairs are in right order
    #
    return len(a) - len(b)
    #                   if both have the same length -> no decision can be made


g = 0
for ind, (a,b) in enumerate(pairs,start=1):
    if compare(a,b) <0: #aka pair is in right order
        g += ind
print("part1 :",g)



packets.extend(([[2]],[[6]]))
packets.sort(key=cmp_to_key(compare))

g = packets.index([[2]])+1
g *= packets.index([[6]])+1
print("part2 :",g)