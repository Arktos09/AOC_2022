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
    def score(a, b):
        shape_score = (ord(b) + 1 - ord("X"))
        outcome_score = {2: 3, 0: 6, 1: 0}[(ord(b) - ord(a)) % 3]  #
        return shape_score + outcome_score

    lines = read_input_lines()
    print(sum((score(*line.split()) for line in lines)))

def part_b():

    def score(a, b):
        offset = ord(b) - ord("Y")  # -1 lost, 0 draw, +1 win
        shape_score = ((ord(a) + offset - ord("A")) % 3) + 1
        outcome_score = offset * 3 + 3
        return shape_score + outcome_score

    lines = read_input_lines()
    print(sum((score(*line.split()) for line in lines)))

part_a()
part_b()