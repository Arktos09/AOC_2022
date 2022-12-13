import os
import json

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

RIGHT = 1
WRONG = -1


def checkpair(a, b):
    if type(a) == type(b) == int:
        return (a < b) - (b < a)

    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]

    for newa, newb in zip(a, b):
        result = checkpair(newa, newb)
        if result:
            return result

    return (len(a) < len(b)) - (len(b) < len(a))

def part_a():

    pairs = read_input_text().split("\n\n")
    pairs = [[json.loads(y) for y in x.split("\n")] for x in pairs]

    score = 0
    for i, pair in enumerate(pairs):
        if checkpair(*pair) == RIGHT:
            score+= i + 1

    print(score)

def part_b():
    items = [json.loads(y) for y in read_input_text().split("\n") if y]
    items += [[[2]], [[6]]]

    def mergesort(items):
        n = len(items)
        itemsa, itemsb = items[:n//2], items[n//2:]
        if n > 2:
            itemsa, itemsb = mergesort(itemsa), mergesort(itemsb)

        result = [] #sorted small -> large
        while itemsa and itemsb:
            head_comp = checkpair(itemsa[0], itemsb[0])
            if head_comp == RIGHT:
                result.append(itemsa[0])
                itemsa = itemsa[1:]
            else:
                result.append(itemsb[0])
                itemsb = itemsb[1:]

        return result + itemsa + itemsb

    in_order = mergesort(items)
    jsonstrings = [json.dumps(x) for x in in_order]
    print((jsonstrings.index("[[2]]")  + 1) * (jsonstrings.index("[[6]]") + 1))

part_a()
part_b()