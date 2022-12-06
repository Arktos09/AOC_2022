import os
import re
import pandas as pd
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x for x in read_input_text()]


count = 1
lineCounter = 36
df = pd.DataFrame(columns = [1,2,3,4,5,6,7,8,9],index= [0,1,2,3,4,5,6,7])
for i in [0,1,2,3,4,5,6,7]:
    for x in [0,1,2,3,4,5,6,7,8]:
        if lines[count].isalpha():
            df.iloc[i,x] = lines[count]
        else:
            df.iloc[i,x] = ""
        count +=4

list_of_stacks = []
for i in [1,2,3,4,5,6,7,8,9]:
    stack = [x for x in df[i] if x.isalpha()][::-1]
    list_of_stacks.append(stack)

def move(stacks,amount,stackSource,stackTarget):
    tempStack = []
    for i in range(amount):
        tempStack.append(stacks[stackSource].pop())
    tempStack = tempStack
    stacks[stackTarget].extend(tempStack)

instructions = [x for x in read_input_lines() if x.startswith("move")]

for i in instructions:
    a,b,c = re.findall('[0-9]+', i)
    move(list_of_stacks, int(a), int(b)-1, int(c)-1)

part1 = [x[-1] for x in list_of_stacks]
print("part1 :", "".join(part1))

'''
part2
'''

count = 1
lineCounter = 36
df = pd.DataFrame(columns = [1,2,3,4,5,6,7,8,9],index= [0,1,2,3,4,5,6,7])
for i in [0,1,2,3,4,5,6,7]:
    for x in [0,1,2,3,4,5,6,7,8]:
        if lines[count].isalpha():
            df.iloc[i,x] = lines[count]
        else:
            df.iloc[i,x] = ""
        count +=4

list_of_stacks = []
for i in [1,2,3,4,5,6,7,8,9]:
    stack = [x for x in df[i] if x.isalpha()][::-1]
    list_of_stacks.append(stack)

def move(stacks,amount,stackSource,stackTarget):
    tempStack = []
    for i in range(amount):
        tempStack.append(stacks[stackSource].pop())
    tempStack = tempStack[::-1]
    stacks[stackTarget].extend(tempStack)

instructions = [x for x in read_input_lines() if x.startswith("move")]

for i in instructions:
    a,b,c = re.findall('[0-9]+', i)
    move(list_of_stacks, int(a), int(b)-1, int(c)-1)

part1 = [x[-1] for x in list_of_stacks]
print("part1 :", "".join(part1))day05.py