def read(day):
    with open(f"{day:02d}.txt", 'r') as f:
        return f.read()

def readlines(day):
    with open(f"{day:02d}.txt", 'r') as f:
        return f.read().splitlines()

### Extract list of whitespace-separated ints from a string
def get_ints(s):
    return [int(i) for i in s.split()]

### Assuming input contains one coordinate per line
### where coordinates are comma-separated,
### return list of coords as tuples.
def parse_coords(input):
    result = []
    for line in input.splitlines():
        result.append(tuple([int(x) for x in line.split(',')]))
    
    return result