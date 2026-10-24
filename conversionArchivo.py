import pandas as pd


file = pd.read_excel("data/dataset.xlsx")

file.to_csv("data/dataset.csv", index=False)