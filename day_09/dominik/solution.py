#!/usr/bin/env python3
from copy import copy

import numpy as np
import math
in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    movements=load_input_list()

    array_size=(250,500)

    direction_dir = {
        "R": np.array((0, 1)),
        "U": np.array((-1, 0)),
        "D": np.array((1, 0)),
        "L": np.array((0,-1))
        }

    map_arr=np.zeros(array_size, dtype=str)
    counter_arr=np.zeros(array_size, dtype=int)
    # set origin of the map
    origin=np.asarray([map_arr.shape[0]//2,map_arr.shape[1]//2])
    map_arr[origin[0],origin[1]] = "s"

    counter_arr[origin[0],origin[1]] = 1

    curr_head_pos = origin.copy()# otherwise it will be overwritten, since it is an array
    curr_tail_pos= origin.copy()

    for i, movement in enumerate(movements):
        direction,steps= movement.split(" ")

        for n in range(int(steps)):
            map_arr[curr_tail_pos[0], curr_tail_pos[1]] = ""
            map_arr[curr_head_pos[0], curr_head_pos[1]] = ""
            # get new position of the head
            old_head_pos=curr_head_pos.copy()
            curr_head_pos+=direction_dir[direction]
            # set new position of head
            map_arr[(curr_head_pos[0], curr_head_pos[1])] = "H"

            # get head tail distance
            dist=math.sqrt(sum((curr_head_pos-curr_tail_pos)**2))
            # drag tail behind head
            if dist>1.4142135623730951:
                curr_tail_pos=old_head_pos
            map_arr[(curr_tail_pos[0], curr_tail_pos[1])] = "T"
            counter_arr[(curr_tail_pos[0], curr_tail_pos[1])]=1

        # keep origin marker alive
        map_arr[origin[0], origin[1]] = "s"

    return counter_arr.sum()

def puzzle2():
    movements = load_input_list()

    array_size=(250,500)

    direction_dir = {
        "R": np.array((0, 1)),
        "U": np.array((-1, 0)),
        "D": np.array((1, 0)),
        "L": np.array((0, -1))
        }

    map_arr = np.zeros(array_size, dtype=str)
    counter_arr = np.zeros(array_size, dtype=int)
    # set origin of the map
    origin = np.asarray([map_arr.shape[0] // 2, map_arr.shape[1] // 2])
    #origin=[9,0]
    map_arr[origin[0], origin[1]] = "s"

    counter_arr[origin[0], origin[1]] = 1

    # set up position dict

    knot_list=[x for x in range(0,10,1)]
    origin_list=[origin]*11
    knot_dict=dict(zip(knot_list,origin_list))
    #print(knot_dict)

    curr_tail_pos = origin.copy()
    old_head_pos = origin.copy()
    for i, movement in enumerate(movements):
        direction, steps = movement.split(" ")
        #print(movement)
        for n in range(int(steps)):

            for knot, pos in knot_dict.items():

                # index 0 == H
                if knot == 0:
                    old_head_pos = copy(pos)
                    map_arr[(knot_dict[0][0], knot_dict[0][1])] = ""
                    knot_dict[0] += direction_dir[direction]
                    map_arr[(knot_dict[0][0], knot_dict[0][1])] = "H"
                else:
                    #print(knot, old_head_pos)
                    # get head tail distance
                    map_arr[(pos[0], pos[1])] = ""
                    dist = math.sqrt(sum(np.subtract(knot_dict[knot-1] , knot_dict[knot]) ** 2))
                    #print("Distance to previous knot:",knot,knot_dict[knot], dist)
                    if dist > 1.4142135623730951:
                        knot_dict[knot] = copy(old_head_pos)
                    map_arr[(knot_dict[knot][0], knot_dict[knot][1])] = f"{knot}"
                    if knot==9:
                        counter_arr[(knot_dict[knot][0], knot_dict[knot][1])] = 1
                    old_head_pos = copy(pos)
            #print(map_arr)
            # set new position of head
        # keep origin marker alive
        map_arr[origin[0], origin[1]] = "s"
        #print(map_arr)
        #print(counter_arr)

        # keep origin marker alive
        map_arr[origin[0], origin[1]] = "s"

    return counter_arr.sum()



if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle: {a}")

    b = puzzle2()
    print(f"Answer to Puzzle: {b} Still Error")