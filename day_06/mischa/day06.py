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

lines = [x for x in read_input_text()]



for ind,i in enumerate(lines[3:]):
    ind +=3
    pure = [lines[ind],lines[ind-1],lines[ind-2],lines[ind-3]]
    a = [ord(lines[ind]),ord(lines[ind-1]),ord(lines[ind-2]),ord(lines[ind-3])]
    b = set(a)
    if len(a) == len(b):
        print(pure,a,b, ind+1)
        break

for ind,i in enumerate(lines[14:]):
    ind +=14
    a =[]
    for x in range(14):
        a.append(ord(lines[ind-x]))
    b = set(a)
    if len(a) == len(b):
        print(a,b, ind+1)
        break