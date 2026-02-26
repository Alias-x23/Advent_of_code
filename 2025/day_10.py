import re
from copy import copy
from functools import cache
from collections import defaultdict
import itertools


def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def create_power_set(d):
    # create a list of all possible combinations for a given list, called a power set
    # list size will be 2^n -1
    n = len(d)
    output = []

    for i in range(2**n):
        inner = []
        for j in range(n):
            if i & 2**j:
                inner.append(d[j])
        if inner:
            output.append(inner)

    output = sorted(output, key=len)

    return output


def part_1(data):
    total = 0

    for r in data:
        buttons = r.split(" ")
        light_schema = re.sub(r"\]|\[", "", buttons.pop(0))
        buttons.pop(-1)
        buttons = [re.sub(r"[()]", "", b) for b in buttons]

        combinations = create_power_set(buttons)

        for combo in combinations:
            lights = ["." if str(combo).count(str(i)) % 2 == 0 else "#" for i in range(len(light_schema))]
            if "".join(lights) == light_schema:
                total += len(combo)
                break

    print(f"Part_1 total: {total}")


def part_2_old(data):
    total = 0

    for r in data:
        buttons = r.split(" ")
        buttons.pop(0)
        j_volts = re.sub(r"[{}]", "", buttons.pop(-1)).split(",")
        buttons = [re.sub(r"[()]", "", b) for b in buttons]

        light_config = ["." if int(j) % 2 == 0 else "#" for j in j_volts]

        combinations = create_power_set(buttons)

        possible_paths = []
        next_jolt = [int(j) for j in j_volts]

        for combo in combinations:
            path_val = 0
            lights = ["." if str(combo).count(str(i)) % 2 == 0 else "#" for i in range(len(light_config))]
            if "".join(lights) == "".join(light_config):
                path_val += len(combo)
                combo_copy = copy(combo)
                multiplier = 1

                while True:
                    light_switches = "".join(combo_copy)
                    # reduce the jolts by the found buttons
                    next_jolt = [next_jolt[i] - light_switches.count(str(i)) for i in range(len(next_jolt))]

                    if any([nj for nj in next_jolt if nj < 0]):
                        # break out if the combo would reduce the jolts below zero
                        break

                    if len([nj for nj in next_jolt if nj == 0]) == len(j_volts):
                        # if all jolts are 0 the path is valid and complete
                        possible_paths.append(path_val)
                        break

                    if len([nj for nj in next_jolt if nj % 2 == 0]) == len(j_volts):
                        # if all the values are even we can reduce all jolts by 2 until there is an odd value
                        # the next combo will then be multiplied by the reduction
                        multiplier = 2
                        next_jolt = [nj/2 for nj in next_jolt]
                        while True:
                            if len([nj for nj in next_jolt if nj % 2 == 0]) == len(j_volts):
                                multiplier *= 2
                                next_jolt = [nj / 2 for nj in next_jolt]
                            else:
                                break

                    next_config = ["." if nj % 2 == 0 else "#" for nj in next_jolt]

                    for next_combo in combinations:
                        new_lights = ["." if str(next_combo).count(str(i)) % 2 == 0 else "#"
                                      for i in range(len(next_config))]
                        if "".join(new_lights) == "".join(next_config):
                            path_val += len(next_combo) * multiplier
                            combo_copy = copy(next_combo)
                            multiplier = 1
                            break

        total += min(possible_paths)

    print(f"Part_2 total: {total}")



def part_2(data):
    total = 0

    # rows 14 and 143 are incorrect in the original first pass

    # for row, r in enumerate(data):
    for row, r in enumerate([data[143]]):
        buttons = r.split(" ")
        buttons.pop(0)
        j_volts = re.sub(r"[{}]", "", buttons.pop(-1)).split(",")
        j_volts = tuple([int(jv) for jv in j_volts])
        buttons = [re.sub(r"[()]", "", b) for b in buttons]

        combinations = create_power_set(buttons)
        combo_dict = defaultdict(lambda: [])

        for c in combinations:
            key = "".join(["." if str(c).count(str(i)) % 2 == 0 else "#" for i in range(len(j_volts))])
            combo_dict[key].append(c)

        # a "zero" buttons pressed is also added to allow the potential where the jolts remain even after halving
        # if len(combo_dict["."*len(j_volts)]) == 0:
        # if 0 < len(combo_dict["."*len(j_volts)]) < 2:
        combo_dict["."*len(j_volts)] = [[]]

        # add each missing combination to make sure code works as expected e.g. key of "....."
        # possible_keys = itertools.product([".", "#"], repeat=len(j_volts))
        # for pk in possible_keys:
        #     # if "".join(pk) not in combo_dict:
        #     if len(combo_dict["".join(pk)]) == 0:
        #         combo_dict["".join(pk)] = [[]]

        pause = "here"

        # cache the recursive function
        @cache
        def recursive_solver(next_jolt):
            """
            a recursive function, a function which calls itself to allow the nested looping
            the recursive function needs to keep calling itself with the next jolt target until either
            the jolt target is reduced to all zeros or no combination will work
            return the number of buttons pressed if the target is reached or a very large number if there is no
            working combination
            """

            if len([nj for nj in next_jolt if nj == 0]) == len(next_jolt):
                # if all jolts are 0 the path is valid and complete
                return 0

            result = 1000000
            combo_key = "".join(["." if int(j) % 2 == 0 else "#" for j in next_jolt])
            for combo in combo_dict[combo_key]:

                jolt_check = [next_jolt[i] - str(combo).count(str(i)) for i in range(len(next_jolt))]
                # change = [str(combo).count(str(i)) for i in range(len(next_jolt))]

                if not any([nj for nj in jolt_check if nj < 0]):
                    # if any of the jolt values are below zero the combo is invalid

                    # all jolt values will always be even after a move
                    # so we can divide the values by 2 and add double the next combo
                    new_jolt = [nj / 2 for nj in jolt_check]
                    # only return the result if it is lower than our limit
                    result = min(result, len(combo) + (2 * recursive_solver(next_jolt=tuple(new_jolt))))

            return result

        sub_total = recursive_solver(next_jolt=j_volts)
        total += sub_total
        print(f"Row {row}: {sub_total}")

    print(f"Part_2 total: {total}")


