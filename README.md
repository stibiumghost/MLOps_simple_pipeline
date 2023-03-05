# Simple machine learning pipeline 

data_creation.py generates three two-dimensional binary classification datasets, each of which split into two directories: train and test.

get_files.py is a module that returns (X_file_n, y_file_n) for every pair in the folder.

model_preprocessing.py performs preprocessing of data by using sklearn.preprocessing.StandardScaler.

model_preparation.py performs KNeighborsClassifier model training and save it as model.txt.

model_testing.py gets a predictions and accuracy scores to test datasets.

pipeline.sh runs all python-scripts sequentially.