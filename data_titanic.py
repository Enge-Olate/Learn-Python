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


def apply_filters(df, survived=None, sex=None, pclass=None, min_fare=None):

    if survived is not None:
        df = df[df["Survived"] == survived]

    if sex:
        df = df[df["Sex"] == sex]

    if pclass:
        df = df[df["Pclass"] == pclass]

    if min_fare:
        df = df[df["Fare"] > min_fare]

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


def export_json(file):
    json_data = file.to_json(
        orient="records",
        force_ascii=False
    )
    return json_data



clean_data()    
menor = is_child()
print("="*50)
etarism = fix_age()
print(etarism)
print("="*50)
survives = analyses()
print(survives)
print("="*50)


from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/passengers", methods=["GET"])
def get_passengers():
    api_df = df[
    ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "Fare", "Embarked"]
]
    data = export_json(api_df)    
    return jsonify(data)
    
if __name__ == '__main__':
    app.run()
