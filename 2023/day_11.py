from day_2 import AdventOfCode
import numpy as np
from scipy.spatial.distance import cdist
from scipy.spatial import distance_matrix


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


def get_distances(universe):

    pos_list = []

    for r, row in enumerate(universe):
        for c, col in enumerate(row):
            if universe[r][c] == ".":
                continue
            pos_list.append([r+1, c+1])

    uni_array = np.array([np.array(p) for p in pos_list])
    matrix = cdist(uni_array, uni_array)
    #matrix2 = distance_matrix(uni_array, uni_array)

    sum_list = [sorted(m)[1] for m in matrix]

    for m in matrix:
        mn = sorted(m)

    return


def main():
    text = AdventOfCode.get_txt("11")
    universe = expand_and_sort(text)
    get_distances(universe)


if __name__ == '__main__':
    main()
