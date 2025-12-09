from collections import defaultdict
from common import read, parse_coords

DAY = 9

example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

input = read(DAY)

# Return a list of (area, i, j)
# where area is the area of the rectangle formed by tiles[i] and tiles[j].
# The list is sorted in descending order by area.
def find_and_sort_areas(tiles):
    areas = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            (xi, yi) = tiles[i]
            (xj, yj) = tiles[j]
            area = (abs(xi-xj) + 1) * (abs(yi-yj) + 1)
            areas.append((area, i, j))
    
    areas.sort(key=lambda x: x[0], reverse=True)

    return areas

def part_one(input):
    tiles = parse_coords(input)

    return find_and_sort_areas(tiles)[0][0]

print(part_one(example))
print(part_one(input))

# check if point (x, y) is inside polygon
# using ray tracing in the positive-y direction
def inside_polygon(horizontal, x, y):
    crossed = 0
    for y_i in horizontal:
        for (start_x, end_x) in horizontal[y_i]:
            if y_i > y and x >= start_x and x <= end_x:
                crossed += 1
    
    return crossed % 2 != 0

def part_two(input):
    tiles = parse_coords(input)

    # store edges separated by horizontal vs vertical
    # horizontal: { y-coord: [(start, end) of x interval range]}
    # similarly for vertical
    horizontal = defaultdict(list)
    vertical = defaultdict(list)

    for i in range(len(tiles) - 1):
        (x1, y1) = tiles[i]
        (x2, y2) = tiles[i+1]

        if x1 == x2:
            vertical[x1].append((min(y1, y2), max(y1, y2)))
        if y1 == y2:
            horizontal[y1].append((min(x1, x2), max(x1, x2)))

    # Iterate in descending order of area 
    # as soon as we find a valid rectangle, we know it's the max area
    areas = find_and_sort_areas(tiles)
    for (area, i, j) in areas:
        (xi, yi) = tiles[i]
        (xj, yj) = tiles[j]

        # guarantee x1 <= x2 and y1 <= y2
        x1, x2 = min(xi, xj), max(xi, xj)
        y1, y2 = min(yi, yj), max(yi, yj)

        # To check whether all points in the rectangle are inside the polygon:
        # 1. Whether any of the polygon's edges are inside the rectangle. If any
        #    are inside, then the rectangle has some points inside and some points outside
        #    the polygon, so it is not valid.
        # 2. If no edges are inside the rectangle, then the rectangle is either
        #    competely inside or completely outside the polygon. Check one interior point
        #    to determine which case it is
        valid = True

        # check if any edges cross or are inside this rectangle
        for y in horizontal:
            for (start_x, end_x) in horizontal[y]:
                if intervals_overlap_exclusive((x1, x2), (start_x, end_x)) and point_in_interval_exclusive((y1, y2), y):
                    valid = False
                    break
        
        if not valid: continue

        for x in vertical:
            for (start_y, end_y) in vertical[x]:
                if intervals_overlap_exclusive((y1, y2), (start_y, end_y)) and point_in_interval_exclusive((x1, x2), x):
                    valid = False
                    break

        if not valid: continue
        
        # check if one interior point of this rectangle
        # is inside the polygon
        if inside_polygon(horizontal, x1 + 1, y1 + 1):
            return area

# intervals that touch at the edge do not count as overlap
def intervals_overlap_exclusive(interval1, interval2):
    start1, end1 = min(interval1), max(interval1)
    start2, end2 = min(interval2), max(interval2)

    # compute the opposite - if one interval starts after the other ends,
    # then they do not overlap
    return not (start1 >= end2 or start2 >= end1)

# point that is on the edge of interval does not count
def point_in_interval_exclusive(interval, point):
    start, end = min(interval), max(interval)

    return point > start and point < end

print(part_two(example))
print(part_two(input))