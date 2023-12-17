from day_2 import AdventOfCode


def triangle_numbers(text):
    text_list = text.split("\n")
    out_list = []
    prehistory = []
    counter = 0

    for history in text_list:
        counter += 1
        history_lol = [history.split()]
        if counter == 46:
            print("46")
        for line in history_lol:
            line = [int(n) for n in line]
            if len(line) == 1:
                break
            else:
                new_line = [int(line[i+1]) - int(line[i]) for i in range(len(line)-1)]
            history_lol.append(new_line)
            line_check = [x for x in new_line if x == 0]
            if len(line_check) == len(new_line):
                break
        sum_list = [int(y[-1]) for y in history_lol]
        out_list.append(sum(sum_list))
        backwards = [int(z[0]) for z in history_lol]
        backwards.reverse()
        backwards = backwards[1:]
        #backwards2 = [backwards[b+1] - backwards[b] for b in range(len(backwards)-1)]
        b_list = [0]
        for i in range(len(backwards)):
            b_list.append(backwards[i] - b_list[i])
        prehistory.append(b_list[-1])

    print(f"sum of sums is {sum(out_list)}")
    print(f"sum of prehistory sums is {sum(prehistory)}")


def main():
    text = AdventOfCode.get_txt("9")
    triangle_numbers(text)


if __name__ == '__main__':
    main()
