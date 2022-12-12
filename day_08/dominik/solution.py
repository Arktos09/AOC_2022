#!/usr/bin/env python3
import numpy as np

in_file = "input.txt"


def load_input_list():
    with open(in_file, 'r') as f:
        return [[int(d) for d in line.rstrip('\n')] for line in f]


def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()


def puzzle1():
    forest = np.asarray(load_input_list())
    forest_map = np.zeros(forest.shape, dtype=int)

    # print(forest)

    def forest_parser(forest, forest_map):
        n_rows, n_cols = forest.shape
        # parse array row wise
        for i_row, tree_row in enumerate(forest):
            # set rim to visible
            if i_row == 0 or i_row == n_rows - 1:
                forest_map[i_row] = 1
            else:
                forest_map = set_visibility(line=tree_row, i_line=i_row, n_lines=n_rows, axis=0)

        # parse array column wise
        for i_col, tree_col in enumerate(forest.T):
            # set rim to visible
            if i_col == 0 or i_col == n_rows - 1:
                continue
            else:
                forest_map = set_visibility(line=tree_col, i_line=i_col, n_lines=n_cols, axis=1)

        return forest_map

    def set_visibility(line, i_line, n_lines, axis=0):
        # make line of sight arrays
        left_to_right = [line[0:x + 2] for x in range(0, len(line) - 1, 1)]
        right_to_left = [np.flip(line)[0:x + 2] for x in range(0, len(line) - 1, 1)]

        for i_dir, direction in enumerate([left_to_right, right_to_left]):

            for tree_line in direction:

                for i_tree, tree in enumerate(tree_line):
                    # set first tree of row as visible

                    if i_dir == 0:
                        tree_replace = i_tree
                    else:
                        tree_replace = n_lines - 1 - i_tree

                    if i_tree == 0:
                        if axis == 0:
                            forest_map[i_line, tree_replace] = 1
                        else:
                            forest_map[tree_replace, i_line] = 1
                    # set visible trees
                    elif list(tree_line).count(max(tree_line)) == 1 and tree == max(tree_line):
                        if axis == 0:
                            forest_map[i_line, tree_replace] = 1
                        else:
                            forest_map[tree_replace, i_line] = 1

        return forest_map

    forest_map = forest_parser(forest, forest_map)

    return np.sum(forest_map)


def puzzle2():
    forest = np.asarray(load_input_list())
    forest_map = np.zeros(forest.shape, dtype=int)
    scenic_score_map = np.ones(forest.shape, dtype=int)
    print(forest)

    for index, tree in np.ndenumerate(forest):
        row = forest[index[0]]
        column = forest[:, index[1]]

        tree_counter = 0
        scenic_score = []

        right = row[index[1] + 1:]
        left = list(reversed(row[0:index[1]]))
        down = column[index[0] + 1:]
        up = list(reversed(column[0:index[0]]))

        for dir in [left, right, down, up]:
            tree_counter_temp = 0

            if len(dir) == 0:
                scenic_score.append(0)
                continue
            else:
                for i, val in enumerate(dir):
                    if len(dir) == 1:

                        tree_counter += 1
                        tree_counter_temp += 1
                        break
                    elif i == len(dir)-1:

                        tree_counter += len(dir)
                        tree_counter_temp += len(dir)
                        break
                    elif val >= tree or val == max(dir):

                        tree_counter += i+1
                        tree_counter_temp += i+1
                        if dir[i+1] == val:
                            tree_counter += 1
                            tree_counter_temp += 1
                        break
                    else: continue
                scenic_score.append(tree_counter_temp)

        scenic_score_map[index] = np.product(scenic_score)
        forest_map[index] = tree_counter

    print(forest_map)
    print(scenic_score_map)
    return np.max(scenic_score_map)


if __name__ == '__main__':
    #a = puzzle1()
    #print(f"Answer to Puzzle: {a}")

    b = puzzle2()
    print(f"Answer to Puzzle: {b}, falsch: 7200,432, 1097600, 227240, 82080")
