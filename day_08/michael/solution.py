import os
import numpy as np

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    arr = np.array([[int(x) for x in line] for line in read_input_lines()])
    visible = np.zeros(arr.shape)

    for _ in range(4): #4 rotations
        cum_max_from_top = np.maximum.accumulate(arr)
        max_size_above = np.concatenate([np.full((1,arr.shape[1]),-1), # above first row is a row of -1
                                         cum_max_from_top[:-1,:]])
        visible += (arr > max_size_above)
        arr,visible = np.rot90(arr), np.rot90(visible)

    print((visible>0).sum())


def part_b():
    arr = np.array([[int(x) for x in line] for line in read_input_lines()])
    score = np.ones(arr.shape)

    for _ in range(4):  # 4 rotations, each only looks at the right
        for y in range(arr.shape[0]): # couldnt think of a nice array method :(
            for x in range(arr.shape[1]): # :(
                dirscore = 0
                for compx in range(x+1,arr.shape[1]):
                    dirscore +=1
                    if arr[y,compx] >= arr[y,x]:
                        break
                score[y,x] *= dirscore
        arr, score = np.rot90(arr), np.rot90(score)

    print(score.max())


part_a()
part_b()