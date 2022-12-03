import os
import string
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


symb2score = {let:score +1 for let,score in zip(string.ascii_letters,range(52))}

def part_a():

    def get_line_score(line):
        halfway = len(line) // 2
        symbol = (set(line[:halfway]) & set(line[halfway:])).pop()
        return symb2score[symbol]

    print(sum(get_line_score(line) for line in read_input_lines()))

def part_b():

    def get_batch_score(batch):
        sets = [set(line) for line in batch]
        symbol =reduce(lambda x,y: x & y,sets).pop()
        return symb2score[symbol]

    lines = read_input_lines()
    batched_lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    print(sum(get_batch_score(batch) for batch in batched_lines))


part_a()
part_b()