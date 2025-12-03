from common import readlines

DAY = 1

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

input = readlines(DAY)

def get_password(lines):
    lock = 50
    count = 0

    for line in lines:
        d = int(line[1:])
        if line[0] == 'L':
            lock = (lock - d) % 100
        else:
            lock = (lock + d) % 100
        
        if lock == 0:
            count += 1
    
    return count

print(get_password(example))
print(get_password(input))

def get_password_2(lines):
    lock = 50
    count = 0

    for line in lines:
        d = int(line[1:])

        if line[0] == 'L':
            step = -1
        else:
            step = 1

        for _ in range(d):
            lock = (lock + step) % 100

            if lock == 0:
                count += 1
    
    return count

print(get_password_2(example))
print(get_password_2(input))
