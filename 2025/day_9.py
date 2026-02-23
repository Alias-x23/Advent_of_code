from copy import copy


def read_input():
    day = __file__[-4]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    out_list = []

    for i, col in enumerate(data):
        if i + 1 == len(data):
            break

        # areas = []
        # for r in data[i + 1:]:
        #     x = abs(int(data[i][0]) - int(r[0])) + 1
        #     y = abs(int(data[i][1]) - int(r[1])) + 1
        #
        #     areas.append(x*y)
        areas = [(abs(int(data[i][0]) - int(r[0]))+1) * (abs(int(data[i][1]) - int(r[1]))+1) for r in data[i + 1:]]

        out_list.append(sorted(areas, reverse=True)[0])

    print(f"Part_1 total: {max(out_list)}")


def part_2(data):
    out_list = []

    max_x = max([d[0] for d in data]) + 1

    largest_area = 0
    zero = 0

    extended_data = copy(data)
    extended_data.append(data[0])

    for i, cord in enumerate(data):
        # print(f"outer: {i}")
        if i + 1 == len(data):
            break

        for r in data[i + 1:]:
            zero += 1
            # print(f"inner {zero}")
            x = abs(int(cord[0]) - int(r[0])) + 1
            y = abs(int(cord[1]) - int(r[1])) + 1

            if x*y <= largest_area:
                continue

            area_cords = [
                cord,
                [cord[0], r[1]],
                r,
                [r[0], cord[1]]
            ]

            top_left = [min([a[0] for a in area_cords]) + 1, min([b[1] for b in area_cords]) + 1]
            top_right = [max([a[0] for a in area_cords]) - 1, min([b[1] for b in area_cords]) + 1]
            bot_left = [min([a[0] for a in area_cords]) + 1, max([b[1] for b in area_cords]) - 1]
            bot_right = [max([a[0] for a in area_cords]) - 1, max([b[1] for b in area_cords]) - 1]

            corner_cords = [top_left, top_right, bot_left, bot_right]

            bad_cords = False

            # if each corner passes through the same number of borders they must all exist in the area
            all_crosses = []
            for corner_cord in corner_cords:
                potential_borders = [[extended_data[n][1], extended_data[n + 1][1]] for n in
                                     range(len(extended_data) - 1)
                                     if extended_data[n][0] == extended_data[n + 1][0]
                                     and extended_data[n + 1][0] in range(corner_cord[0], max_x)]
                if not potential_borders:
                    bad_cords = True
                    break

                # this also needs to also check the y but it worked without it
                border_crosses = 0
                border_crosses += len([pb for pb in potential_borders if min(pb) <= corner_cord[1] <= max(pb)])
                if not border_crosses:
                    bad_cords = True
                    break

                # if any([corner_cord for ed_cord in range(len(extended_data) - 1)
                #         if min(extended_data[ed_cord][0], extended_data[ed_cord + 1][0]) <= corner_cord[0] <=
                #         max(extended_data[ed_cord][0], extended_data[ed_cord + 1][0])
                #         and corner_cord[1] == extended_data[ed_cord][1]
                #         and corner_cord[1] == extended_data[ed_cord + 1][1]]):
                #     border_crosses -= 1

                if border_crosses % 2 == 0:
                    bad_cords = True
                    break

                all_crosses.append(border_crosses)

            if len(list(set(all_crosses))) > 1:
                bad_cords = True
                break

            # x_cords = [d[0] for d in area_cords]
            # y_cords = [d[1] for d in area_cords]
            #
            # sides = [
            #     {"y": max(y_cords), "min": min(x_cords), "max": max(x_cords)},
            #     {"y": min(y_cords), "min": min(x_cords), "max": max(x_cords)},
            #     {"x": max(x_cords), "min": min(y_cords), "max": max(y_cords)},
            #     {"x": min(x_cords), "min": min(y_cords), "max": max(y_cords)}
            # ]
            #
            # for side in sides:
            #     if "y" in side.keys():
            #         for px in range(side["min"], side["max"]):
            #             if not check_perimeter([px, side["y"]], extended_data=extended_data, max_x=max_x):
            #                 bad_cords = True
            #                 break
            #     if bad_cords:
            #         break
            #     if "x" in side.keys():
            #         for py in range(side["min"], side["max"]):
            #             if not check_perimeter([side["x"], py], extended_data=extended_data, max_x=max_x):
            #                 bad_cords = True
            #                 break

            if not bad_cords:
                largest_area = x*y

    print(f"Part_2 total: {largest_area}")


# def get_outline(data):
#     # get the co-ords for the perimeter of a shape
#
#     outline = copy(data)
#
#     for i, cord in enumerate(data):
#
#         if i == (len(data) - 1):
#             next_point = data[0]
#         else:
#             next_point = data[i + 1]
#
#         step = 1
#
#         if cord[0] == next_point[0]:
#             if next_point[1] < cord[1]:
#                 step = -1
#             new_borers = [[cord[0], r] for r in range(cord[1], next_point[1], step)]
#             new_borers = [nb for nb in new_borers if nb not in outline]
#             outline += new_borers
#
#         else:
#             if next_point[0] < cord[0]:
#                 step = -1
#             new_borers = [[r, cord[1]] for r in range(cord[0], next_point[0], step)]
#             new_borers = [nb for nb in new_borers if nb not in outline]
#             outline += new_borers
#
#     return outline

