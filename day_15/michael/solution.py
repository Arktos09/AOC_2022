import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines_test():
    return """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")


os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():

    special_row = 2000000
    beacons_special_row = set()
    lines = read_input_lines()

    # get ranges of points on relevant line
    y2000000ranges = []
    for line in [line for line in lines if line]:
        sx, sy, bx,by = [int("".join([let for let in x.split("=")[-1] if let.isdigit() or let == '-'])) for x in line.split() if "=" in x]
        dist = abs(sx-bx) + abs(sy-by)
        y2000000_width_one_side = dist - abs(sy - special_row)
        if y2000000_width_one_side >= 0: # 0 means we have a single point
            y2000000ranges.append((sx-y2000000_width_one_side, sx + y2000000_width_one_side))
        if by == special_row:
            beacons_special_row.add((bx,by))

    # merge ranges where possible
    y2000000ranges = sorted(y2000000ranges)
    merged_ranges = []

    minx, maxx = y2000000ranges[0]
    for x,x2 in y2000000ranges[1:]:
        if x <= maxx: # start falls in prev range
            if x2 > maxx:
                maxx = x2
            #else we already cover the entire range
        else:
            merged_ranges.append((minx, maxx))
            minx, maxx = x, x2
    merged_ranges.append((minx, maxx))
    print(sum([x2  + 1- x for x, x2 in merged_ranges] ) - len(beacons_special_row))

part_a()
def part_b():
    """idea: we only need to check the rim coordinates around avery sensor area. because we know there is only one unchecked spot
       possible optimization: early exclusion on cells outside range and """

    def check_covered(x,y):
        for sx, sy, dist in covered_areas:
            if (abs(x-sx) + abs(y-sy)) <= dist:
                return True

    def get_coords_of_interest(sx,sy,dist):
        dist+=1 # we are actually interested 1 stop beyond the sensor range
        for xdir, ydir in [(1,1),(-1,1),(-1,-1),(1,-1)]:
            for y_part in range(dist+1):
                x_offset = (dist - y_part) * xdir
                y_offset = y_part * ydir
                yield (sx + x_offset, sy + y_offset)


    lines = read_input_lines()

    covered_areas = [] # tuples of sensors x,y,distance covered
    for line in [line for line in lines if line]:
        sx, sy, bx,by = [int("".join([let for let in x.split("=")[-1] if let.isdigit() or let == '-'])) for x in line.split() if "=" in x]
        dist = abs(sx-bx) + abs(sy-by)
        covered_areas.append((sx,sy,dist))

    for area in covered_areas:
        for poi in get_coords_of_interest(*area):
            if not check_covered(*poi):
                if all( 0 <= coord <= 4000000 for coord in poi):
                    print(poi)
                    print(poi[0] * 4000000 + poi[1])
                    return




part_b()
