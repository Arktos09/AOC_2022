import os
import re
from collections import deque, defaultdict
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x for x in read_input_lines()]

def get_dist(a,b):
    return sum(abs(val1-val2) for val1,val2 in zip(a,b))

known_pos = set()
beacons = set()
for i in lines:
    a ,b= [int(x) for x in re.findall(r"[-+]?[.]?[\d]+",i)[:2]],  [int(x) for x in   re.findall(r"[-+]?[.]?[\d]+",i)[2:]]
    beacons.add((b[0],b[1]))
    d = get_dist(a,b)
    for indY,y in enumerate(range(d)):
        if a[1]+y ==2000000 or a[1]-y ==2000000:
            for x in range(d-indY+1):
                if a[1]+y == 2000000 :
                    known_pos.add((a[0] + x  , a[1]+y))
                    known_pos.add((a[0] - x  , a[1] + y))
                elif a[1]-y ==2000000:
                    known_pos.add((a[0] + x, a[1] - y))
                    known_pos.add((a[0] - x, a[1] - y))
beacons_in_line = len(beacons.intersection(known_pos))
positions = len(known_pos) -beacons_in_line
print(positions)
