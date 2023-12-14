from day_2 import AdventOfCode
import numpy as np


def sort_data(text):
    text_list = text.split("\n")
    text_list = [t for t in text_list if len(t) > 0]

    seed_list = text_list[0].split(": ")[1].split()
    guide_dict = {}
    temp = ""

    for line in text_list[1:]:
        if ":" in line:
            temp = line
            guide_dict[line] = []
            continue
        guide_dict[temp].append(line.split())

    return seed_list, guide_dict


def get_locations(seed_list, plant_dict):
    out_list = []

    for seed in seed_list:
        seed = int(seed)
        for section in plant_dict.keys():
            for limits in plant_dict[section]:
                limits = [int(x) for x in limits]
                if limits[1] <= seed < (limits[1]+limits[2]):
                    seed = limits[0]+(seed-limits[1])
                    break
        out_list.append(seed)

    return out_list


def alt_seed_list(seed_list, plant_dict):

    start_list = []
    range_list = []

    for i, seed in enumerate(seed_list):
        if (i+1) % 2 == 0:
            range_list.append(seed)
        else:
            start_list.append(seed)

    out_list = []

    for j, start in enumerate(start_list):
        size = int(range_list[j]) + int(start)
        sub_list = np.arange(int(start), int(size)).tolist()
        out_list.append(min(get_locations(sub_list, plant_dict)))

    return out_list


def main():
    text = AdventOfCode.get_txt("5")
    seed_list, plant_dict = sort_data(text)
    location_list = get_locations(seed_list, plant_dict)
    print(f"The lowest location value is {min(location_list)}")
    new_loc_list = alt_seed_list(seed_list, plant_dict)
    #location_list2 = get_locations(new_seed_list, plant_dict)
    print(f"The lowest new location value is {min(new_loc_list)}")


if __name__ == '__main__':
    main()
