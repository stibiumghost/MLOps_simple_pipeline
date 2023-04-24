import pandas as pd


# Read the dataset
titanic_df = pd.concat([pd.read_csv("train_df.csv")[["Pclass", "Sex", "Age"]],
                        pd.read_csv("test_df.csv")[["Pclass", "Sex", "Age"]]],
                        sort=True).reset_index(drop=True)

# NaN to mean (for Age)
titanic_df.Age = titanic_df.Age.fillna(titanic_df.Age.mean())

titanic_df.to_csv("titanic_df.csv", index=False)