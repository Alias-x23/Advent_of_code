def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = 0

    print(f"Part_1 total: {total}")


def part_2(data):
    total = 0

    print(f"Part_2 total: {total}")


def main():
    data = read_input()

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()

