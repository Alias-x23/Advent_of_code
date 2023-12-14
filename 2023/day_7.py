from day_2 import AdventOfCode
from collections import Counter


def order_hands(text):
    text = text.split("\n")
    hands = {x.split()[0]: int(x.split()[1]) for x in text}
    score_chart = {"A": 0, "K": 1, "Q": 2, "J": 3, "T": 4, "9": 5, "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12}
    win_chart = ["5", "41", "32", "311", "221", "2111", "11111"]

    score_dict = {}

    for hand in hands.keys():
        score_count = sorted(Counter(hand).values(), reverse=True)
        score_count = [str(s) for s in score_count]
        score = "".join(score_count)
        score_dict[hand] = score

    out_list = []

    for win in win_chart:
        temp_list = [h for h in score_dict.keys() if score_dict[h] == win]
        temp_list.sort(key=lambda val: [score_chart[j] for j in val])
        out_list += [hands[t] for t in temp_list]

    return out_list


def get_winnings(scores):

    winnings = 0

    for i, score in enumerate(scores):
        winnings += (score*(len(scores)-i))

    print(f"Winnings are {winnings}")


def main():
    text = AdventOfCode.get_txt("7")
    scores = order_hands(text)
    get_winnings(scores)


if __name__ == '__main__':
    main()
