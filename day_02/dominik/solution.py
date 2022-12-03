#!/usr/bin/env python3

in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()

# A X 1 Rock
# B Y 2 Paper
# C Z 3 Scissor
# lost 0 Points
# Draw 3
# Win 6

def puzzle1():
    win=["AY","BZ","CX"]
    draw=["AX","BY","CZ"]
    points_by_choice={"X":1,"Y":2,"Z":3}
    points=0
    input_list=load_input_list()
    for round in input_list:
        if round.replace(" ","") in win:
            points+=6
        elif round.replace(" ","") in draw:
            points += 3
        points+= points_by_choice[round.replace(" ","")[1]]
    return points

def puzzle2():
    combi_dict={"Z":["AB", "BC", "CA"], "Y":["AA", "BB", "CC"], "X": ["BA","CB","AC"]}
    points_by_choice = {"A": 1, "B": 2, "C": 3}
    points = 0
    input_list = load_input_list()
    for round in input_list:
        opponent,result=round.replace(" ", "")
        combi = ""

        for c in combi_dict[result]:
            if c.startswith(opponent):
                combi=c
        if result == "Z":
            points+=6
        elif result == "Y":
            points += 3
        points+= points_by_choice[combi[1]]

    return points

if __name__ == '__main__':
    a= puzzle1()
    print(f"Answer to Puzzle a is a total score of: {a}")

    b=puzzle2()
    print(f"Answer to Puzzle b is a total score of: {b}")
