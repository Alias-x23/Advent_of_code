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


def alt_seed_list(seed_list):

    start_list = []
    range_list = []

    for i, seed in enumerate(seed_list):
        if (i+1) % 2 == 0:
            range_list.append(int(seed))
        else:
            start_list.append(int(seed))

    range_dict = {i: [int(start_list[i]), (start_list[i] + range_list[i])] for i in range(len(start_list))}

    return range_dict


def reverse_lookup(plant_dict, range_dict):
    sections = list(plant_dict.keys())
    check = 99750000
    loc_num = 99750000

    while True:
        for section in reversed(sections):
            for limits in plant_dict[section]:
                limits = [int(x) for x in limits]
                if limits[0] <= check < (limits[0]+limits[2]):
                    check = limits[1]+(check-limits[0])
                    break
        for key in range_dict.keys():
            if range_dict[key][0] <= check <= range_dict[key][1]:
                print(f"First match is {loc_num} from {check}")
                exit()
        loc_num += 1
        if loc_num % 10000 == 0:
            print(f"Run {loc_num} checks so far")
        check = loc_num


def get_locations_alt(range_dict, plant_dict):
    seed_range_list = list(range_dict.values())

    for section in plant_dict.keys():
        section_list = []
        for seed_range in seed_range_list:
            for limits in plant_dict[section]:
                limits = [int(x) for x in limits]

                if limits[1] <= seed_range[0] < (limits[1]+limits[2]):
                    if limits[1] <= seed_range[1] < (limits[1] + limits[2]):
                        break
                    else:
                        seed_range_list.append([(limits[1] + limits[2]), seed_range[1]])
                        seed_range[1] = limits[1] + limits[2] - 1
                        break

                elif limits[1] <= seed_range[1] < (limits[1] + limits[2]):
                    seed_range_list.append([seed_range[0], limits[1] - 1])
                    seed_range[0] = limits[1]
                    break

            section_list.append([limits[0]+(seed_range[0]-limits[1]), limits[0]+(seed_range[1]-limits[1])])
        seed_range_list = section_list.copy()
        print(f"Seed list now contains {len(seed_range_list)} ranges")

    out_list = [x for z in seed_range_list for x in z]

    return out_list


def main():
    text = AdventOfCode.get_txt("5")
    seed_list, plant_dict = sort_data(text)
    location_list = get_locations(seed_list, plant_dict)
    print(f"The lowest location value is {min(location_list)}")
    range_dict = alt_seed_list(seed_list)
    new_location_list = get_locations_alt(range_dict, plant_dict)
    print(f"The lowest location value is {min(new_location_list)}")
    #reverse_lookup(plant_dict, range_dict)


if __name__ == '__main__':
    main()
