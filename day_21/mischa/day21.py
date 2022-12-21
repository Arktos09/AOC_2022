import os
import re
from collections import deque, defaultdict
import operator
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x for x in read_input_lines()]
dict_of_monkeys = {}
#print(lines)

for i in lines:
    mon = i.split(":")
    try:
        dict_of_monkeys[mon[0]] = int(mon[1].strip())
    except:
        dict_of_monkeys[mon[0]] = mon[1].strip().split()


ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/":operator.truediv, "=": operator.eq}


not_seen = ["root"]
while len(not_seen) >0:
    monkey = not_seen[-1]
    act_monkey = dict_of_monkeys[monkey]
    left = act_monkey[0]
    right = act_monkey[2]
    if type(dict_of_monkeys[left]) == int and type(dict_of_monkeys[right]) == int:
        dict_of_monkeys[monkey] = int(ops[act_monkey[1]](dict_of_monkeys[left],dict_of_monkeys[right]))
        not_seen= not_seen[:-1]
    if type(dict_of_monkeys[left]) == list and left not in not_seen:
        not_seen.append(left)
    if type(dict_of_monkeys[right]) == list and right not in not_seen:
        not_seen.append(right)
print(dict_of_monkeys["root"])






