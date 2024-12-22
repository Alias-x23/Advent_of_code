
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
    map_plot.append([r for r in row])

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

loops = 0

# for i, row in enumerate(map_plot):
#     # if i % 5 == 0:
#     #     print(f"Done {i} rows")
#     print(f"done {i} rows")
#     for j, col in enumerate(row):
counter = 0
for step in list(set(steps)):
    print(counter)
    counter += 1
    d = "n"
    pos = map_plot[start[0]][start[1]]
    y = start[0]
    x = start[1]
    y_coord = int(step.split("-")[0])
    x_coord = int(step.split("-")[1])
    if map_plot[y_coord][x_coord] == ".":
        map_plot[y_coord][x_coord] = "#"
    else:
        continue
    path = []
    while True:
        new_pos = map_plot[y][x]
        if map_plot[y][x] == ".":
            if f"{y}-{x}-{d}" in path:
                loops += 1
                map_plot[y_coord][x_coord] = "."
                break
            path.append(f"{y}-{x}-{d}")
        elif map_plot[y][x] == "#":
            y -= compass[d][0]
            x -= compass[d][1]
            d = change_direction(d)
        elif map_plot[y][x] == "o":
            map_plot[y_coord][x_coord] = "."
            break
        y += compass[d][0]
        x += compass[d][1]

print(loops)

print("Hello")
