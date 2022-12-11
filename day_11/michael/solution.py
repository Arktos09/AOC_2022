import os
import re
from math import prod
CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

class Monkey:

    def __init__(self, input):
        _, items, op, test, out_t, out_f = input.split("\n")
        self.items = [int(x) for x in re.findall(r"\d+", items)]
        self.op = eval("lambda old: " + op.split("=")[-1])
        self.test = int(test.split()[-1])
        self.out_t = int(out_t.split()[-1])
        self.out_f = int(out_f.split()[-1])
        self.score = 0
        self.reduce = lambda x: x//3

    def __call__(self):
        for item in self.items:
            item = self.reduce(self.op(item))
            monkey_out = self.out_f if item % self.test else self.out_t
            monkeys[monkey_out].items.append(item)
            self.score +=1
        self.items = []

# part 1
monkeys = [Monkey(x) for x in read_input_text().split("\n\n")]
for _ in range(20):
    for monkey in monkeys:
        monkey()

print(prod(sorted([m.score for m in monkeys])[-2:]))

# part 2
monkeys = [Monkey(x) for x in read_input_text().split("\n\n")]
total_mod = prod([m.test for m in monkeys]) # idea is that we can always do item%total mod because it does not affect any test
for m in monkeys:
    m.reduce = lambda x: x%total_mod

for _ in range(10000):
    for monkey in monkeys:
        monkey()

print(prod(sorted([m.score for m in monkeys])[-2:]))
