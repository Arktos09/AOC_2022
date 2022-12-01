import os
import re
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x for x in read_input_text().split("\n\n")]

#part1
max_num =  max([sum(a) for a in [[int(i) for i in re.findall('[0-9]+', x)] for x in lines]])
#part2
top3 = sum(sorted([sum(a) for a in [[int(i) for i in re.findall('[0-9]+', x)] for x in lines]])[-3:])
print("part 1: ",max_num)
print("part 2: ",top3)