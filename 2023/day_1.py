import re
import pandas as pd


class DigitPull:
    def __init__(self):
        self.number_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        self.silly_num_dict = {
                "one": "o1ne",
                "two": "t2wo",
                "three": "t3hree",
                "four": "f4our",
                "five": "f5ive",
                "six": "s6ix",
                "seven": "s7even",
                "eight": "e8ight",
                "nine": "n9ine"
            }

    @staticmethod
    def get_text():
        t = open("resources//day_1.txt")
        text = t.read()
        text_list = text.split("\n")
        return text_list

    def word_to_nums_re(self, text_list):
        # this makes a regex pattern which allows overlapping matches
        num_string = "(?=(" + "|".join(self.number_dict.keys()) + r"|\d))"
        num_pattern = re.compile(num_string)
        # we compile it as we are building it from variables so it needs to be converted to a regex

        # i just had this to test the regex while i was working on it
        # text_list = ["eightwo1sevenine"]

        out_list = []
        for text in text_list:
            out_list.append("".join(re.findall(num_pattern, text)))

        # to easily manage the replacements i'm converting the list to a pandas series
        # think of it as a single pandas column
        out_list = pd.Series(out_list)
        out_list = out_list.replace(self.number_dict, regex=True)
        # and now back to a list so it works with my other functions
        out_list = out_list.to_list()

        return out_list

    def word_to_nums_silly(self, text_list):

        out_list = []
        for text in text_list:
            for key in self.silly_num_dict:
                if key in text:
                    text = text.replace(key, self.silly_num_dict[key])
            out_list.append(text)

        return out_list

    @staticmethod
    def extract_digits(text_list):

        out_lol = []
        for sub_text in text_list:
            sub_text = re.findall(r"\d", sub_text)
            out_lol.append(sub_text)

        #text_list = [re.findall(r"\d", x) for x in text_list]

        num_list = []
        for n in out_lol:
            num_list.append(int(n[0] + n[-1]))

        #calibration_values = [int(n[0] + n[-1]) for n in out_lol]

        return num_list

    @staticmethod
    def sum_data(number_list):
        x = sum(number_list)
        print(x)
        return


def main():
    digit_pull = DigitPull()
    text_list = digit_pull.get_text()
    text_list = digit_pull.word_to_nums_re(text_list)
    #text_list = digit_pull.word_to_nums_silly(text_list)
    num_list = digit_pull.extract_digits(text_list)
    digit_pull.sum_data(num_list)


if __name__ == '__main__':
    main()
