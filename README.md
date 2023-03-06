# Simple machine learning pipeline 

1. data_creation.py generates three datasets for binary classification using datasets.make_moons.
2. model_preprocessing.py normalizes the data using preprocessing.StandardScaler.
3. model_preparation.py trains and saves the model using neighbors.KNeighborsClassifier.
4. model_testing.py makes predictions and evaluates their accuracy scores.
5. pipeline.sh runs the scripts.

*get_files.py returns file names in a folder when called.