#
# def alt_get_outline(data):
#     # get the co-ords for the perimeter of a shape
#
#     outline = copy(data)
#
#     x_cords = [d[0] for d in data]
#     y_cords = [d[1] for d in data]
#
#     top_side = [[x, max(y_cords)] for x in range(min(x_cords), max(x_cords))]
#     bottom_side = [[x, min(y_cords)] for x in range(min(x_cords), max(x_cords))]
#     right_side = [[max(x_cords), y] for y in range(min(y_cords), max(y_cords))]
#     left_side = [[min(x_cords), y] for y in range(min(y_cords), max(y_cords))]
#
#     for side in [top_side, bottom_side, right_side, left_side]:
#         outline += [s for s in side if s not in outline]
#     return outline


def check_perimeter(p, extended_data, max_x):
    # check a perimeter co-ordinate to see if it is valid

    if p in extended_data:
        return True

    # # if the co-ord is on an edge it's fine
    if any([p for ed_cord in range(len(extended_data) - 1)
            if min(extended_data[ed_cord][0], extended_data[ed_cord + 1][0]) <= p[0] <=
            max(extended_data[ed_cord][0], extended_data[ed_cord + 1][0])
            and p[1] == extended_data[ed_cord][1] and p[1] == extended_data[ed_cord + 1][1]]):
        return True

    # if any([p for ed_cord in range(len(extended_data) - 1)
    #         if min(extended_data[ed_cord][1], extended_data[ed_cord + 1][1]) <= p[1] <=
    #         max(extended_data[ed_cord][1], extended_data[ed_cord + 1][1])
    #         and p[0] == extended_data[ed_cord][1] and p[0] == extended_data[ed_cord + 1][0]]):
    #     return True

    # get each co-ord pair where the x axis are the same for any point in the area's perimeter
    potential_borders = [[extended_data[n][1], extended_data[n + 1][1]] for n in range(len(extended_data) - 1)
                         if extended_data[n][0] == extended_data[n + 1][0]
                         and extended_data[n + 1][0] in range(p[0] + 1, max_x)]
    if not potential_borders:
        return False


    border_crosses = 0
    border_crosses += len([pb for pb in potential_borders if min(pb) <= p[1] <= max(pb)])
    if not border_crosses:
        return False

    if border_crosses % 2 != 0:
        return True
    return False


def main():
    data = read_input()
    data_list = data.split("\n")
    co_ords = [[int(c) for c in d.split(",")] for d in data_list]

    part_1(co_ords)
    part_2(co_ords)


if __name__ == '__main__':
    main()

    # getting the full outline was not actually useful
    # outline = copy(data)
    # for i, cord in enumerate(data):
    #
    #     if i == (len(data) - 1):
    #         next_point = data[0]
    #     else:
    #         next_point = data[i + 1]
    #
    #     step = 1
    #
    #     if cord[0] == next_point[0]:
    #         if next_point[1] < cord[1]:
    #             step = -1
    #         new_borers = [[cord[0], r] for r in range(cord[1], next_point[1], step)]
    #         new_borers = [nb for nb in new_borers if nb not in outline]
    #         outline += new_borers
    #
    #     else:
    #         if next_point[0] < cord[0]:
    #             step = -1
    #         new_borers = [[r, cord[1]] for r in range(cord[0], next_point[0], step)]
    #         new_borers = [nb for nb in new_borers if nb not in outline]
    #         outline += new_borers

# for p in perimeters:
#     x_edge = []
#     y_edge = []
#
#     # if the co-ord is on an edge it's fine
#     if any([p for ed_cord in range(len(extended_data) - 1)
#             if min(extended_data[ed_cord][0], extended_data[ed_cord + 1][0]) <= p[0] <=
#             max(extended_data[ed_cord][0], extended_data[ed_cord + 1][0])
#             and p[1] == extended_data[ed_cord][1] and p[1] == extended_data[ed_cord + 1][1]]):
#     # if x_edge:
#         continue
#     if any([p for ed_cord in range(len(extended_data) - 1)
#             if min(extended_data[ed_cord][1], extended_data[ed_cord + 1][1]) <= p[1] <=
#             max(extended_data[ed_cord][1], extended_data[ed_cord + 1][1])
#             and p[0] == extended_data[ed_cord][1] and p[0] == extended_data[ed_cord + 1][0]]):
#     # if y_edge:
#         continue
#
#     # get each co-ord pair where the x axis are the same for any point in the area's perimeter
#     potential_borders = [[extended_data[n][1], extended_data[n+1][1]] for n in range(len(extended_data) - 1)
#                          if extended_data[n][0] == extended_data[n+1][0]
#                          and extended_data[n+1][0] in range(p[0], max_x)]
#     if not potential_borders:
#         bad_cords = True
#         break
#
#     border_crosses = 0
#     for pb in potential_borders:
#         border_crosses += len([b for b in range(p[0], max_x) if min(pb) <= p[1] <= max(pb)])
#
#     # border_crosses = 0
#     # for b in range(p[0], max_x):
#     #     border_crosses += len([p for ed_cord in range(len(extended_data) - 1)
#     #                            if min(extended_data[ed_cord][1], extended_data[ed_cord + 1][1]) <= p[1] <=
#     #                            max(extended_data[ed_cord][1], extended_data[ed_cord + 1][1])
#     #                            and b == extended_data[ed_cord][0] and b == extended_data[ed_cord + 1][0]])
#     if border_crosses % 2 != 0:
#         continue
#     bad_cords = True
#     break

