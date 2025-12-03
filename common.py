def read(day):
    with open(f"{day:02d}.txt", 'r') as f:
        return f.read()

def readlines(day):
    with open(f"{day:02d}.txt", 'r') as f:
        return f.read().splitlines()

### Extract list of whitespace-separated ints from a string
def get_ints(s):
    return [int(i) for i in s.split()]