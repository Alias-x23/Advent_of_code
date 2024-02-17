from day_2 import AdventOfCode
import numpy as np
from scipy.spatial.distance import cdist


def expand_and_sort(text):
    text_list = text.split("\n")
    row_lol = []

    for row in text_list:
        row = list(row)
        row_lol.append(row)
        if "#" not in row:
            row_lol.append(row)

    row_lol = [[r[i] for r in row_lol] for i in range(len(row_lol[0]))]

    col_lol = []

    for col in row_lol:
        col_lol.append(col)
        if "#" not in col:
            col_lol.append(col)

    # i don't think i need to do this but i have returned the universe to its normal orientation
    universe = [[c[i] for c in col_lol] for i in range(len(col_lol[0]))]

    return universe


def get_distances(universe, mega=False):

    pos_list = []
    mega_r = 0

    for r, row in enumerate(universe):
        if row[0] == 0:
            mega_r += 999999
        mega_c = 0
        for c, col in enumerate(row):
            if universe[r][c] == 0:
                mega_c += 999999
                continue
            if universe[r][c] == ".":
                continue
            if mega:
                pos_list.append([r+1+mega_r, c+1+mega_c])
            else:
                pos_list.append([r+1, c+1])

    # turns out i don't need to do the fancy way
    # uni_array = np.array([np.array(p) for p in pos_list])
    # matrix = cdist(uni_array, uni_array)
    # sum_list = [sorted(m)[1:] for m in matrix]

    dist = 0

    for i, pos in enumerate(pos_list):
        dist_list = [abs(pos_list[i][0] - pos_list[i+x][0]) + abs(pos_list[i][1] - pos_list[i+x][1])
                     for x in range(len(pos_list[i:]))]
        dist += sum(dist_list)

    print(f"Sum of all shortest pairs is {dist}")

    return


def extreme_expand(text):
    text_list = text.split("\n")
    row_lol = []

    for row in text_list:
        row = list(row)
        if "#" in row:
            row_lol.append(row)
        else:
            row_lol.append([0 for i in range(len(row))])

    row_lol = [[r[i] for r in row_lol] for i in range(len(row_lol[0]))]

    col_lol = []

    for col in row_lol:
        if "#" in col:
            col_lol.append(col)
        else:
            col_lol.append([0 for i in range(len(col))])

    universe = [[c[i] for c in col_lol] for i in range(len(col_lol[0]))]

    return universe


def main():
    text = AdventOfCode.get_txt("11")
    universe = expand_and_sort(text)
    get_distances(universe)
    big_universe = extreme_expand(text)
    get_distances(big_universe, mega=True)


if __name__ == '__main__':
    main()
