def read_input():
    # the year will have to be updated
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    "Advent_of_code/2025/inputs/day1.txt"
    return t.read()


def part_1(ranges, values):
    total = 0

    for value in values:
        check_list = [r for r in ranges if r[0] <= int(value) <= r[1]]
        if len(check_list) > 0:
            total += 1

    print(f"Good ingredient total: {total}")


def part_2(ranges):

    while True:
        changes = 0
        for r in ranges:
            check_start = [x for x in ranges if x[0] <= r[0] <= x[1]]
            if len(check_start) > 1:
                lowest_start = min([c[0] for c in check_start])
                r[0] = lowest_start
                changes += 1

            check_end = [x for x in ranges if x[0] <= r[1] <= x[1]]
            if len(check_end) > 1:
                highest_end = max([c[1] for c in check_end])
                r[1] = highest_end
                changes += 1

        ranges = [f"{r[0]}-{r[1]}" for r in ranges]
        ranges = list(set(ranges))
        # this feels a tad excessive
        ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges]

        if changes == 0:
            break

    total = 0
    for r in ranges:
        total += (r[1] - r[0] + 1)

    print(f"Good ingredient ID's: {total}")


def main():
    data = read_input()
    data = data.split("\n\n")
    ranges = data[0]
    ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges.split("\n")]
    values = data[1].split("\n")

    part_1(ranges, values)
    part_2(ranges)


if __name__ == '__main__':
    main()

