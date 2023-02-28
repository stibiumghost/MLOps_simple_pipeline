from os import listdir
from os.path import isfile, join

def file_names(directory):
    '''Returns (X_file_n, y_file_n) for every pair in the folder'''

    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    X_files = sorted([f for f in files if 'X' in f])
    y_files = sorted([f for f in files if 'y' in f])
    return [(directory + '/' + X, directory + '/' + y) for X, y in zip(X_files, y_files)]