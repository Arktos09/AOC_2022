import os
from functools import cache
from scipy.optimize import minimize_scalar
CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)
from collections import defaultdict

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    monkeys = {line.split(":")[0] : line.split(":")[1] for line in read_input_lines()}

    @cache
    def recurse(monkey):
        try:
            return int(monkeys[monkey])
        except:
            m1, op, m2 = monkeys[monkey].split()
            return eval (f"{recurse(m1)} {op} {recurse(m2)}")

    print(recurse("root"))

#part_a()
def part_b():
    monkeys = {line.split(":")[0]: line.split(":")[1] for line in read_input_lines()}
    monkeys['root'] = "wdzt - dffc"
    monkey_results = {"root": 0}
    monkey2parent = {} # every monkey only has 1 parent
    for m, txt in monkeys.items():
        if len(txt.split()) == 3:
            m1, op, m2 = txt.split()
            monkey2parent[m1] = m
            monkey2parent[m2] = m

    def recursedown(monkey):
        if monkey == "humn": return 1j
        try:
            res = int(monkeys[monkey])
            monkey_results[monkey] = res
            return res

        except:
            m1, op, m2 = monkeys[monkey].split()
            res = eval(f"{recursedown(m1)} {op} {recursedown(m2)}")
            monkey_results[monkey] = res
            return res

    def recurseup(monkey):
        parent = monkey2parent[monkey]
        if type(monkey_results[parent]) != int:
            recurseup(parent)

        parent_val = monkey_results[parent]
        m1, op, m2 = monkeys[parent].split()
        i_am_m1 = m1 == monkey
        match [op, i_am_m1]:
            case ["+", True]:
                res = parent_val - monkey_results[m2]
            case ["+", False]:
                res = parent_val - monkey_results[m1]
            case ["-", True]:
                res = parent_val + monkey_results[m2]
            case ["-", False]:
                res =  monkey_results[m1] - parent_val
            case ["*", True]:
                res = parent_val / monkey_results[m2]
            case ["*", False]:
                res = parent_val / monkey_results[m1]
            case ["/", True]:
                res = parent_val * monkey_results[m2]
            case ["/", False]:
                res = monkey_results[m1] / parent_val

        monkey_results[monkey] = res


    recursedown("root")
    monkey_results["root"] = 0
    recurseup("humn")

    print(monkey_results["humn"])


part_b()
