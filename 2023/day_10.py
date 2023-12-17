from day_2 import AdventOfCode
import re


def convert_map(text):

    replace_dict = {
        ".": "(0000)",
        "|": "(1010)",
        "-": "(0101)",
        "F": "(0110)",
        "7": "(0011)",
        "L": "(1100)",
        "J": "(1001)",
    }

    for key in replace_dict.keys():
        text = text.replace(key, replace_dict[key])

    text_list = text.split("\n")
    text_lol = [re.split(r"\)\(|\(|\)", t) for t in text_list]
    text_lol = [t[1:-1] for t in text_lol]

    return text_lol


def find_loop(text_lol):

    x_limit = len(text_lol[0])
    y_limit = len(text_lol)
    start_y = 0
    start_x = 0

    for i, row in enumerate(text_lol):
        if "S" in row:
            start_y = i
            start_x = row.index("S")

    pos_starts = [text_lol[start_y+1][start_x], text_lol[start_y-1][start_x],
                  text_lol[start_y][start_x+1], text_lol[start_y][start_x-1]]

    move_dict = {"1000": 2,
                 "0100": 3,
                 "0010": 0,
                 "0001": 1}

    for s in move_dict.keys():
        steps = 1
        if s.index("1") == 0:
            y = start_y - 1
            x = start_x
        elif s.index("1") == 1:
            y = start_y
            x = start_x + 1
        elif s.index("1") == 2:
            y = start_y + 1
            x = start_x
        else:
            y = start_y
            x = start_x - 1

        pos = text_lol[y][x]
        if pos[move_dict[s]] != "1":
            continue
        pos = list(pos)
        pos[move_dict[s]] = "0"
        pos = "".join(pos)
        while True:
            steps += 1
            if pos.index("1") == 0:
                y = y - 1
            elif pos.index("1") == 1:
                x = x + 1
            elif pos.index("1") == 2:
                y = y + 1
            else:
                x = x - 1

            new_pos = text_lol[y][x]
            if new_pos == "S":
                print(f"Found the loop!\nThe loop is {steps} steps so {steps/2}")
                exit()
            if new_pos[move_dict[pos]] != "1":
                break
            new_pos = list(new_pos)
            new_pos[move_dict[pos]] = "0"
            pos = "".join(new_pos)

    return


def main():
    text = AdventOfCode.get_txt("10")
    text_lol = convert_map(text)
    find_loop(text_lol)


if __name__ == '__main__':
    main()
