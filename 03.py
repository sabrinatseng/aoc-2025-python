from common import readlines

DAY = 3

example = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

input = readlines(DAY)

def total_output_joltage(input):
    total = 0
    for bank in input:
        m1 = max(bank) # max digit in string
        i = bank.index(m1) # index of max digit

        # If max digit is at the end, find the max digit before it
        # Otherwise, find the max digit after it
        if i == len(bank) - 1:
            m2 = max(bank[:-1])
            joltage = int(m2) * 10 + int(m1)
        else:
            m2 = max(bank[i+1:])
            joltage = int(m1) * 10 + int(m2)

        total += joltage
    
    return total

print(total_output_joltage(example))
print(total_output_joltage(input))

def total_output_joltage_2(input):
    total = 0

    for bank in input:
        joltage = joltage_helper(bank, 12)
        total += joltage
        
    return total

# Recursive approach to find max joltage for any bank and number of batteries
def joltage_helper(bank, num_batteries):
    # base cases
    if num_batteries == 0:
        return 0
    if len(bank) == num_batteries:
        return int(bank)
    
    # find the max digit in bank
    m = max(bank)
    i = bank.index(m)

    length_to_end = len(bank) - i

    # if it's exactly num_batteries from the end,
    # we can just return the number starting from here
    if length_to_end == num_batteries:
        return int(bank[i:])

    # if it's less than num_batteries from the end,
    # then we want to include this digit to the end, 
    # but we also need to find more batteries to the left
    if length_to_end < num_batteries:
        return int(bank[i:]) + joltage_helper(bank[:i], num_batteries - length_to_end) * (10 ** length_to_end)
    
    # if it's greater, then we should use this as the first digit
    # and repeat the process to the right
    if length_to_end > num_batteries:
        return int(m) * (10 ** (num_batteries - 1)) + joltage_helper(bank[i+1:], num_batteries - 1)

# Test recursive function using example
assert([joltage_helper(i, 2) for i in example] == [98, 89, 78, 92])
assert([joltage_helper(i, 12) for i in example] == [987654321111, 811111111119, 434234234278, 888911112111])

print(total_output_joltage_2(example))
print(total_output_joltage_2(input))