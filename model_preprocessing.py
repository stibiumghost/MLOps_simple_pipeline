from sklearn.preprocessing import StandardScaler
import numpy as np
from get_files import file_names

train_files = file_names('train')
test_files = file_names('test')
files = train_files + test_files

# Apply scaler to values
scaler = StandardScaler()
for file in files:
    X = np.genfromtxt(file[0], delimiter=',')
    np.savetxt(file[0], scaler.fit_transform(X), delimiter=',', fmt='%.3e')
