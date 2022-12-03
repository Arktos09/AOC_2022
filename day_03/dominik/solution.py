#!/usr/bin/env python3

in_file = "input.txt"

def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    backpacks= load_input_list()
    prio_sum=0
    for bag in backpacks:
        comp1, comp2=set(bag[:int(len(bag)/2)]), set(bag[int(len(bag)/2):])

        duplette=list(comp1.intersection(comp2))[0]
        if duplette.isupper():
            prio_sum+=ord(duplette)-38
        else:
            prio_sum+=ord(duplette)-96
    return prio_sum
# Unicode upper Case 65-90
# Unicode lower case 97-122
def puzzle2():
    backpacks= load_input_list()
    groups= [backpacks[x:x+3] for x in range(0, len(backpacks), 3)]
    prio_sum=0

    for g in groups:
        prio=list(set(g[0]).intersection(set(g[1])).intersection(set(g[2])))[0]
        if prio.isupper():
            prio_sum+=ord(prio)-38
        else:
            prio_sum+=ord(prio)-96
    return prio_sum
if __name__ == '__main__':
    a=puzzle1()
    print(f"Answer to puzzle a is: {a}")
    b=puzzle2()
    print(f"Answer to puzzle b is: {b}")