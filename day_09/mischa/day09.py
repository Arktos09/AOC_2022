import os
import re
from collections import deque, defaultdict
import pandas as pd
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x.split() for x in read_input_lines()]

#print(lines)


hx,hy = 0,0
tx, ty = 0,0

rope = [(0,0)]*10
directions = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
visited = set()
visitedKnot10 = set()
def move(instructions,hx,hy,tx,ty):
    for instruction in instructions:
        dir = instruction[0]
        steps = int(instruction[1])

        for step in range(steps):
            #move head
            moveX,moveY = directions[dir]
            hx,hy = rope[0]
            rope[0] =(hx+moveX,hy+moveY)
            #move tail
            for i in range(9):
                hx,hy = rope[i]
                tx, ty = rope[i+1]
                dx = hx-tx
                dy = hy-ty
                if dx**2 + dy**2 >2:#uses euclidian distances

                    if dx != 0:
                        tx += 1 if dx >0 else -1
                    if dy != 0:
                        ty += 1 if dy >0 else -1
                    rope[i+1] =(tx,ty)
            visited.add(tuple(rope[1]))
            visitedKnot10.add(tuple(rope[9]))

move(lines,hx,hy,tx,ty)
print(len(visited))
print(len(visitedKnot10))
