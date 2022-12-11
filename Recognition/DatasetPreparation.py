import pathlib, os
import numpy as np
import pandas as pd


def DataframePreparation(path, label):
    data = np.loadtxt(path)

    x,y,z = np.split(data, 3, axis=1)
    x,y = x.flatten(), y.flatten()
    y = y*-1+512

    cx, cy = sum(x)/90, sum(y)/90
    res = []
    for xi,yi in zip(x,y):
        res.append(((cx-xi)**2 + (cy-yi)**2) ** 0.5)

    res.extend([cx, cy, label])
    df.loc[len(df.index)] = res

# dataframe creation
columns = ['d'+str(i) for i in range(1,91)]
columns.extend(['cx', 'cy', 'label'])
df = pd.DataFrame(columns=columns)

directory = pathlib.Path(__file__).parent.resolve()
data_dir = os.path.join(directory, '90point')

#iterating through all files within 90-point
for dir in sorted(os.listdir(data_dir)):
    parent = os.path.join(data_dir, dir)
    for file in sorted(os.listdir(parent)):
        fullpath = os.path.join(parent, file)
        DataframePreparation(fullpath, dir)

df.to_csv(os.path.join(directory, 'dataset.csv'), encoding='utf-8', index=False)
