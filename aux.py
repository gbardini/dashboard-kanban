import pandas as pd

df = pd.read_csv("./data/file.csv", sep=";", encoding="ISO-8859-1")

print(df.columns)