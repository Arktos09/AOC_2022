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

lines = [x for x in read_input_lines()]

for i in lines:
    if len(i)%2 !=0:
        print(i,len(i))

item_list = []
for i in lines:
    a = i[0:len(i)//2]
    b = i[len(i)//2:]
    item = list(set(a)&set(b))[0]
    if item.lower() == item:
        prio = ord(item)-96
    else:
        prio = ord(item)-38
    item_list.append(prio)
print("part 1: ",sum(item_list))

item_list = []
while len(lines)>2:
    group = lines[0:3]
    lines = lines[3:]
    item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
    if item.lower() == item:
        prio = ord(item)-96
    else:
        prio = ord(item)-38
    item_list.append(prio)
print("part 2: ",sum(item_list))

