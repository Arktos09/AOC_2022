import os


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)
import numpy as np

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    ints = [int(x) for x in read_input_lines()] # ints are not unique and rotation values are large
    ints = [int(x) for x in """1
2
-3
3
-2
0
4""".split("\n")]
    originalix2pos = np.arange(0,len(ints))

    for i in range(len(ints)):
        num, pos = ints[i],originalix2pos[i]
        new_pos = (pos + num) % len(ints)
        print(i, num, pos,  new_pos)

        effective_move = num % len(ints)
        new_pos_unbounded = pos + effective_move


        range_unbounded = np.arange(pos+1,new_pos_unbounded + 1 ) if new_pos_unbounded > pos else np.arange(new_pos_unbounded,pos)
        range_bounded = range_unbounded % len(ints)
        originalix2pos[range_bounded] += (-1 if num > 0 else 1)
        originalix2pos[i] = new_pos
        originalix2pos %= len(ints)

        print([ints[i] for i in sorted(range(len(ints)), key = lambda x: originalix2pos[x])])

    print(len(set(originalix2pos.values())))
    zeroix = originalix2pos[ints.index(0)]
    print(sum(ints[k] for k,v in originalix2pos.items() if v in [(zeroix+x)% len(ints) for x in [1000,2000,3000]]))


part_a()
def part_b():
    pass