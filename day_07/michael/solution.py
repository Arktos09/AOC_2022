import os

from collections import  defaultdict


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

node2node = defaultdict(set) #nodes are names "/.{node1}.{node2}... to acomodate for non unique node names
node2size = {}

node = "/"
for line in read_input_lines():
    match line.split():
        case["$", "cd", "/"]:
            node = "/"
        case["$", "cd", ".."]:
            node = ".".join(node.split(".")[:-1])
        case["$", "cd", newnode]:
            node = node + "." + newnode
        case["$", "ls"]:
            pass
        case[size, name]:
            node2node[node].add(node + "." + name)
            if size != "dir":
                node2size[node + "." + name] = int(size)

def recursive_size_solver(node):
    for lowernode in node2node[node]:
        if not lowernode in node2size:
            recursive_size_solver(lowernode)

    node2size[node] = sum((node2size[lowernode] for lowernode in  node2node[node]))

recursive_size_solver("/")


def part_a():
    print(sum((val for name,val in node2size.items() if val <=100000 and name in node2node )))

def part_b():
    required = (30000000 +  node2size["/"]) - 70000000
    print(min((val for name,val in node2size.items() if val >=required and name in node2node )))

part_a()
part_b()