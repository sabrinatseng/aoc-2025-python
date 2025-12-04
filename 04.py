from common import readlines

DAY = 4

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

input = readlines(DAY)

ADJS = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (-1, 1), (1, -1), (-1, -1),
]

def part_one(input):
    count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '@' and can_access(input, i, j):
                    count += 1
        
    return count

def is_roll_of_paper(input, i, j):
    return i >= 0 and i < len(input) and j >= 0 and j < len(input[i]) and input[i][j] == '@'

def can_access(input, i, j):
    num_adj = 0
    for (di, dj)  in ADJS:
        if is_roll_of_paper(input, i + di, j + dj):
            num_adj += 1
            if num_adj >= 4:
                return False
    return True

print(part_one(example))
print(part_one(input))

def part_two(input):
    # Similar to part one, but maintain a queue of positions to check
    # When a roll is removed, check all its adjacent positions

    count = 0

    # start with checking all rolls of paper
    queue = set([(i, j) for i in range(len(input)) for j in range(len(input[i])) if input[i][j] == '@'])

    while len(queue) > 0:
        i, j = queue.pop()
        if is_roll_of_paper(input, i, j) and can_access(input, i, j):
            count += 1

            # Remove this roll of paper and add adjacent squares to queue
            input[i] = input[i][:j] + '.' + input[i][j+1:]

            queue = queue.union([(i + di, j + dj) for (di, dj) in ADJS])
        
    return count

print(part_two(example))
print(part_two(input))

