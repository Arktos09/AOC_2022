import os

from collections  import defaultdict, deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    drawing, operations = read_input_text().split("\n\n")
    state = defaultdict(deque)  # {1 : deque["J", "A", "P" ...}

    for row in drawing.split("\n")[::-1]:
        for loc, symb in enumerate(row):
            if symb.isupper():
                state[(loc//4) + 1].append(symb)

    for op in operations.split("\n"):
        _, n, _, fromi, _, toi = op.split()
        for _ in range(int(n)):
            state[int(toi)].append(state[int(fromi)].pop())

    print("".join((state[i].pop() for i in range(1,10))))




def part_b():
    drawing, operations = read_input_text().split("\n\n")
    state = defaultdict(deque)

    for row in drawing.split("\n")[::-1]:
        for loc, symb in enumerate(row):
            if symb.isupper():
                state[(loc // 4) + 1].append(symb)

    for op in operations.split("\n"):
        _, n, _, fromi, _, toi = op.split()
        removed = [state[int(fromi)].pop() for _ in range(int(n))]
        state[int(toi)].extend(removed[::-1])

    print("".join((state[i].pop() for i in range(1, 10))))

part_a()
part_b()