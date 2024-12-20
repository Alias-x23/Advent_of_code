
t = open("input6.txt")
text = t.read()
map_plot1 = text.split("\n")

buffer = "o" * len(map_plot1[0])

# prepare data
map_plot1.insert(0, buffer)
map_plot1.append(buffer)
map_plot1 = [f"o{line}o" for line in map_plot1]

start = "plese stop complaining"

map_plot = []

for i, row in enumerate(map_plot1):
    if "^" in row:
        start = [i, row.index("^")]
        row = row.replace("^", ".")
    map_plot.append(row)

compass = {
    "n": [-1, 0],
    "e": [0, 1],
    "s": [1, 0],
    "w": [0, -1]
}


def change_direction(direction):
    if direction == "n":
        return "e"
    if direction == "e":
        return "s"
    if direction == "s":
        return "w"
    if direction == "w":
        return "n"


steps = []

d = "n"
pos = map_plot[start[0]][start[1]]
y = start[0]
x = start[1]

while True:
    new_pos = map_plot[y][x]
    if map_plot[y][x] == ".":
        steps.append(f"{y}-{x}")
    elif map_plot[y][x] == "#":
        y -= compass[d][0]
        x -= compass[d][1]
        d = change_direction(d)
    elif map_plot[y][x] == "o":
        break
    y += compass[d][0]
    x += compass[d][1]

distinct_steps = len(set(steps))

print(distinct_steps)

print("Hello")