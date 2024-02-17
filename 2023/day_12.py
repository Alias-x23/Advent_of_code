from day_2 import AdventOfCode
import itertools
import re


def sort_data(text):
    text_list = text.split("\n")
    text_lol = [t.split() for t in text_list]

    return text_lol


def get_patterns(text_lol):

    test = list(itertools.product([".", "#"], repeat=3))

    out_list = []

    for line in text_lol:
        check = list(line[0])
        missing = check.count("?")
        variants = list(itertools.product([".", "#"], repeat=missing))

        pattern_info = line[1].split(",")
        pattern_info = [int(p) for p in pattern_info]
        variants = [vr for vr in variants if vr.count("#") == (sum(pattern_info) - check.count("#"))]

        possibles = []
        for v in variants:
            swap = 0
            temp_list = []
            for c in check:
                if c == "?":
                    temp_list.append(v[swap])
                    swap += 1
                else:
                    temp_list.append(c)
            possibles.append("".join(temp_list))

        pattern_list = [f"#{{{p}}}" for p in pattern_info]
        pat = "\.*"+"\.+".join(pattern_list)+"\.*"
        pattern = re.compile(pat)
        matches = 0
        # for pos in possibles:
        #     if re.match(pattern, pos):
        #         matches += 1
        matches = [pos for pos in possibles if re.match(pattern, pos)]
        out_list.append(len(matches))

    print(f"Total possible matches = {sum(out_list)}")

    return out_list


def unfold_sort(text, perm_list):
    text_list = text.split("\n")
    text_lol = [t.split() for t in text_list]

    new_out = []

    for i, line in enumerate(text_lol):
        # spring_string = "?".join([line[0] for i in range(5)])
        # spring_pat = ",".join([line[1] for i in range(5)])
        if line[0][-1] == "#":
            spring_string = f".{line[0]}"
        else:
            spring_string = f"?{line[0]}"
        new_out.append([spring_string, line[1]])

    return new_out


def main():
    text = AdventOfCode.get_txt("12")
    text_lol = sort_data(text)
    perm_list = get_patterns(text_lol)
    unfolded_text = unfold_sort(text, perm_list)
    alt_perms = get_patterns(unfolded_text)
    final_perms = []
    for i, p in enumerate(perm_list):
        final_perms.append(p*(alt_perms[i]**4))
    print(f"Sum of the final perms is {sum(final_perms)}")


if __name__ == '__main__':
    main()
