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
all_neighbors = []
for i in lines:
    temp = find_neighbour_cubes(i[0],i[1],i[2])
    all_neighbors.extend(temp)
    for i in temp:
        if i in lines:
            count+=1
answer1 = len(lines)*6-count
print("part 1: ",answer1)

count1 = 0
all_neighbors = [str(x) for x in all_neighbors]
all_neighbors_set = set(all_neighbors)
lines_set = set([str(x) for x in lines])
#print("1",len(all_neighbors))
#print("2",len(all_neighbors_set))
air_pockets = []
for i in all_neighbors_set:
    nums = re.findall(r"[-+]?[.]?[\d]+",i)
    temp = find_neighbour_cubes(int(nums[0]),int(nums[1]),int(nums[2]))
    temp = [str(x) for x in temp]
    #print("t",temp)
    new_set = lines_set.copy()
    for d in temp:
        new_set.add(d)
    #print("newset",new_set)

    if len(new_set) == len(lines):
        nums_nums = [int(nums[0]),int(nums[1]),int(nums[2])]


        if nums_nums not in lines and nums_nums not in air_pockets:
            air_pockets.append(nums_nums)

            count1+=1

print("enclosed cubes",count1)
print(answer1 - count1*6)
#print(29*6,count1*6)
print(air_pockets)
#3402 too high - need to find more air pockets