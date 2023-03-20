import pickle
import numpy as np
from pathlib import Path
from sklearn.metrics import accuracy_score
from get_files import file_names


files = file_names('test')
X_test_all = []
y_test_all = []


with open('model.txt', 'rb') as file: 
    model = pickle.load(file)


# Save predictions & print out results
Path('predict').mkdir(parents=True, exist_ok=True)

for file in files:
    X_test = np.genfromtxt(file[0], delimiter=',')
    X_test_all.extend(X_test)

    y_test = np.genfromtxt(file[1], delimiter=',')
    y_test_all.extend(y_test)

    prediction = model.predict(X_test)
    np.savetxt('predict/' + file[0][5:] + '_predict', prediction, delimiter=',', fmt='%.3e')

    print(f'For {file[0][5:]} ({len(y_test)} lines) accuracy score is', \
        accuracy_score(y_test, prediction))

prediction_all = model.predict(X_test_all)
np.savetxt('predict/X_test_all_predict', prediction_all, delimiter=',', fmt='%.3e')

print(f'Combined ({len(y_test_all)} lines) accuracy score is', \
    accuracy_score(y_test_all, prediction_all))
