from copy import copy
import numpy as np
from scipy.spatial import KDTree


def read_input():
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = 0

    data_array = np.array(data)

    out_list = []

    # points_tree = KDTree(data_array)
    # points_in_rad = points_tree.query_pairs()
    # x, i = points_tree.query(data_array, 1)

    for i, col in enumerate(data_array):
        if i == len(data_array):
            break
        distances = [(np.linalg.norm(data_array[i] - r)) for r in data_array[i+1:]]

        # nearest_index = distances.index(sorted(distances)[1])
        # pair_detail = (list(data_array[i]), list(data_array[nearest_index]), sorted(distances)[1])
        # reverse_pair = (list(data_array[nearest_index]), list(data_array[i]), sorted(distances)[1])

        out_list += [(list(data_array[i]), list(junk), distances[j]) for j, junk in enumerate(data_array[i+1:])]

        # for j, junction in enumerate(data_array[i+1:]):
        #     # if j == i:
        #     #     continue
        #     pair_detail = (list(data_array[i]), list(junction), distances[j])
        #     # reverse_pair = (list(data_array[j]), list(data_array[i]), distances[j])
        #     # if reverse_pair not in out_list:
        #     out_list.append(pair_detail)
        # out_list = sorted(out_list, key=lambda x: x[2])

    # out_array = np.array(out_list)

    out_list = sorted(out_list, key=lambda x: x[2])
    part_2_data = copy(out_list)

    if len(data) == 20:
        out_list = out_list[:10]
    else:
        out_list = out_list[:1000]

    circuit_list = []
    for pair in out_list:
        check = 0
        circuit_ids = []
        first_second = 0
        for c, circuit in enumerate(circuit_list):

            if pair[0] in circuit and pair[1] in circuit:
                check += 1
                break

            if pair[0] in circuit and pair[1] not in circuit:
                check += 1
                circuit_ids.append(c)
                first_second = 1

            if pair[1] in circuit and pair[0] not in circuit:
                check += 1
                circuit_ids.append(c)
                first_second = 0

        if len(circuit_ids) == 2:
            new_circuit = copy(circuit_list[circuit_ids[0]])
            new_circuit += circuit_list[circuit_ids[1]]
            for c_id in sorted(circuit_ids, reverse=True):
                circuit_list.pop(c_id)
            circuit_list.append(new_circuit)

        if len(circuit_ids) == 1:
            circuit_list[circuit_ids[0]].append(pair[first_second])

        if check == 0:
            circuit_list.append([pair[0], pair[1]])

    out_counts = sorted([len(sub_list) for sub_list in circuit_list], reverse=True)

    total = out_counts[0] * out_counts[1] * out_counts[2]

    print(f"Part_1 total: {total}")

    part_2(part_2_data)


def part_2(data):
    total = 0

    total_circuits = 1000
    if len(data) == 190:
        total_circuits = 20

    circuit_list = []
    for pair in data:
        check = 0
        circuit_ids = []
        first_second = 0
        for c, circuit in enumerate(circuit_list):

            if pair[0] in circuit and pair[1] in circuit:
                check += 1
                break

            if pair[0] in circuit and pair[1] not in circuit:
                check += 1
                circuit_ids.append(c)
                first_second = 1

            if pair[1] in circuit and pair[0] not in circuit:
                check += 1
                circuit_ids.append(c)
                first_second = 0

        if len(circuit_ids) == 2:
            new_circuit = copy(circuit_list[circuit_ids[0]])
            new_circuit += circuit_list[circuit_ids[1]]

            for c_id in sorted(circuit_ids, reverse=True):
                circuit_list.pop(c_id)
            circuit_list.append(new_circuit)

        if len(circuit_ids) == 1:
            circuit_list[circuit_ids[0]].append(pair[first_second])

        if check == 0:
            circuit_list.append([pair[0], pair[1]])

        # this is the new for part 2
        if len(circuit_list) == 1 and len(circuit_list[0]) == total_circuits:
            total = pair[0][0] * pair[1][0]
            break

    print(f"Part_2 total: {total}")


def main():
    data = read_input()

    data_list = data.split("\n")
    co_ords = [[int(c) for c in d.split(",")] for d in data_list]

    part_1(co_ords)
    # part_2(co_ords)


if __name__ == '__main__':
    main()

