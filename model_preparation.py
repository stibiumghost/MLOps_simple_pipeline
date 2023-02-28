import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from get_files import file_names


files = file_names('train')
model = KNeighborsClassifier(n_neighbors=5)


# train the model on every pair in the directory
for file in files:
    X_train = np.genfromtxt(file[0], delimiter=',')
    y_train = np.genfromtxt(file[1], delimiter=',')
    model.fit(X_train, y_train)


# save the model
with open('model.txt', 'wb') as file:
    pickle.dump(model, file)