from copy import copy
from collections import defaultdict


def read_input():
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = 0
    data = copy(data)
    positions = [data[0].index("S")]
    data.pop(0)

    # this actually has an error as the positions are being added to in the wrong place
    # however it gave the correct results
    for row in data:
        for pos in positions:
            if row[pos] == "^":
                total += 1
                positions += [pos + 1, pos - 1]
                positions = [p for p in positions if p != pos and p]
                positions = list(set(positions))

    print(f"Part_1 total: {total}")


def part_2(data):
    data = copy(data)
    positions = [data[0].index("S")]
    paths = 1
    data.pop(0)

    # pos_dict = {positions[0]: 1}
    pos_dict = defaultdict(int)
    pos_dict[positions[0]] = 1

    new_positions = []
    used_positions = []

    for row in data:
        if row.count(".") == len(row):
            continue
        for pos in positions:
            new_new_positions = []
            if row[pos] == "^":
                paths += pos_dict[pos]
                # new_positions += [[pos + 1, pos - 1] for i in range(pos_dict[pos])]
                new_new_positions = [pos + 1, pos - 1]
                used_positions += [pos]

            for new_pos in new_new_positions:
                # pos_dict[new_pos] += new_positions.count(new_pos)
                pos_dict[new_pos] += pos_dict[pos]
            new_positions += new_new_positions

        # pos_dict += {p: positions.count(p) for p in positions}
        # for p in list(set(new_positions)):
        #     pos_dict[p] += new_positions.count(p)
        for p in used_positions:
            pos_dict.pop(p)

        # positions += [x for xs in new_positions for x in xs]
        positions += new_positions
        positions = [p for p in positions if p not in used_positions and p]
        positions = list(set(positions))
        new_positions = []
        used_positions = []

    # for i, row in enumerate(data):
    #     new_paths = []
    #     new_positions = copy(positions)
    #     for pos in positions:
    #         if row[pos] == "^":
    #             new_positions += [pos + 1, pos - 1]
    #             new_positions = [p for p in new_positions if p != pos]
    #             new_positions = list(set(new_positions))
    #             for path in paths:
    #                 if path[-1] == pos:
    #                     new_path_a = copy(path)
    #                     new_path_a.append(pos - 1)
    #                     new_path_b = copy(path)
    #                     new_path_b.append(pos + 1)
    #                     new_paths += [new_path_a, new_path_b]
    #
    #         else:
    #             for path in paths:
    #                 if path[-1] == pos:
    #                     path.append(pos)
    #
    #     paths += new_paths
    #     paths = [p for p in paths if len(p) == i + 2]
    #     positions = copy(new_positions)

    print(f"Part_2 total: {paths}")


def main():
    data = read_input()
    data = data.split("\n")

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()

