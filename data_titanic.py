import pandas as pd

df = pd.read_csv('./titanic.csv')
print(type(df))
average_sex_age = df[["Age", "Sex"]].groupby("Sex").mean()
print(average_sex_age)

amount_age = df["Age"].describe()
print(amount_age)

males = df[df["Sex"] == "male"]
print(males.head(10))

have = df[df["Name"].str.contains("Rene")]
print(have)