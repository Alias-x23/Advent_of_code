def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = 0

    history = []
    move_list = [[m] for m in data["you"]]

    # while True:
    #     new_moves = []
    #     for move in move_list:
    #         new_moves = [move.append(x) for x in data[move[-1]]]

    # for move in move_list:
    #     if move != "out":
    #         new_moves = [m for m in data[move] if m not in history]
    #     # if move == "out":
    #     #     total += 1

    print(f"Part_1 total: {total}")


def part_2(data):
    total = 0

    print(f"Part_2 total: {total}")


def main():
    data = read_input()
    data = data.split("\n")

    data = {d.split(":")[0]: d.split(":")[1].strip().split(" ") for d in data}

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()

