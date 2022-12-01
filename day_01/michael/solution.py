import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    txt = read_input_text()
    print(max(sum((int(num) for num in chunk.split("\n"))) for chunk in txt.split("\n\n") ))

def part_b():
    txt = read_input_text()
    print(sum(sorted([sum((int(num) for num in chunk.split("\n"))) for chunk in txt.split("\n\n")])[-3:]))

part_a()
part_b()