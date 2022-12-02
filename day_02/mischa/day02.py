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

lines = [x.split(" ") for x in read_input_lines()]

scores = []
for i in lines:
    score1 = 0
    score2 = 0
    if i[1] == "X":
        score1 = 1
        if i[0] == "A":
            score2 = 3
        elif i[0] == "C":
            score2 = 6
        else:
            score2 = 0
    elif i[1] == "Y":
        score1 = 2
        if i[0] == "B":
            score2 = 3
        elif i[0] == "A":
            score2 = 6
        else:
            score2 = 0
    else:
        score1 = 3
        if i[0] == "C":
            score2 = 3
        elif i[0] == "B":
            score2 = 6
        else:
            score2 = 0
    scores.append(score1+score2)

print("part 1: ",sum(scores))


scores = []
for i in lines:
    score1 = 0
    score2 = 0
    if i[1] == "X":
        score2 = 0
        if i[0] == "A":
            score1 = 3
        elif i[0] == "B":
            score1 = 1
        else:
            score1 = 2
    elif i[1] == "Y":
        score2 = 3
        if i[0] == "A":
            score1 = 1
        elif i[0] == "B":
            score1 = 2
        else:
            score1 = 3
    else:
        score2 = 6
        if i[0] == "A":
            score1 = 2
        elif i[0] == "B":
            score1 = 3
        else:
            score1 = 1
    scores.append(score1+score2)

print("part 2: ",sum(scores))