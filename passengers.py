import pandas as pd

passengers = {
    "Name":[
        "Olate, Mr . Márcio Aléxis",
        "Andrade, Mr . Gustavo Ribeiro",
        "Olate, Mr . Gabriel Pizzo",
        "Barrros, Miss Clarice de Almeida"
    ],
    "Age":[48, 28, 27, 16],
    "Sex":["male", "male", "male", "female"],
}
print(type(passengers))

df = pd.DataFrame(passengers)
print(df)
print("#"*50)
sex_passengers=df["Sex"]

print(sex_passengers)
print("#"*50)
ages= pd.Series(df["Age"],name="Anos")
print(ages)
print("#"*50)
max_age=df["Age"].max()
print(max_age)
print("#"*50)
min_age = df["Age"].min()
print(min_age)
print("#"*50)
qut_age= len(df["Age"])
for age in df["Age"]:
    if age < 20:
        print(f'Maior: {age}')
print("#"*50)
print(df.describe())
print("#"*50)
print(df.info())
print("#"*50)
age_shape = df["Age"].shape
print(age_shape)
print("#"*50)
age_sex = df[["Age", "Sex"]]
print(age_sex)
print(age_sex.shape)
print("#"*50)
senior = [df["Age"][:-1] < 15]
print(senior)
print("#"*50)
ages = df["Age"]
print(ages.head())
print("#"*50)
age_none = list(filter(lambda x: x > 35, df["Age"]))
print(age_none)
print("#"*50)
age_no_na = df["Age"].notna()
print(age_no_na)
print("#"*50)
adult_names = df.loc[df["Age"] < 35, "Name"]
print(adult_names)
exp= df.iloc[0:3, 1:2]
print(exp)
print("#"*50)
df["Anos"] = df["Age"] > 34
print(df)
print("#"*50)
media = lambda x, y: sum(x.values) / len(y)
print(media(df["Age"], df["Age"]))
print("#"*50)
print(df["Age"].mean())
print("#"*50)
print(df["Age"].median())
print("#"*50)
print(df["Age"].describe())
print("#"*50)
df_agg =df.agg({
    "Age": ["max", "min", "mean", "skew"]
})
print(df_agg)
print("#"*50)
media_catego = df[["Age", "Sex"]].groupby("Sex").mean()
print(media_catego)
