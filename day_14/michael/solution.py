import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def drawmap():
    map = {}

    lines = read_input_lines()
    for line in lines:
        coords = []
        for coord in line.split(" -> "):
            a, b = coord.split(",")
            coords.append(int(a) + 1j * int(b))

        for pair in zip(coords[:-1], coords[1:]):
            reals, imags = sorted([x.real for x in pair]), sorted([x.imag for x in pair])
            range_real = range(int(reals[0]), int(reals[1] + 1))
            range_imag = range(int(imags[0]), int(imags[1] + 1))
            for real in range_real:
                for imag in range_imag:
                    map[real + imag * 1j] = "#"

    return map

def part_a():
    map = drawmap()
    max_y = max((coord.imag for coord in map)) # larger y than this will never stop

    ### walk
    path = [500]
    while path[-1].imag < max_y:
        for dir in [1j, 1j -1, 1j+1]:
            if (path[-1] + dir) not in map:
                path.append(path[-1] + dir) # we fall further
                break
        else: # we come to rest
            map[path.pop()] = "o"

    print(len([v for v in map.values() if v == "o"]))

def part_b():

    map = drawmap()
    max_y = max((coord.imag for coord in map))  # larger y than this will never stop

    ### walk
    path = [500]
    while path:
        if path[-1].imag == (max_y + 1): # we come to rest:
            map[path.pop()] = "o"

        for dir in [1j, 1j - 1, 1j + 1]:
            if (path[-1] + dir) not in map:
                path.append(path[-1] + dir)  # we fall further
                break
        else:  # we come to rest
            map[path.pop()] = "o"

    print(len([v for v in map.values() if v == "o"]))


part_b()
