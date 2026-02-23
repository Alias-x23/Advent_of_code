def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data, shapes):
    total = 0
    remainder = 0

    shape_sizes = [s.count("#") for s in shapes]

    for d in data:
        d_list = d.split(":")
        area_vals = d_list[0].split("x")
        area = int(area_vals[0])*int(area_vals[1])
        shape_vals = d_list[1].split(" ")[1:]

        min_area = sum([int(s_val)*shape_sizes[i] for i, s_val in enumerate(shape_vals)])
        if min_area > area:
            continue

        safe_area = sum([int(s)*9 for s in shape_vals])
        if area >= safe_area:
            total += 1
        else:
            remainder += 1

    print(f"Part_1 total: {total}\n with {remainder} remaining")


def part_2(data, shapes):
    total = 0

    print(f"Part_2 total: {total}")


def main():
    data = read_input()

    data_list = data.split("\n\n")
    data = data_list[-1].split("\n")
    shapes = data_list[:-1]

    part_1(data, shapes)
    part_2(data, shapes)


if __name__ == '__main__':
    main()

