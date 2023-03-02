import numpy as np
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


rand = 42
test_size = 0.2
new_folders = ['test', 'train']
samples = int(np.random.randint(50, 400) * 6 / test_size)


# generate the dataset and split it in test/train
X, y = make_moons(n_samples=samples, noise=0.25, random_state=rand)
data = list(train_test_split(X, y, test_size=test_size, random_state=rand))


for name in new_folders:
    Path(name).mkdir(parents=True, exist_ok=True)


for name, group in zip(['X_train', 'X_test', 'y_train', 'y_test'], data):
    if new_folders[0] in name:
        name = new_folders[0] + '/' + name
    else:
        name = new_folders[1] + '/' + name
    
    # split the dataset in 3 chunks (as 1:2:3) and save as X_train_1, X_train_2...
    sq_start = 0
    for i in range(1, 4):
        sq_end = int(sq_start + len(group) / 6 * i)
        np.savetxt(name + '_' + str(i), group[sq_start:sq_end], delimiter=',', fmt='%.3e')
        sq_start = sq_end
