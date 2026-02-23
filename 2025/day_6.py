import re
import math


def read_input():
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = 0

    for i in range(len(data[0])):
        sum_list = [d[i] for d in data]
        operator = sum_list.pop()
        sum_list = [int(s) for s in sum_list]

        if operator == "+":
            z = sum(sum_list)
            total += sum(sum_list)
        else:
            x = math.prod(sum_list)
            total += math.prod(sum_list)

    print(f"Part_1 total: {total}")


def part_2(raw_data, operators):
    data = raw_data.split("\n")
    data = data[:-1]

    total = 0
    value_list = []
    op_pos = 0

    for col in range(len(data[0])):

        value = "".join([d[col] for d in data]).strip()

        if col == len(data[0]) - 1:
            value_list.append(value)

        if not value or col == len(data[0]) - 1:
            sum_list = [int(v) for v in value_list]
            if operators[op_pos] == "+":
                z = sum(sum_list)
                total += sum(sum_list)
            else:
                x = math.prod(sum_list)
                total += math.prod(sum_list)
            value_list = []
            op_pos += 1
            continue

        value_list.append(value)

    print(f"Part_2 total: {total}")


def main():
    raw_data = read_input()

    data = raw_data.split("\n")
    data = [re.sub(r" {1,999}", " ", d.strip()).split(" ") for d in data]

    part_1(data)
    part_2(raw_data, data[-1])


if __name__ == '__main__':
    main()


# 10604451464 too low
