from common import read

DAY = 2

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

input = read(DAY)

def parse(input):
    output = []
    for range in input.split(','):
        [start, end] = range.split('-')
        output.append((int(start), int(end)))

    return output

assert(parse("11-22,95-115,998-1012") == [(11, 22), (95, 115), (998, 1012)])

def part_one(input):
    ranges = parse(input)
    sum = 0

    for (start, end) in ranges:
        for i in range(start, end + 1):
            s = str(i)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    sum += i

    return sum

print(part_one(example))
print(part_one(input))

def part_two(input):
    ranges = parse(input)
    sum = 0

    for (start, end) in ranges:
        for i in range(start, end + 1):
            s = str(i)
            for div in range(2, len(s) + 1):
                # try dividing s into div parts of equal length
                if len(s) % div == 0:
                    length = len(s) // div
                    parts = [s[i:i+length] for i in range(0, len(s), length)]
                    if len(set(parts)) == 1:
                        # all parts are the same
                        sum += i
                        break

    return sum

print(part_two(example))
print(part_two(input))