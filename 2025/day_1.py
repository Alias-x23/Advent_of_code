from copy import copy


def read_input(day):
    t = open(f"inputs/day{day}.txt")
    "Advent_of_code/2025/inputs/day1.txt"
    return t.read()


data = read_input("1")
moves = {f"{line}-{i}": int(line[1:]) for i, line in enumerate(data.split("\n"))}

digits = [n for n in range(0, 100)]

pos = 50
zeroes = 0
more_zeroes = 0

for i, key in enumerate(moves.keys()):

    # for part 2
    more_zeroes += abs(int(moves[key] / 100))

    old_pos = copy(pos)

    move = int(str(abs(moves[key]))[-2:])
    if key[0] == "L":
        move = -move

    pos += move

    # if pos changes from +ve to -ve add 1
    if old_pos > 0 > pos:
        more_zeroes += 1
    if old_pos < 0 < pos:
        more_zeroes += 1

    if pos > 99:
        pos = int(str(abs(pos))[-2:])
        more_zeroes += 1
    if pos < -100:
        pos = - int(str(abs(pos))[-2:])
        more_zeroes += 1

    c = digits[pos]
    if digits[pos] == 0:
        zeroes += 1
        more_zeroes += 1


# 1034
print(f"original: {zeroes}")
print(f"part 2: {more_zeroes}")

# 6216 too high
# 6147 too low
