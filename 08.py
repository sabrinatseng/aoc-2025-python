from common import read, parse_coords

DAY = 8

example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

input = read(DAY)

# return list of (dist, i, j) where dist = the distance (squared) between i and j
# sorted from least to greatest distance.
def get_sorted_distances(boxes):
    dists = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            # don't bother with sqrt as it doesn't affect comparisons
            dist = sum([abs(boxes[i][k] - boxes[j][k]) ** 2 for k in range(3)])
            dists.append((dist, i, j))
    
    # sort by distance
    dists.sort(key=lambda x: x[0])

    return dists

# return (circuits, circuits_lookup) to start with
# - circuits: { circuit index : set of box indexes in the circuit }
# - circuits_lookup: { box index : circuit index which it belongs to }
# start with each box in its own circuit
def build_lookups(l):
    circuits = { i: set([i]) for i in range(l) } 
    circuits_lookup = { i : i for i in range(l)} 
    return (circuits, circuits_lookup)

def part_one(input, pairs):
    boxes = parse_coords(input)

    dists = get_sorted_distances(boxes) 
    circuits, circuits_lookup = build_lookups(len(boxes))

    # start connecting closest pairs
    for c in range(pairs):
        _, i, j = dists[c]
        connect_boxes(i, j, circuits, circuits_lookup)

    circuit_sizes = [len(circuit) for circuit in circuits.values()]
    circuit_sizes.sort(reverse=True)

    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

def connect_boxes(i, j, circuits, circuits_lookup):
    circuit_index_i = circuits_lookup[i]
    circuit_index_j = circuits_lookup[j]
    if circuit_index_i != circuit_index_j:
        # join the entire circuit that j belongs to, with the one that i belongs to
        # update both lookups
        for c_j in circuits[circuit_index_j]:
            circuits_lookup[c_j] = circuit_index_i
        circuits[circuit_index_i] = circuits[circuit_index_i].union(circuits[circuit_index_j])
        # circuit j is now gone
        del circuits[circuit_index_j]

print(part_one(example, 10))
print(part_one(input, 1000))

def part_two(input):
    boxes = parse_coords(input)

    dists = get_sorted_distances(boxes) 

    circuits, circuits_lookup = build_lookups(len(boxes))

    dists_index = 0
    while len(circuits) > 1:
        _, i, j = dists[dists_index] 
        connect_boxes(i, j, circuits, circuits_lookup)
        dists_index += 1
    
    # return the product of the x-coordinates of last 2 boxes connected
    return boxes[i][0] * boxes[j][0]

print(part_two(example))
print(part_two(input))

