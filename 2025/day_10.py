import re
import itertools
from copy import copy


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


def part_2(data):
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


def main():
    data = read_input()
    data = data.split("\n")

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()

