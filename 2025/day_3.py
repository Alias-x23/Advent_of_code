
def read_input(day):
    t = open(f"inputs/day{day}.txt")
    "Advent_of_code/2025/inputs/day1.txt"
    return t.read()


def get_top_index(x):
    top = max(x)
    return x.index(top)


data = read_input("3")
data_list = data.split("\n")
joltage = 0


for bank in data_list:
    values = [int(b) for b in bank]

    # if the top values is on the far right it will need to be the next highest
    # so disregard the farthest right as it can never be the highest value
    top_index = get_top_index(values[:-1])
    sub_values = values[top_index + 1:]

    second_index = get_top_index(sub_values)

    combined = f"{values[top_index]}{sub_values[second_index]}"

    joltage += int(combined)

print(f"Total Joltage is: {joltage}")

greater_joltage = 0

for bank in data_list:
    values = [int(b) for b in bank]

    battery_values = []
    c = values[:0]
    c2 = values[:-11]

    for i in range(-11, 1):
        if i < 0:
            bat_index = get_top_index(values[:i])
        else:
            bat_index = get_top_index(values)
        battery_values.append(str(values[bat_index]))
        values = values[bat_index + 1:]

    combined = int("".join(battery_values))

    greater_joltage += int(combined)

print(f"Total greater_Joltage is: {greater_joltage}")

