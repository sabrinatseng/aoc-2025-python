from common import read

DAY = 12

example = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

input = read(DAY)

class Present:
    def __init__(self, coords):
        self.coords = coords
    
    def area(self):
        return len(self.coords)

class Region:
    def __init__(self, width, height, present_counts):
        self.width = width
        self.height = height
        self.present_counts = present_counts
    
    def __repr__(self):
        present_str = " ".join(str(count) for count in self.present_counts)
        return f"{self.width}x{self.height}: {present_str}"
    
    def area(self):
        return self.width * self.height


# Return:
# - list of presents, represented as set of coords relative to (0,0) top left
# - list of regions
def parse(input):
    sections = input.split("\n\n")

    # present definitions
    presents = []
    for i in range(len(sections) - 1):
        section = sections[i]

        present = set()
        # skip the line with the present idx which we can keep track of
        lines = section.splitlines()[1:]
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] == '#':
                    present.add((r, c))
        presents.append(Present(present))
    
    # regions
    regions = []
    for line in sections[-1].splitlines():
        area, present_counts = line.split(": ")
        width, height = [int(i) for i in area.split("x")]
        present_counts = [int(i) for i in present_counts.split(" ")]
        regions.append(Region(width, height, present_counts))

    return (presents, regions)

def part_one(input):
    presents, regions = parse(input)

    count = 0
    for region in regions:
        # Constraint 1: If total present area > region area, it definitely doesn't fit
        total_present_area = sum([region.present_counts[i] * presents[i].area() for i in range(len(presents))])
        region_area = region.area()
        if total_present_area > region_area:
            continue
        
        # Constraint 2: if region has enough area to fit each present
        # in its own 3x3 area, it definitely fits
        num_3x3_areas = (region.width // 3) * (region.height // 3)
        total_present_count = sum([present_count for present_count in region.present_counts])
        if total_present_count <= num_3x3_areas:
            count += 1
            continue
        
        # Otherwise, we're not sure so just log it
        print("Indeterminate")

    return count

print(part_one(example))
print(part_one(input))

        

