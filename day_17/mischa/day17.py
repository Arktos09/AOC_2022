import os
import re
from collections import deque, defaultdict
from itertools import cycle

dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = cycle([i for i in [x for x in read_input_lines()][0]])



w = 6
initial_appears_h = 3
initial_appears_leftEdge = 2

initial_tower_height = 0
tower = set()

block1 = [(2,3),(3,3),(4,3),(5,3)]
block2 = [(2,4),(3,4),(4,4),(3,3),(3,5)]
block3 = [(2,3),(3,3),(4,3),(4,4),(4,5)]
block4 = [(2,3),(2,4),(2,5),(2,6)]
block5 = [(2,3),(3,3),(2,4),(3,4)]

blocks = cycle([block1,block2,block3,block4,block5])

jets = {"<":(-1,0),">":(1,0)}
def visualize(t):
    grid =[]
    t_h = get_tower_height(t)
    for y in range(t_h+5):
        row = []
        for x in range(7):
          row.append("_")
        grid.append(row)
    for i in t:
        grid[i[1]][i[0]] = "@"
    grid.reverse()
    for i in grid:
        print(i)
    print()

def get_tower_height(t):
    if len(t) >0:
        tower_height = [x[1] for x in t]
        return max(tower_height)+1
    return 0

def move_X(block ,pos,jet_dir):
    push = jet
    new_block = []
    for i in block:
        new_block.append((i[0]+push[0],i[1]+push[1]))
    X_pos = [x[0] for x in new_block]
    if 7 in X_pos or len(tower.intersection(new_block))>0 or -1 in X_pos:
        return block
    else:
        return new_block


def move_Y(block,step):
    new_block = []
    for i in block:
        new_block.append((i[0],i[1]-1))
    Y_pos = [x[1] for x in new_block]
    if -1 in Y_pos or len(tower.intersection(new_block))>0:
        for i in block:
            tower.add(i)
        step +=1
        return "done",block,step#returns "done when the block is at ground level or tower is hit
    else:
        return "",new_block,step

dict_of_states = dict()
tower_heights=[]
step = 0
while step <2022:
    d = ""
    act_block = next(blocks)
    hCorr_act_block = []
    t_height = get_tower_height(tower)
    for i in act_block:
        hCorr_act_block.append((i[0],i[1]+t_height))
    jet = ""
    while d != "done" :
        j = next(lines)
        jet = jets[j]
        hCorr_act_block = move_X(hCorr_act_block,0,jet)
        d, hCorr_act_block, step = move_Y(hCorr_act_block,step)
        if d == "done":
            hCorr_act_block = move_X(hCorr_act_block, 0, jet)
    tower_heights.append(get_tower_height(tower))
    if step >100:
        #print("jet",j)
        act_block_string = str(act_block).strip("[]")
        key = (j,act_block_string)
        column0 = str(max([x for x in tower if x[0] == 0]))
        column1 = str(max([x for x in tower if x[0] == 1]))
        column2= str(max([x for x in tower if x[0] == 2]))
        column3 = str(max([x for x in tower if x[0] == 3]))
        column4 = str(max([x for x in tower if x[0] == 4]))
        column5 = str(max([x for x in tower if x[0] == 5]))
        column6 = str(max([x for x in tower if x[0] == 6]))
        elevation_profile = "".join([column0,column1,column2,column3,column4,column5,column6])
        #print(key)
        if key in dict_of_states:
            prev_rock, prev_ele_profile = dict_of_states[key]
            period = step - prev_rock
            if step % period == 1_000_000_000_000 % period:
                print("period",period)
                print(prev_rock - step)
                print(tower_heights[-1])
                print("test",1514285714288/period)
        else:
            dict_of_states[key] = (step,tower_heights[-1])
#visualize(tower)
print(dict_of_states)
print("part1: ",get_tower_height(tower))

#print(tower_heights)

'''def guess_seq_len(seq):
    guess = 1
    max_len = int(len(seq) / 2)
    print("max_len",max_len)
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess

def cycle_(list):
    # list to store shortest cycles
    shortest = []
    # return single integer and non-repeating lists
    if len(list) <= 1: return list
    if len(set(list)) == len(list): return list
    # loop through the list expanding and comparing
    # groups of elements until a sequence is seen
    for x in range(len(list)):
        if list[0:x] == list[x:2*x]:
            shortest = list[0:x]
    return shortest

#print(cycle_(tower_heights))'''