"""
    part 2 ramblings
    
    use the j-voltage to make a string of each light as many times as it needs to be pressed
    e.g. {3,2,4} == 000113333
    
    make each button into a dict key 
    for each button, sorted largest first 
        if there are characters from the j-voltage that can make it remove the used characters and continue
        if not try the next largest button 
        if the smallest button cannot be fit start again with the second largest in place of the largest
        if there are any chars left in the j-voltage after all dict keys same as above
    
    not sure this will work as need to get the generated orders right - might still be too intensive
    
    from the j-voltage string generate a list of all the combinations of potential buttons, 
    for each combination if there is a potential button that is not a real button continue
    if all potential buttons exist in the real buttons you have a solution
    
    
    still using the j-volt string
    get all combos of buttons like in pt1 
    ~~~~ remove all below largest j-voltage value ~~~~ this wont work as won't know ho many presses until after subbing
    for each combo
    make a regex pattern from the buttons
    re.sub all the buttons in the combo
    if the j-volt string is empty success
    else continue
    
    
    for each j-voltage get the index of the lowest value
    completed indexes = []
    get a list of all the buttons that have that index and no completed indexes
    build up the incremental pattern to get the minimal button presses
    
    rather than storing the combination just keep all the new j-voltage outcomes and 
    then repeat for each one until all values == 0 or fail?
    
    build the list of possible start combinations
    remove any that are invalid e.g. reduce a value to less than 0
    extend the lists to the next lowest value and check again, repeat to size of jolts 
    
    
    
"""


# 17827 is too high
# should give 17820 but not sure where the errors are
# likely from the way the combination dict is built / nature of the data as that is the only real difference

def main():
    data = read_input()
    data = data.split("\n")

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()



"""
Row 0: 87
Row 1: 77
Row 2: 234
Row 3: 20
Row 4: 64
Row 5: 35
Row 6: 216
Row 7: 37
Row 8: 65
Row 9: 109
Row 10: 62
Row 11: 58
Row 12: 124
Row 13: 64
Row 14: 76  *
Row 15: 143
Row 16: 199
Row 17: 190
Row 18: 77
Row 19: 51
Row 20: 44
Row 21: 142
Row 22: 37
Row 23: 245
Row 24: 29
Row 25: 35
Row 26: 61
Row 27: 28
Row 28: 111
Row 29: 83
Row 30: 71
Row 31: 55
Row 32: 44
Row 33: 76
Row 34: 212
Row 35: 80
Row 36: 50
Row 37: 54
Row 38: 61
Row 39: 62
Row 40: 193
Row 41: 31
Row 42: 24
Row 43: 40
Row 44: 83
Row 45: 198
Row 46: 152
Row 47: 282
Row 48: 247
Row 49: 213
Row 50: 250
Row 51: 61
Row 52: 218
Row 53: 39
Row 54: 63
Row 55: 103
Row 56: 117
Row 57: 69
Row 58: 81
Row 59: 174
Row 60: 60
Row 61: 46
Row 62: 91
Row 63: 233
Row 64: 107
Row 65: 172
Row 66: 216
Row 67: 95
Row 68: 189
Row 69: 63
Row 70: 80
Row 71: 68
Row 72: 103
Row 73: 78
Row 74: 158
Row 75: 45
Row 76: 112
Row 77: 86
Row 78: 134
Row 79: 67
Row 80: 101
Row 81: 51
Row 82: 76
Row 83: 97
Row 84: 76
Row 85: 103
Row 86: 282
Row 87: 87
Row 88: 150
Row 89: 164
Row 90: 22
Row 91: 123
Row 92: 111
Row 93: 63
Row 94: 235
Row 95: 46
Row 96: 124
Row 97: 41
Row 98: 50
Row 99: 79
Row 100: 83
Row 101: 219
Row 102: 322
Row 103: 15
Row 104: 105
Row 105: 81
Row 106: 70
Row 107: 72
Row 108: 61
Row 109: 107
Row 110: 269
Row 111: 54
Row 112: 109
Row 113: 196
Row 114: 75
Row 115: 83
Row 116: 126
Row 117: 116
Row 118: 231
Row 119: 57
Row 120: 227
Row 121: 178
Row 122: 62
Row 123: 241
Row 124: 41
Row 125: 70
Row 126: 12
Row 127: 20
Row 128: 84
Row 129: 224
Row 130: 168
Row 131: 196
Row 132: 61
Row 133: 225
Row 134: 97
Row 135: 69
Row 136: 96
Row 137: 53
Row 138: 26
Row 139: 91
Row 140: 36
Row 141: 55
Row 142: 60
Row 143: 45
Row 144: 63
Row 145: 44
Row 146: 62
Row 147: 111
Row 148: 148
Row 149: 86
Row 150: 164
Row 151: 135
Row 152: 184
Row 153: 227
Row 154: 83
Row 155: 59
Row 156: 99
Row 157: 37
Row 158: 38
Row 159: 216
Row 160: 82
Row 161: 170
Row 162: 81
Row 163: 149
Row 164: 102
Row 165: 109
"""

