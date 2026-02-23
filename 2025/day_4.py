from copy import copy


def read_input():
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    "Advent_of_code/2025/inputs/day1.txt"
    return t.read()


def part_1(data):
    total = 0

    for y, sub_data in enumerate(data):
        for x, char in enumerate(sub_data):
            if char == ".":
                continue
            surroundings = data[y-1][x-1:x+2] + sub_data[x-1:x+2] + data[y+1][x-1:x+2]

            rolls = surroundings.count("@")
            if rolls < 5:
                total += 1

    print(f"Total movable rolls: {total}")


def part_2(data):
    total = 0
    previous = -1
    loops = 0

    while True:
        loops += 1
        for y, sub_data in enumerate(data):
            for x, char in enumerate(sub_data):
                if char == ".":
                    continue
                surroundings = data[y - 1][x - 1:x + 2] + sub_data[x - 1:x + 2] + data[y + 1][x - 1:x + 2]

                rolls = surroundings.count("@")
                if rolls < 5:
                    total += 1
                    sub_data = list(sub_data)
                    sub_data[x] = "."
                    sub_data = "".join(sub_data)
                    data[y] = "".join(sub_data)

        if previous == total:
            break
        previous = copy(total)

    print(f"Part_2\nTotal movable rolls: {total}")


def main():
    data = read_input()
    data_list = data.split("\n")

    # add a border around the data for ease of operations
    data_list = [f".{d}." for d in data_list]
    data_list = ["."*len(data_list[0])] + data_list + ["."*len(data_list[0])]

    part_1(data_list)
    part_2(data_list)


if __name__ == '__main__':
    main()

