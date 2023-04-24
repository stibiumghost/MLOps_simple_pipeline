import pandas as pd


# Read the dataset
titanic_df = pd.concat([pd.read_csv("train_df.csv")[["Pclass", "Sex", "Age"]],
                        pd.read_csv("test_df.csv")[["Pclass", "Sex", "Age"]]],
                        sort=True).reset_index(drop=True)

# NaN to mean (for Age)
titanic_df.Age = titanic_df.Age.fillna(titanic_df.Age.mean())

# Categorical to on hot encoding (for Sex)
sexes = pd.get_dummies(titanic_df.Sex)
titanic_df[sexes.columns.to_list()] = sexes[sexes.columns]
titanic_df.drop(columns=["Sex"], inplace=True)

titanic_df.to_csv("titanic_df.csv", index=False)