
def read_input(day):
    t = open(f"inputs/day{day}.txt")
    "Advent_of_code/2025/inputs/day1.txt"
    return t.read()


data = read_input("2")
data_list = data.split(",")


def part_1():
    total = 0
    for ids in data_list:
        start = int(ids.split("-")[0])
        end = int(ids.split("-")[1])
        check_list = [n for n in range(start, end + 1)]

        for num in check_list:
            id_string = str(num)
            if len(id_string) % 2 != 0:
                continue

            length = int(len(id_string) / 2)
            first = id_string[:length]
            last = id_string[length:]
            if id_string[:length] == id_string[length:]:
                total += num

    return total


id_total = part_1()
print(f"part 1: {id_total}")


def get_factors(x):
    # get the factors for a number excluding 1 and itself
    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)
    return factors


def part_2():
    total = 0
    for ids in data_list:
        start = int(ids.split("-")[0])
        end = int(ids.split("-")[1])
        check_list = [n for n in range(start, end + 1)]

        for num in check_list:
            id_string = str(num)
            digits = len(id_string)
            factors = get_factors(digits)

            # # check for all same number
            # num_count = id_string.count(id_string[0])
            # if num_count == len(id_string):
            #     total += num
            #     continue

            for factor in factors:
                char_check = id_string[:factor]
                num_count = id_string.count(id_string[:factor])
                if num_count == digits / factor:
                    total += num
                    break
                # sub_list = [id_string[i:i+factor] for i in range(0, len(id_string), factor)]
                # first_sequence = sub_list[0]
                # sequence_count = 0
                # for sub in sub_list:
                #     if first_sequence == sub:
                #         sequence_count += 1
                # if sequence_count == len(sub_list):
                #     total += num

    return total


new_total = part_2()
print(f"part 2: {new_total}")

# 54627623377 too high

