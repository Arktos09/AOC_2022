#!/usr/bin/env python3
import sys

in_file = "input.txt"
import re
import numpy as np

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


class Monkey():
    def __init__(self, name, starting_items, operation, test, test_true, test_false):
        self.name = name
        self.items = [int(x) for x in starting_items.split(",")]
        self.operation = operation
        self.test = int(test)
        self.test_true = int(test_true)
        self.test_false = int(test_false)
        self.__remove_items_list=[]
        self.inspection_counter=0

    def inspect_item(self, worry_level_old):
        operator, number=self.operation.split(" ")
        if number == "old":
            number=worry_level_old
        worry_level_new = eval(f"{worry_level_old}{operator}{number}")
        self.__remove_items_list.append(worry_level_old)
        self.inspection_counter+=1
        return worry_level_new

    def throw_item_to_monkey_x(self, worry_level):
        new_worry_level= worry_level // 3
        if  new_worry_level % self.test == 0:
            return self.test_true, new_worry_level
        else:
            return self.test_false, new_worry_level

    def throw_item_to_monkey_x_2(self, worry_level):
        new_worry_level = worry_level
        if  new_worry_level % self.test == 0:
            return self.test_true, new_worry_level
        else:
            return self.test_false, new_worry_level

    def clean_inventory(self):
        for item in self.__remove_items_list:
            self.items.remove(item)
        self.__remove_items_list=[]

def create_the_monkey_house():
    monkey_str = read_input_text()
    monkey_list = monkey_str.split("\n\n")
    monkey_dict = {}
    regex = r"(\w+ \d):\n  Starting items: (.+)\n  Operation: new = old (.+)\n  Test: divisible by (.+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"

    for monkey in monkey_list:
        matches = re.findall(regex, monkey, re.MULTILINE)
        matches = matches[0]
        monkey_dict[matches[0]] = Monkey(name=matches[0], starting_items=matches[1], operation=matches[2], test=matches[3], test_true=matches[4], test_false=matches[5])

    return monkey_dict

def puzzle1():
    monkey_dict=create_the_monkey_house()

    for round in range(1,21,1):
        for monkey_name in monkey_dict.keys():
            active_monkey=monkey_dict[monkey_name]
            for worry_level in active_monkey.items:
                # get new worry level after inspection by monkey
                worry_level=active_monkey.inspect_item(worry_level)
                # append item to item list of other monkeys
                throw_to, new_worry_level=active_monkey.throw_item_to_monkey_x(worry_level)
                monkey_dict[f"Monkey {throw_to}"].items.append(new_worry_level)
            active_monkey.clean_inventory()

    result=[]
    for monkey in monkey_dict.values():
        result.append(monkey.inspection_counter)

    return np.product(sorted(result)[-2:])


def puzzle2():
    monkey_dict = create_the_monkey_house()
    for round in range(1, 10001, 1):
        for monkey_name in monkey_dict.keys():
            active_monkey = monkey_dict[monkey_name]
            # print(active_monkey.name)
            # print(active_monkey.items)
            for worry_level in active_monkey.items:
                # get new worry level after inspection by monkey
                worry_level = active_monkey.inspect_item(worry_level)
                # append item to item list of other monkeys
                throw_to, new_worry_level = active_monkey.throw_item_to_monkey_x_2(worry_level)
                # print(f"Throw to monkey {throw_to} with worry level {new_worry_level}")
                monkey_dict[f"Monkey {throw_to}"].items.append(new_worry_level)
            print(round, monkey_name, active_monkey.inspection_counter)
            active_monkey.clean_inventory()

    result = []
    for monkey in monkey_dict.values():
        result.append(monkey.inspection_counter)

    return np.product(sorted(result)[-2:])


if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle: {a}")

    b = puzzle2()
    print(f"Answer to Puzzle: {b}")
