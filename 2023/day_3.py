from day_2 import AdventOfCode
import re
from collections import defaultdict


def get_tool_ids(text):
    text_list = text.split("\n")
    row_limit = len(text_list[0]) - 1
    row_count = len(text_list) - 1

    out_list = []
    gear_dict = defaultdict(lambda: [])

    for x, line in enumerate(text_list):
        n_list = []
        pos_list = []
        for y, c in enumerate(line):
            if re.match(r"\d", c):
                n_list.append(c)
                pos_list.append(y)
                if y != row_limit:
                    continue
            if len(n_list) != 0:
                check_list = []
                gear_list = []
                if pos_list[0] != 0:
                    pos_list.append(min(pos_list)-1)
                if y != row_limit:
                    pos_list.append(max(pos_list)+1)
                if x != 0:
                    check_list += [text_list[x-1][a] for a in pos_list]
                    gear_list += [f"{x-1}-{a}" for a in pos_list]
                if x != row_count:
                    check_list += [text_list[x+1][a] for a in pos_list]
                    gear_list += [f"{x+1}-{a}" for a in pos_list]
                check_list += [text_list[x][a] for a in pos_list]
                gear_list += [f"{x}-{a}" for a in pos_list]
                check = re.sub(r"\d|\.", "", "".join(check_list))
                if len(check) > 0:
                    out_list.append(int("".join(n_list)))
                if "*" in check_list:
                    gear_dict[gear_list[check_list.index("*")]].append(int("".join(n_list)))
                n_list = []
                pos_list = []

    return out_list, gear_dict


def gear_powers(gear_dict):

    out_list = [x[0]*x[1] for x in gear_dict.values() if len(x) == 2]

    return out_list


def main():
    text = AdventOfCode.get_txt("3")
    good_ids, gear_dict = get_tool_ids(text)
    print(f"Sum of tool Id's is: {sum(good_ids)}")
    gear_values = gear_powers(gear_dict)
    print(f"Sum of gear powers is: {sum(gear_values)}")


if __name__ == '__main__':
    main()
