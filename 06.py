from common import read

DAY = 6

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

input = read(DAY)

def parse(input):
    nums = []
    lines = input.splitlines()
    for line in lines[:-1]:
        nums.append([int(i) for i in line.split()])
    
    ops = lines[-1].split()

    return (nums, ops)

def part_one(input):
    nums, ops = parse(input)

    total_sum = 0
    for i in range(len(nums[0])):
        total_sum += evaluate(ops[i], [row[i] for row in nums])
    
    return total_sum

def evaluate(op, nums):
    if op == "+":
        return sum(nums)
    if op == "*":
        prod = 1
        for num in nums:
            prod *= num
        return prod

print(part_one(example))
print(part_one(input))

def part_two(input):
    lines = input.splitlines()

    total_sum = 0

    # Assume all lines of input are the same length l
    l = len(lines[0])

    # Running list of numbers that have been read but not evaluated yet
    buffer = [] 

    for i in reversed(range(0, l)):
        # read down the column
        col = "".join([lines[j][i] for j in range(len(lines))])

        # parse the number by ignoring all non-digit characters, and add to buffer
        digits = "".join([c for c in col if c.isdigit()])
        if digits:
            buffer.append(int(digits))
        
        if col[-1] in ('+', '*'):
            # evaluate and add to total
            total_sum += evaluate(col[-1], buffer)
            # reset buffer
            buffer = []

    return total_sum 


print(part_two(example))
print(part_two(input))