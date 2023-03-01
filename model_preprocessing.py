from sklearn.preprocessing import StandardScaler
import numpy as np
from get_files import file_names

train_files = file_names('train')
test_files = file_names('test')

# Apply scaler to values
scaler = StandardScaler()
for file in train_files:
    X = np.genfromtxt(file[0], delimiter=',')
    np.savetxt(file[0], scaler.fit_transform(X), delimiter=',', fmt='%.3e')
for file in test_files:
    X = np.genfromtxt(file[0], delimiter=',')
    np.savetxt(file[0], scaler.transform(X), delimiter=',', fmt='%.3e')
