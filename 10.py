import pulp
from common import read

DAY = 10

example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input = read(DAY)

# Return a tuple per line of:
# - desired_state: set of lights that should be on,
# - buttons: [set of lights flipped by button]
def parse(input):
    machines = []
    for line in input.splitlines():
        parts = line.split()
        desired_state_str = parts[0][1:-1]
        desired_state = set([i for i, c in enumerate(desired_state_str) if c == '#'])
        
        buttons = []
        for s in parts[1:-1]:
            button = set([int(x) for x in s[1:-1].split(",")])
            buttons.append(button)
        
        machines.append((desired_state, buttons))
    
    return machines

def part_one(input):
    # do a breadth first search to get to the desired state
    # in the fewest number of button presses
    machines = parse(input)

    count = 0
    for desired_state, buttons in machines:
        count += find_min_button_presses(desired_state, buttons)
    
    return count


def press_button(state, button):
    # symmetric difference toggles all the indexes in button
    return state ^ button

def find_min_button_presses(desired_state, buttons):
    queue = [(set(), [])]
    # cache of states already seen (we don't need to add to the queue if we've already seen it)
    states_seen = []
    while len(queue) > 0:
        state, buttons_pressed = queue.pop(0)

        # try pressing each button except the one that was just pressed (if any)
        for i in range(len(buttons)):
            if len(buttons_pressed) == 0 or i != buttons_pressed[-1]:
                new_state = press_button(state, buttons[i])
                new_buttons_pressed = buttons_pressed + [i]

                # we've reached desired state, add the number of button presses
                if new_state == desired_state:
                    return len(new_buttons_pressed)

                if new_state not in states_seen:
                    queue.append((new_state, new_buttons_pressed))
                    states_seen.append(new_state)
        
            
print(part_one(example))
print(part_one(input))


# Return a tuple per line of:
# - desired_state: [desired counter states]
# - buttons: [list of counters incremented by button]
def parse_2(input):
    joltages = []
    for line in input.splitlines():
        parts = line.split()
        
        buttons = []
        for s in parts[1:-1]:
            button = [int(x) for x in s[1:-1].split(",")]
            buttons.append(button)
        
        desired_state_str = parts[-1][1:-1]
        desired_state = [int(x) for x in desired_state_str.split(",")]

        joltages.append((desired_state, buttons))
    
    return joltages

# Use LP solver pulp
def find_min_button_presses_2(desired_state, buttons):
    prob = pulp.LpProblem("button_presses", sense=pulp.LpMinimize)

    # one variable per button for the number of times it's pressed
    button_vars = [
        pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(len(buttons))
    ]

    # each counter must land exactly on its target count
    for counter_idx, target in enumerate(desired_state):
        touched = [button_vars[i] for i, button in enumerate(buttons) if counter_idx in button]
        prob += pulp.lpSum(touched) == target, f"counter_{counter_idx}"

    # minimize total presses across all buttons
    prob += pulp.lpSum(button_vars)

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    # Return the total number of button presses
    return int(sum(var.value() for var in button_vars))

def part_two(input):
    joltages = parse_2(input)

    count = 0
    for desired_state, buttons in joltages:
        count += find_min_button_presses_2(desired_state, buttons)
    
    return count

print(part_two(example))
print(part_two(input))