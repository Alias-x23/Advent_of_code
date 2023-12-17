from day_2 import AdventOfCode
from collections import Counter


def order_hands(text):
    text = text.split("\n")
    hands = {x.split()[0]: int(x.split()[1]) for x in text}
    score_chart = {"A": 0, "K": 1, "Q": 2, "J": 3, "T": 4, "9": 5,
                   "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12}
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


def order_hands_joker(text):
    text = text.split("\n")
    hands = {x.split()[0]: int(x.split()[1]) for x in text}
    score_chart = {"A": 0, "K": 1, "Q": 2, "T": 4, "9": 5, "8": 6, "7": 7,
                   "6": 8, "5": 9, "4": 10, "3": 11, "2": 12, "J": 13}
    win_chart = ["5", "41", "32", "311", "221", "2111", "11111"]

    score_dict = {}

    for hand in hands.keys():
        score_count = Counter(hand)
        if "J" in score_count and hand != "JJJJJ":
            j_count = score_count.pop("J")
            top_key = max(zip(score_count.values(), score_count.keys()))[1]
            score_count[top_key] += j_count
        score_count = sorted(score_count.values(), reverse=True)
        score_count = [str(s) for s in score_count]
        score = "".join(score_count)
        score_dict[hand] = score

    out_list = []

    for win in win_chart:
        temp_list = [h for h in score_dict.keys() if score_dict[h] == win]
        temp_list.sort(key=lambda val: [score_chart[j] for j in val])
        out_list += [hands[t] for t in temp_list]

    return out_list


def main():
    text = AdventOfCode.get_txt("7")
    scores = order_hands(text)
    get_winnings(scores)
    joker_scores = order_hands_joker(text)
    get_winnings(joker_scores)


if __name__ == '__main__':
    main()
