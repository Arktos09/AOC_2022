import os
import math

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():

    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    dirs = {"U": -1, "D": 1, "L": -1 * 1j, "R" : 1j}

    h = 0
    t = 0
    visited = {0.0}
    for dir, n in  (line.split() for line in read_input_lines()):
        for step in range(int(n)):
            h+= dirs[dir]
            if abs((h-t).real) > 1:
                t += ((h-t).real // 2)
                t += 1j * ((h - t).imag)
            if abs((h-t).imag) > 1:
                t += 1j * ((h-t).imag // 2)
                t+= ((h-t).real)
            visited.add(t)

    print(len(visited))

def part_b():
    dirs = {"U": -1, "D": 1, "L": -1 * 1j, "R": 1j}

    rope = [0] * 10

    visited = {0.0}
    for dir, n in (line.split() for line in read_input_lines()):
        for step in range(int(n)):
            rope[0] +=  dirs[dir]
            for tailix in range(1,10):
                dif = rope[tailix-1] - rope[tailix]
                if max(abs(dif.real), abs(dif.imag)) > 1:
                    if abs(dif.real) > 0:
                        rope[tailix] += math.copysign(1,dif.real)
                    if abs(dif.imag) > 0:
                        rope[tailix] += 1j * math.copysign(1,dif.imag)

            visited.add(rope[-1])


    print(len(visited))

part_a()
part_b()