from functools import cache
import math


def read_input():
    file_name = __file__
    day = file_name.split("day_")[1].split(".py")[0]
    t = open(f"inputs/day{day}.txt")
    return t.read()


def part_1(data):
    total = []

    # this version only works while not cached
    # def recursive_path_finder(key):
    #     for route in data[key]:
    #         if route == "out":
    #             total.append(1)
    #             return
    #         recursive_path_finder(route)

    # recursive_path_finder("you")

    @cache
    def recursive_path_finder(key):
        paths = 0

        if key == "out":
            return 1

        for route in data[key]:
            paths += recursive_path_finder(route)

        return paths

    result = recursive_path_finder("you")

    print(f"Part_1 total: {result}")


def part_2(data):
    total = []

    # @cache
    # def recursive_path_finder(key, check):
    #
    #     for route in data[key]:
    #
    #         match route:
    #             case "fft":
    #                 check += "fft"
    #                 recursive_path_finder(route, check)
    #             case "dac":
    #                 check += "dac"
    #                 recursive_path_finder(route, check)
    #
    #             case "out":
    #                 if "fft" in check and "dac" in check:
    #                     total.append(1)
    #                 return
    #
    #         if "fft" in data[key]:
    #             check.replace("fft", "", 1)
    #         if "dac" in data[key]:
    #             check.replace("dac", "", 1)
    #
    #         recursive_path_finder(route, check)
    #
    # recursive_path_finder("svr", check="")

    # all_paths = []
    #
    # @cache
    # def recursive_path_finder(key, path):
    #
    #     if key in ["fft", "dac"]:
    #         path += key
    #
    #     for route in data[key]:
    #         if route == "out":
    #             if "fft" in path and "dac" in path:
    #                 total.append(1)
    #             all_paths.append(path)
    #             return
    #         recursive_path_finder(route, path)
    #
    # recursive_path_finder("svr", path="")

    # 22 is not the answer, but it is the answer I keep getting, while cache is on in any case

    @cache
    def recursive_path_finder(key, end):
        paths = 0

        if key == end:
            return 1

        if key not in data:
            return 0

        for route in data[key]:
            paths += recursive_path_finder(route, end=end)

        return paths

    total.append(recursive_path_finder("svr", "fft"))
    total.append(recursive_path_finder("fft", "dac"))
    total.append(recursive_path_finder("dac", "out"))

    print(f"Part_2 total: {math.prod(total)}")


def main():
    data = read_input()
    data = data.split("\n")

    data = {d.split(":")[0]: d.split(":")[1].strip().split(" ") for d in data}

    # part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()


"""
    @cache
    def recursive_path_finder(key, fft, dac):

        for route in data[key]:

            match route:
                case "fft":
                    fft = True
                    recursive_path_finder(route, fft, dac)
                case "dac":
                    dac = True
                    recursive_path_finder(route, fft, dac)

                case "out":
                    if fft and dac:
                        total.append(1)
                    return

            if "fft" in data[key]:
                fft = False
            if "dac" in data[key]:
                dac = False

            recursive_path_finder(route, fft, dac)

    recursive_path_finder("svr", False, False)



    def recursive_path_finder(key, check):

        for route in data[key]:

            match route:
                case "fft":
                    check.append("fft")
                    recursive_path_finder(route, check)
                case "dac":
                    check.append("dac")
                    recursive_path_finder(route, check)

                case "out":
                    if check[0] == 1 and check[1] == 1:
                        total.append(1)
                    return

            if "fft" in data[key] and "fft" in check:
                check.remove("fft")
                check.replace("fft", "")
            if "dac" in data[key] and "dac" in check:
                check.remove("dac")

            recursive_path_finder(route, check)

    recursive_path_finder("svr", [])
    
    
    def recursive_path_finder(key, end):
        if key not in data:
            return
        for route in data[key]:
            if route == end:
                total.append(1)
                return
            recursive_path_finder(route, end=end)

    sub_total = []
    recursive_path_finder("svr", end="fft")
    sub_total.append(len(total))
    total = []
    recursive_path_finder("fft", end="dac")
    sub_total.append(len(total))
    total = []
    recursive_path_finder("dac", end="out")
    sub_total.append(len(total))

    print(f"Part_2 total: {sum(sub_total)}")
    
"""
