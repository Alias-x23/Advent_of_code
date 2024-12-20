import re

import pandas as pd


t = open("input3.txt")
text = t.read()
# this was the main issue ye bastard
text = text.replace("\n", "")

def get_muls(text):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
    matches = [x.replace("mul(", "").replace(")", "") for x in matches]
    out_list = [int(x.split(",")[0]) * int(x.split(",")[1]) for x in matches]
    return sum(out_list)


result = get_muls(text)
print(result)

new_text = re.sub(r"(don't\(\)){1,}.*?do\(\)", "", text)
new_text = new_text.split("don't()")[0]
result2 = get_muls(new_text)
print(result2)

print("hello")
