from collections import defaultdict
from itertools import groupby
import re


def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip('\n') for x in content]


def get_stackpole(stack_puzzle: list) -> list:

    stackpole = []
    for crates in stack_puzzle[::-1]:
        crates = re.sub(r'^\D\W\S', '', crates)
        crates = crates.replace('    ', ' ').split(' ')
        #crates = crates.replace('  ', ' ')
        try:
            crates = [int(x) for x in crates if x]
        except:
            crates = crates
        stackpole.append(crates)
    return stackpole


filename = 'debug.txt'
# filename = 'day_4_1.txt'
puzzle_list = get_fileinput(filename)
stack_commands = [list(g) for k, g in groupby(puzzle_list, key=bool) if k]
stackpole = get_stackpole(stack_commands[0])
commands = [list(map(int, re.sub(r'\D', '', command)))
            for command in stack_commands[1]]

stack_command_dict = defaultdict(list)
for stack in stackpole[0]:
    for crates in stackpole[1:]:
        stack_command_dict[stack].append(crates[stack-1])

for key, value in stack_command_dict.items():
    stack_command_dict[key] = list(filter(None, value))

# print(stack_command_dict)


def crane(command: list) -> dict:

    from collections import Counter
    cmd_reversed = command[::-1]
    # stack_command_copy = stack_command_dict.copy()
    moving_stacks = stack_command_dict[cmd_reversed[1]][::-1][:cmd_reversed[2]]
    stack_command_dict[cmd_reversed[0]
                       ] = stack_command_dict[cmd_reversed[0]]+moving_stacks
    stack_command_dict[cmd_reversed[1]] = list(
        Counter(stack_command_dict[cmd_reversed[1]]) - Counter(moving_stacks))
    return stack_command_dict


for command in commands:
    crane(command)

Top_crates = ''.join([value[-1] for value in stack_command_dict.values() if value])

print(re.sub(r'[^A-Za-z]','',Top_crates))
