def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]


filename = 'debug'
# filename = 'day_4_1.txt'

puzzle_list = get_fileinput(filename)


def get_ranges(linst_input: list) -> list:

    pairs = [pair.split(',') for pair in linst_input]
    return [[list(map(int, i.split('-'))) for i in p] for p in pairs]


def joiner(list_input: list) -> list:

    joined = ''.join([str(item)
                     for item in range(list_input[0], list_input[-1]+1, 1)])
    return joined


def extract_ranges(list_input: list) -> list:

    pair_range = [[joiner(pair) for pair in pairs] for pairs in list_input]
    return pair_range


def simple_comparer(list_input: list) -> int:

    if list_input[0] in list_input[1] or list_input[1] in list_input[0]:
        counter = 1
    else:
        counter = 0
    print(list_input[0], list_input[1], counter)
    return counter


def counter(list_input: list) -> int:

    return sum([simple_comparer(pair) for pair in list_input])


def ranger(list_input: list) -> range:
    return range(list_input[0], list_input[-1], 1)


def set_comparer(list_input: list) -> int:

    if set(list_input[0]).issubset(list_input[1]):
        counter = 1
    elif set(list_input[1]).issubset(list_input[0]):
        counter = 1
    else:
        counter = 0

    return counter





def get_range_pairs(list_input: list) -> list:
    return [set_comparer([ranger(p) for p in pair]) for pair in [pairs for pairs in list_input]]


ranges = get_ranges(puzzle_list)
str_ranges = extract_ranges(ranges)

print(counter(str_ranges))
print(sum(get_range_pairs(ranges)))
