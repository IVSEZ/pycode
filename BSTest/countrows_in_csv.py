import os
import csv
import dask
import dask.dataframe as dd


file1 = 'C:\_out\custname2.csv'
file2 = 'C:\_out\custnin3.csv'
file3 = 'C:\_out\custphone1.csv'

with open(file3) as csvfile:
    row_count = sum(1 for row in csvfile)
    print(row_count if row_count else 'Empty')

# bigfile = dd.read_csv(file3)

# print(bigfile.info())
# print(str(len(bigfile)))
