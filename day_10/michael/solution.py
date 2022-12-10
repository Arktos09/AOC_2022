import os


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

x = 1
t = 1
t2x = {1:1}
for inst in read_input_lines():
    match inst.split():
        case["noop"]:
            t+=1
        case['addx', num]:
            t2x[t+1] = x
            x += int(num)
            t+=2
    t2x[t] = x

def part_a():

    print(sum((t2x[t] * t for t in range(20,221,40))))

part_a()
def part_b():
    for start in range(1,221, 40):
        print("".join("#" if abs(t2x[t] - pos) <= 1 else "." for pos,t in enumerate(range(start, start+40))))

part_b()