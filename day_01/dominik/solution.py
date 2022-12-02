#!/usr/bin/env python3

in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    food_list=read_input_text()
    food_list=food_list.replace("\n",",").split(",,")
    calories_list=[]
    for elve in food_list:
        calories=0
        snacks=elve.split(",")
        for snack in snacks:
            calories += int(snack)
        calories_list.append(calories)
    return calories_list



def puzzle2():
    calorie_list=sorted(puzzle1())
    return sum(calorie_list[-3:])


if __name__ == '__main__':
    a=puzzle1()
    print(f"Answer to Puzzle a is: {max(a)} calories")

    b=puzzle2()
    print(f"Answer to Puzzle b is: {b} calories")