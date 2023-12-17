from day_2 import AdventOfCode
import re
import math


def split_data(text):
    text_list = text.split("\n")
    directions = text_list[0]
    directions = directions.replace("L", "0")
    directions = directions.replace("R", "1")
    map_list = text_list[2:]
    map_dict = {}

    for m in map_list:
        m = re.sub(r" =|\(|\)|,", "", m)
        m = m.split()
        map_dict[m[0]] = [m[1], m[2]]

    return directions, map_dict


def find_route(directions, map_dict):

    steps = 0
    loop = 0
    max_loop = len(directions) - 1
    pos = "AAA"

    while True:
        steps += 1
        move = map_dict[pos][int(directions[loop])]
        if move == "ZZZ":
            print(f"Reached destination in {steps} steps")
            return
        loop += 1
        if loop > max_loop:
            loop = 0
        pos = move


def find_all_routes(directions, map_dict):

    steps = 1271600000
    loop = 0
    max_loop = len(directions) - 1
    pos_list = [k for k in map_dict.keys() if k.endswith("A")]

    while True:
        steps += 1
        if steps % 100000 == 0:
            print(f"{steps} current steps")
        move_list = [map_dict[pos][int(directions[loop])] for pos in pos_list]
        move_check = [m for m in move_list if m.endswith("Z")]
        if len(move_check) > 0:
            print("hello")
        if len(move_check) == len(move_list):
            print(f"Reached all destinations in {steps} steps")
            return
        loop += 1
        if loop > max_loop:
            loop = 0
        pos_list = move_list.copy()


def find_all_routes2(directions, map_dict):

    max_loop = len(directions) - 1
    pos_list = [k for k in map_dict.keys() if k.endswith("A")]

    out_list = []

    for pos in pos_list:
        steps = 0
        loop = 0
        while True:
            steps += 1
            move = map_dict[pos][int(directions[loop])]
            loop += 1
            if move.endswith("Z"):
                out_list.append(steps)
                break
            if loop > max_loop:
                loop = 0
            pos = move

    print(f"Lowest common multiple for routes is {math.lcm(12169, 20093, 20659, 22357, 13301, 18961)}")




def main():
    text = AdventOfCode.get_txt("8")
    directions, map_dict = split_data(text)
    find_route(directions, map_dict)
    find_all_routes2(directions, map_dict)


if __name__ == '__main__':
    main()
