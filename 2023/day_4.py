from day_2 import AdventOfCode
from collections import defaultdict


def split_data(text):
    text_list = text.split("\n")

    games = []

    for card in text_list:
        card = card.split(": ")[1]
        card_pair = card.split("|")
        sub_list = []
        for c in card_pair:
            sub_list.append(c.split())
        games.append(sub_list)

    return games


def calculate_points(games):

    out_list = []

    for g in games:
        winners = [x for x in g[1] if x in g[0]]
        if len(winners) != 0:
            points = 2**(len(winners)-1)
            out_list.append(points)

    return out_list


def multiply_cards(games):

    card_dict = defaultdict(lambda: 1)

    for i, g in enumerate(games):
        card_dict[i] += 0
        winners = [x for x in g[1] if x in g[0]]
        if len(winners) != 0:
            for j in range(len(winners)):
                card_dict[i+j+1] += card_dict[i]

    return card_dict.values()


def main():
    text = AdventOfCode.get_txt("4")
    game_list = split_data(text)
    point_list = calculate_points(game_list)
    AdventOfCode.sum_list("Point list", point_list)
    card_count = multiply_cards(game_list)
    AdventOfCode.sum_list("Card count", card_count)


if __name__ == '__main__':
    main()
