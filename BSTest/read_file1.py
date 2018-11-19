import pandas as pd
import dask.dataframe as dd
import os
from tqdm import tqdm

TRAIN_PATH = 'C:\_out\custname1.csv'

# %%time
# Assume we only know that the csv file is somehow large, but not the exact size
# we want to know the exact number of rows

# Method 1, using file.readlines. Takes about 20 seconds.
# with open(TRAIN_PATH) as file:
#     n_rows = len(file.readlines())

f = open(TRAIN_PATH)

data = []

for line in f:
   data_line = line.rstrip().split(',')
   data.append(data_line)


print(size)
print(head)
