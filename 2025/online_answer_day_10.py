from functools import cache
from itertools import combinations, product


def patterns(coeffs: list[tuple[int, ...]]) -> dict[tuple[int, ...], dict[tuple[int, ...], int]]:
    num_buttons = len(coeffs)
    num_variables = len(coeffs[0])
    out = {parity_pattern: {} for parity_pattern in product(range(2), repeat=num_variables)}
    for num_pressed_buttons in range(num_buttons+1):
        for buttons in combinations(range(num_buttons), num_pressed_buttons):
            pattern = tuple(map(sum, zip((0,) * num_variables, *(coeffs[i] for i in buttons))))
            parity_pattern = tuple(i%2 for i in pattern)
            if pattern not in out[parity_pattern]:
                out[parity_pattern][pattern] = num_pressed_buttons
    return out


def solve_single(coeffs: list[tuple[int, ...]], goal: tuple[int, ...]) -> int:
    pattern_costs = patterns(coeffs)\
    # @cache
    def solve_single_aux(goal: tuple[int, ...]) -> int:
        if all(i == 0 for i in goal):
            return 0
        answer = 1000000
        for pattern, pattern_cost in pattern_costs[tuple(i%2 for i in goal)].items():
            if all(i <= j for i, j in zip(pattern, goal)):
                new_goal = tuple((j - i)//2 for i, j in zip(pattern, goal))
                answer = min(answer, pattern_cost + 2 * solve_single_aux(new_goal))
        return answer
    return solve_single_aux(goal)


def solve(raw: str):
    score = 0
    lines = raw.splitlines()
    # for I, L in enumerate(lines, 1):
    for I, L in enumerate([lines[143]], 1):
        _, *coeffs, goal = L.split()
        goal = tuple(int(i) for i in goal[1:-1].split(","))
        coeffs = [[int(i) for i in r[1:-1].split(",")] for r in coeffs]
        coeffs = [tuple(int(i in r) for i in range(len(goal))) for r in coeffs]
        subscore = solve_single(coeffs, goal)
        print(f'Line {I}/{len(lines)}: answer {subscore}')
        score += subscore
    print(score)


def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def main():
    data = read_input()
    # data = data.split("\n")

    solve(data)


if __name__ == '__main__':
    main()


"""
https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
Line 1/166: answer 87
Line 2/166: answer 77
Line 3/166: answer 234
Line 4/166: answer 20
Line 5/166: answer 64
Line 6/166: answer 35
Line 7/166: answer 216
Line 8/166: answer 37
Line 9/166: answer 65
Line 10/166: answer 109
Line 11/166: answer 62
Line 12/166: answer 58
Line 13/166: answer 124
Line 14/166: answer 64
Line 15/166: answer 70 *
Line 16/166: answer 143
Line 17/166: answer 199
Line 18/166: answer 190
Line 19/166: answer 77
Line 20/166: answer 51
Line 21/166: answer 44
Line 22/166: answer 142
Line 23/166: answer 37
Line 24/166: answer 245
Line 25/166: answer 29
Line 26/166: answer 35
Line 27/166: answer 61
Line 28/166: answer 28
Line 29/166: answer 111
Line 30/166: answer 83
Line 31/166: answer 71
Line 32/166: answer 55
Line 33/166: answer 44
Line 34/166: answer 76
Line 35/166: answer 212
Line 36/166: answer 80
Line 37/166: answer 50
Line 38/166: answer 54
Line 39/166: answer 61
Line 40/166: answer 62
Line 41/166: answer 193
Line 42/166: answer 31
Line 43/166: answer 24
Line 44/166: answer 40
Line 45/166: answer 83
Line 46/166: answer 198
Line 47/166: answer 152
Line 48/166: answer 282
Line 49/166: answer 247
Line 50/166: answer 213
Line 51/166: answer 250
Line 52/166: answer 61
Line 53/166: answer 218
Line 54/166: answer 39
Line 55/166: answer 63
Line 56/166: answer 103
Line 57/166: answer 117
Line 58/166: answer 69
Line 59/166: answer 81
Line 60/166: answer 174
Line 61/166: answer 60
Line 62/166: answer 46
Line 63/166: answer 91
Line 64/166: answer 233
Line 65/166: answer 107
Line 66/166: answer 172
Line 67/166: answer 216
Line 68/166: answer 95
Line 69/166: answer 189
Line 70/166: answer 63
Line 71/166: answer 80
Line 72/166: answer 68
Line 73/166: answer 103
Line 74/166: answer 78
Line 75/166: answer 158
Line 76/166: answer 45
Line 77/166: answer 112
Line 78/166: answer 86
Line 79/166: answer 134
Line 80/166: answer 67
Line 81/166: answer 101
Line 82/166: answer 51
Line 83/166: answer 76
Line 84/166: answer 97
Line 85/166: answer 76
Line 86/166: answer 103
Line 87/166: answer 282
Line 88/166: answer 87
Line 89/166: answer 150
Line 90/166: answer 164
Line 91/166: answer 22
Line 92/166: answer 123
Line 93/166: answer 111
Line 94/166: answer 63
Line 95/166: answer 235
Line 96/166: answer 46
Line 97/166: answer 124
Line 98/166: answer 41
Line 99/166: answer 50
Line 100/166: answer 79
Line 101/166: answer 83
Line 102/166: answer 219
Line 103/166: answer 322
Line 104/166: answer 15
Line 105/166: answer 105
Line 106/166: answer 81
Line 107/166: answer 70
Line 108/166: answer 72
Line 109/166: answer 61
Line 110/166: answer 107
Line 111/166: answer 269
Line 112/166: answer 54
Line 113/166: answer 109
Line 114/166: answer 196
Line 115/166: answer 75
Line 116/166: answer 83
Line 117/166: answer 126
Line 118/166: answer 116
Line 119/166: answer 231
Line 120/166: answer 57
Line 121/166: answer 227
Line 122/166: answer 178
Line 123/166: answer 62
Line 124/166: answer 241
Line 125/166: answer 41
Line 126/166: answer 70
Line 127/166: answer 12
Line 128/166: answer 20
Line 129/166: answer 84
Line 130/166: answer 224
Line 131/166: answer 168
Line 132/166: answer 196
Line 133/166: answer 61
Line 134/166: answer 225
Line 135/166: answer 97
Line 136/166: answer 69
Line 137/166: answer 96
Line 138/166: answer 53
Line 139/166: answer 26
Line 140/166: answer 91
Line 141/166: answer 36
Line 142/166: answer 55
Line 143/166: answer 60
Line 144/166: answer 44
Line 145/166: answer 63
Line 146/166: answer 44
Line 147/166: answer 62
Line 148/166: answer 111
Line 149/166: answer 148
Line 150/166: answer 86
Line 151/166: answer 164
Line 152/166: answer 135
Line 153/166: answer 184
Line 154/166: answer 227
Line 155/166: answer 83
Line 156/166: answer 59
Line 157/166: answer 99
Line 158/166: answer 37
Line 159/166: answer 38
Line 160/166: answer 216
Line 161/166: answer 82
Line 162/166: answer 170
Line 163/166: answer 81
Line 164/166: answer 149
Line 165/166: answer 102
Line 166/166: answer 109
"""

