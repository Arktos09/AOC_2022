import os
import re
from collections import deque, defaultdict
import pandas as pd
import numpy as np
from operator  import sub,add
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


data = read_input_lines()
instructions = data[-1]
instructions = re.split('(\d+)', instructions)
instructions.pop()
instructions.pop(0)


grid = []
WALL, FREE, EMPTY = '#._'
with open("input.txt") as fin:
    grid  = fin.read().splitlines()
    moves = grid[-1]  # Take last line with movement instructions.
    grid  = grid[:-2] # Throw away last two lines.

HEIGHT, WIDTH = len(grid), max(map(len, grid))

for i in range(HEIGHT):
    grid[i] = grid[i].ljust(WIDTH, EMPTY)

for i in range(HEIGHT):
    # Add two empty columns left and right.
    grid[i] = EMPTY + grid[i].ljust(WIDTH, EMPTY) + EMPTY

HEIGHT += 2
WIDTH  += 2

# Add two empty rows at the top and at the bottom.
grid = [EMPTY * WIDTH] + grid + [EMPTY * WIDTH]
data = [[i for i in x] for x in grid[:][:]]
df = pd.DataFrame(data)
df=df.replace(" ", "_")
df_show = df.copy()
pos = (1,1)
facing = "right"
facing_show = ">"
face_dict = {"right": (1,0),"left":(-1,0),"up":(0,-1),"down":(0,1)}
face_order = ["right","down","left","up"]

def change_facing(clock_dir,facing):
    p = face_order.index(facing)

    if clock_dir =="R" and facing !="up":
        facing=face_order[p + 1]
        #print(face_order[p + 1])
    elif clock_dir =="R":
        facing = face_order[0]
        #print(face_order[0])

    if clock_dir =="L" and facing !="right":
        facing = face_order[p - 1]
        #print(face_order[p - 1])
    elif clock_dir == "L":
        facing = face_order[3]
        #print(face_order[3])
    return facing
#find start pos
pos = ([x for x in enumerate(df.loc[1][:]) if x[1]=="."][0][0],1)
#print(pos)

for i in instructions:
    #print("instruction: ",i)
    if i.isnumeric():
        for step in range(int(i)):
            #print("step ",step)
            mover = face_dict[facing]
            pos = np.add(pos, mover)

            #if i hit a wall stop moving
            if df[pos[0]][pos[1]] == "#":
                pos = np.subtract(pos, mover)
                #print(pos[0], pos[1])
                #print(df[pos[0]][pos[1]])
                break
            # if i hit a outer boundary i have to loop to the other side
            if df[pos[0]][pos[1]] == "_":
                pos = np.subtract(pos, mover)
                #print("loop at",pos)
                if facing == "right":
                    # find the first dot in row
                    #this puts me on the outer boundaries so i can check if the first field is a wall but it probalby makes weird edge cases were i move outside the grid....
                    prelim_pos = ([x for x in enumerate(df.loc[pos[1]][:]) if x[1] != "_"][0][0], pos[1])
                    if df[prelim_pos[0]][prelim_pos[1]] == ".":
                        pos = (prelim_pos[0]-1,prelim_pos[1])
                        pos = np.add(pos, mover)
                    #this works
                if facing == "left":
                    # find the first dot in row
                    #print([x for x in enumerate(df.loc[pos[1]][:]) if x[1] != "_"])
                    #print([x for x in enumerate(df.loc[pos[1]][:]) if x[1] != "_"][-1])
                    prelim_pos = ([x for x in enumerate(df.loc[pos[1]][:]) if x[1] != "_"][-1][0], pos[1])
                    if df[prelim_pos[0]][prelim_pos[1]] == ".":
                        pos = (prelim_pos[0] + 1, prelim_pos[1])
                        pos = np.add(pos, mover)
                    # this works

                if facing == "down":
                    # find the first dot in column
                    #print([x for x in enumerate(df.loc[:][pos[0]]) if x[1]=="."])
                    #print(df.loc[:, pos[0]])
                    prelim_pos = (pos[0],[x for x in enumerate(df.loc[:][pos[0]]) if x[1]!="_"][0][0])
                    if df[prelim_pos[0]][prelim_pos[1]] == ".":
                        pos = prelim_pos

                if facing == "up":
                    # find the first dot in column
                    #print([x for x in enumerate(df.loc[:][pos[0]]) if x[1]=="."])
                    #print(df.loc[:, pos[0]])
                    prelim_pos = (pos[0],[x for x in enumerate(df.loc[:][pos[0]]) if x[1]!="_"][-1][0])
                    if df[prelim_pos[0]][prelim_pos[1]] == ".":
                        pos = prelim_pos

            #print(pos[0], pos[1])
            #print(df[pos[0]][pos[1]])
            #print(facing)
            #df_show[pos[0]][pos[1]] = "@"
            #print(df_show)

        #move in direction of facing
    else:
        #change facing
        facing = change_facing(i,facing)

        #print(facing)
print(pos,facing)
face_add = 0
if facing == "down":
    face_add =1
if facing =="left":
    face_add = 2
if facing == "up":
    face_add =3
print(pos[0]*4+pos[1]*1000+face_add)
# 62*4 +58*1000+0 right == 58248


