from common import read

DAY = 11

example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

input = read(DAY)

# Return a dictionary of {node: set(neighbors)}
def parse(input):
    graph = {}
    for line in input.splitlines():
        node, neighbors = line.split(': ')
        graph[node] = set(neighbors.split())

    return graph

def count_paths_recursive(graph, start, end, memo):
    # base cases
    if start == end:
        return 1
    if start not in graph:
        return 0

    # check memo
    if (start, end) in memo:
        return memo[(start, end)]

    paths = 0
    for neighbor in graph[start]:
        paths += count_paths_recursive(graph, neighbor, end, memo)
    
    memo[(start, end)] = paths
    return paths

def part_one(input):
    graph = parse(input)

    return count_paths_recursive(graph, 'you', 'out', {})

print(part_one(example))
print(part_one(input))

example_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

def part_two(input):
    graph = parse(input)

    svr_to_dac = count_paths_recursive(graph, 'svr', 'dac', {})
    svr_to_fft = count_paths_recursive(graph, 'svr', 'fft', {})

    dac_to_fft = count_paths_recursive(graph, 'dac', 'fft', {})
    fft_to_dac = count_paths_recursive(graph, 'fft', 'dac', {})

    dac_to_out = count_paths_recursive(graph, 'dac', 'out', {})
    fft_to_out = count_paths_recursive(graph, 'fft', 'out', {})

    return svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out


print(part_two(example_2))
print(part_two(input))