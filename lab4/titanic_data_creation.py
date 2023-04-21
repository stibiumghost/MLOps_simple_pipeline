import pandas as pd
from catboost.datasets import titanic

# Load the Titanic dataset from CatBoost
train_df, test_df = titanic()

# Save the training and testing data frames as CSV files
train_df.to_csv("train_df.csv", index=False)
test_df.to_csv("test_df.csv", index=False)
