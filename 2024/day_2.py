import pandas as pd


df = pd.read_csv("input2.txt", header=None, names=["col1"])


def reactor_check(cell):
    cell = cell.split()
    cell = [int(x) for x in cell]

    if cell[0] == cell[1]:
        return 0

    increase = 0
    decrease = 0

    for i in range(len(cell) - 1):
        if increase > 0 and decrease > 0:
            return 0
        if cell[i]+4 > cell[i+1] > cell[i]:
            increase += 1
            continue
        if cell[i]-4 < cell[i+1] < cell[i]:
            decrease += 1
            continue
        else:
            return 0

    if increase > 0 and decrease > 0:
        return 0

    return 1

df["check"] = df["col1"].apply(reactor_check)

result1 = df["check"].sum()

print(result1)


# def reactor_check2(cell):
#     cell = cell.split()
#     cell = [int(x) for x in cell]
#
#     if cell[0] == cell[1]:
#         return 0
#
#     increase = 0
#     decrease = 0
#     skips = 0
#     pos = 0
#
#     while True:
#         if pos >= len(cell) - 1 or skips > 1:
#             break
#         if (cell[pos]+4 > cell[pos+1] > cell[pos]) and decrease == 0:
#             increase += 1
#             pos += 1
#             continue
#         if (cell[pos]-4 < cell[pos+1] < cell[pos]) and increase == 0:
#             decrease += 1
#             pos += 1
#             continue
#         else:
#             skips += 1
#             cell.pop(pos)
#
#     if increase > 0 and decrease > 0:
#         return 0
#
#     if skips > 1:
#         return 0
#
#     return 1

def reactor_check2(cell):
    cell = cell.split()
    cell = [int(x) for x in cell]

    data_list = [cell]
    for i in range(len(cell)):
        data_list.append(cell[:i] + cell[i+1:])

    for data in data_list:
        data = [data[i] - data[i+1] for i in range(len(data)-1)]

        increase = len([x for x in data if x > 0])
        decrease = len([x for x in data if x < 0])
        out_of_bounds = len([x for x in data if x < -3 or x > 3])
        zeros = data.count(0)

        if not (increase > 0 and decrease > 0) and zeros == 0 and out_of_bounds == 0:
            return 1

    return 0


df["check2"] = df["col1"].apply(reactor_check2)

result2 = df["check2"].sum()

print(result2)

print("hello")
