import pandas as pd


df = pd.read_csv("input_1.txt", header=None, delimiter="   ", names=["col1", "col2"])

for col in df.columns:
    temp_list = sorted(df[col].to_list())
    df[col] = temp_list

df["dif"] = (df["col1"] - df["col2"]).abs()

result = df["dif"].sum()

print(result)

count_dict = df["col2"].value_counts().to_dict()

df["p2"] = df["col1"].apply(lambda x: count_dict[x]*x if x in count_dict.keys() else 0)

result2 = df["p2"].sum()
print(result2)

print("hello")
