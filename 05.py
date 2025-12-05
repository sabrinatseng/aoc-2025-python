from common import read

DAY = 5

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

input = read(DAY)

# Return (ranges, ingredients):
# - ranges: [(start, end)]
# - ingredients: [ingredient]
def parse(input): 
    ranges = []
    ingredients = []

    ranges_s, ingredients_s = input.split("\n\n")

    for range in ranges_s.splitlines():
        start, end = range.split('-')
        ranges.append((int(start), int(end)))
    
    for ingredient in ingredients_s.splitlines():
        ingredients.append(int(ingredient))
    
    return (ranges, ingredients)


def part_one(input):
    ranges, ingredients = parse(input)

    count = 0

    for ingredient in ingredients:
        for (start, end) in ranges:
            if ingredient >= start and ingredient <= end:
                count += 1
                break
    
    return count

print(part_one(example))
print(part_one(input))

def part_two(input):
    ranges, _ = parse(input)

    # Sort by start
    ranges.sort(key=lambda x: x[0])

    # Keep a running sum of range lengths
    # start with first range
    curr_start, curr_end = ranges[0]
    sum = curr_end - curr_start + 1
    for (start, end) in ranges[1:]:
        # check whether this can be merged with current range
        # note: we know that start >= curr_start already because ranges is sorted
        if start <= curr_end:
            if end <= curr_end:
                # both start and end are in current range,
                # so we don't need to do anything
                continue
            else:
                # start is in the range, but end is outside the range
                # add the difference and update current range end to end
                sum += end - curr_end
                curr_end = end
        else:
            # neither are in the current range, so add to sum and update current range
            sum += end - start + 1
            curr_start, curr_end = start, end
    
    return sum

print(part_two(example))
print(part_two(input))

