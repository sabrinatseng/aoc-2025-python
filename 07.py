from common import read

DAY = 7

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input = read(DAY)

class Map:
    def __init__(self, input):
        lines = input.splitlines()

        self.height = len(lines)
        self.width = len(lines[0])
        self.splitters = set()
        self.start = None

        for i in range(self.height):
            for j in range(self.width):
                if lines[i][j] == 'S':
                    self.start = j # assumed to be on line 0
                elif lines[i][j] == '^':
                    self.splitters.add((i, j))
    
    def is_splitter(self, i, j):
        return (i, j) in self.splitters


def part_one(input):
    map = Map(input)
    beams = [map.start]
    splits = 0

    for i in range(1, map.height):
        new_beams = set()
        for beam in beams:
            if map.is_splitter(i, beam):
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                splits += 1
            else:
                new_beams.add(beam)
        
        beams = list(new_beams)

    return splits 

print(part_one(example))
print(part_one(input))

def part_two(input):
    map = Map(input)
    return count_timelines_inner(map, 0, map.start)

# Count timelines for the beam starting at (i, j)
def count_timelines_inner(map, i, j, memo={}):
    # base case
    if i == map.height - 1:
        return 1

    if memo:
        if (i, j) in memo:
            return memo[(i, j)]
    
    # try to advance the beam and see if there's a splitter
    if map.is_splitter(i + 1, j):
        # recursively count timelines
        count = count_timelines_inner(map, i + 1, j - 1) + count_timelines_inner(map, i + 1, j + 1)
    else:
        # if no splitter, just advance the beam and continue
        count = count_timelines_inner(map, i + 1, j)

    memo[(i, j)] = count
    return count

print(part_two(example))
print(part_two(input))