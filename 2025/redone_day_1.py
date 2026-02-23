def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(moves):
    total = 0
    pos = 50

    for m in moves:
        hundreds = int(m / 100)
        m -= (hundreds * 100)

        pos += m
        if pos < 0:
            pos += 100
        if pos > 99:
            pos -= 100

        if pos == 0:
            total += 1

    print(f"Part_1 total: {total}")


def part_2(moves):
    total = 0
    pos = 50

    for m in moves:
        hundreds = int(m/100)
        total += abs(hundreds)
        m -= (hundreds*100)

        previous_pos = pos
        pos += m
        if pos < 0:
            pos += 100
            if previous_pos != 0:
                total += 1
        if pos > 99:
            pos -= 100
            if pos != 0:
                total += 1

        if pos == 0:
            total += 1

    print(f"Part_2 total: {total}")


def main():
    data = read_input()
    moves = [int(m[1:]) if m[0] == "R" else -abs(int(m[1:])) for m in data.split("\n")]

    part_1(moves)
    part_2(moves)


if __name__ == '__main__':
    main()

