import re


class AdventOfCode:
    def __init__(self):
        self.colours = ["red", "blue", "green"]
        return

    @staticmethod
    def get_txt(day):
        day = str(day)
        t = open(f"resources//day_{day}.txt")
        text = t.read()
        return text

    def sort_data(self, text):
        game_list = text.split("\n")

        game_lod = []

        for i, game in enumerate(game_list):
            game_data = game.split(": ")[1]
            game_data = re.split(r"[,;]", game_data)
            out_dict = {"game": i+1}
            for colour in self.colours:
                colour_score = [int(x.split()[0]) for x in game_data if colour in x]
                out_dict[colour] = max(colour_score)
            game_lod.append(out_dict)

        return game_lod

    def get_valid_games(self, game_lod, limit_dict):

        good_games = []

        for game in game_lod:
            good_game = True
            for colour in self.colours:
                if game[colour] > limit_dict[colour]:
                    good_game = False
                    break
            if good_game:
                good_games.append(game["game"])

        return good_games

    @staticmethod
    def game_powers(game_lod):

        out_list = []

        for game in game_lod:
            out_list.append(game["red"]*game["blue"]*game["green"])

        # out_list = [game["red"]*game["blue"]*game["green"] for game in game_lod]

        return out_list


def main():
    day_2 = AdventOfCode()
    text = day_2.get_txt(2)
    game_data = day_2.sort_data(text)
    limit_dict = {"red": 12, "blue": 14, "green": 13}
    valid_game_list = day_2.get_valid_games(game_data, limit_dict)
    print(f"valid games sum to: {sum(valid_game_list)}")
    powers_list = day_2.game_powers(game_data)
    print(f"Summed powers of games are: {sum(powers_list)}")


if __name__ == '__main__':
    main()
