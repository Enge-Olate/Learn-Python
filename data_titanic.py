import pandas as pd

df = pd.read_csv(
    './titanic.csv',
    dtype={
        "PassengerId": "int64",
        "Survived": "int8",
        "Pclass": "int8",
        "Sex":"category",
        "Embarked": "category"
    }
)
df.describe()
df.info()
df.head()
df.isna().sum()

def get_filters():
    df[df["Survived"] == 1]
    df[(df["Sex"] == "female")& (df["Pclass"] == 1)]
    df[(df["Sex"] == 'male') & (df["Fare"] > 20.000)]
    
    return df

def clean_data():
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna("S")
    df.drop(columns=["Cabin"])
    return df

def is_child():
    df["IsChild"] = df["Age"] < 18
    return df[df["IsChild"] == True]

def fix_age():
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0, 12, 18, 60, 100],
        labels=["Criança", "Adolescente", "Adulto", "Idoso"]
    )
    return df[df["AgeGroup"] == "Criança"]

def analyses():
    survive = df.groupby("Sex")["Survived"].mean().round(2)
    survive_per_class = df.groupby(["Pclass", "Sex"])["Survived"].agg(
        taxa_sobrevivencia="mean",
        total_passageiros="count"
    )
    
    return survive, survive_per_class
    

clean_data()    
menor = is_child()
print("="*50)
etarism = fix_age()
print(etarism)
print("="*50)
survives = analyses()
print(survives)
