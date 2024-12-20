
t = open("input4.txt")
text = t.read()
text_list = text.split("\n")

buffer = "o" * len(text_list[0])

# prepare data
text_list.insert(0, buffer)
text_list.append(buffer)

new_text_list = [f"o{line}o" for line in text_list]

direction_dict = {
    "N": [-1, 0],
    "NE": [-1, 1],
    "E": [0, 1],
    "SE": [1, 1],
    "S": [1, 0],
    "SW": [1, -1],
    "W": [0, -1],
    "NW": [-1, -1]
}

letters = "MAS"

matches = 0

for y, line in enumerate(new_text_list):
    for x, char in enumerate(line):
        if char == "X":
            for d in direction_dict.values():
                letter_check = 0
                new_y = y + d[0]
                new_x = x + d[1]
                while True:
                    z = new_text_list[new_y][new_x]
                    if letter_check == 3:
                        matches += 1
                        break
                    if new_text_list[new_y][new_x] == letters[letter_check]:
                        letter_check += 1
                        new_y += d[0]
                        new_x += d[1]
                    else:
                        break

print(matches)

diagonal_dict = {
    "NW": [-1, -1],
    "SE": [1, 1],
    "NE": [-1, 1],
    "SW": [1, -1]
}

new_matches = 0
a_co_ords = []

for y, line in enumerate(new_text_list):
    for x, char in enumerate(line):
        if char == "A":
            nw_se = [new_text_list[y-1][x-1], new_text_list[y+1][x+1]]
            check_nw_se = list(set([c for c in nw_se if c in ["M", "S"]]))
            if len(check_nw_se) != 2:
                continue
            ne_sw = [new_text_list[y - 1][x + 1], new_text_list[y + 1][x - 1]]
            check_ne_sw = list(set([c for c in ne_sw if c in ["M", "S"]]))
            if len(check_ne_sw) == 2:
                new_matches += 1
                # a_co_ords.append(f"{y,x}")


print(new_matches)
# print(a_co_ords)
# ['(2, 3)', '(3, 7)', '(3, 8)', '(4, 3)', '(4, 5)', '(5, 3)', '(7, 6)', '(8, 2)', '(8, 4)', '(8, 6)', '(8, 8)', (9, 2)]

print("hello")
