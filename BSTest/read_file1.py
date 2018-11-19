import pymysql
import configparser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import csv
import itertools
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
import time

start_time = time.time()
print("Starts:" + time.asctime(time.localtime(start_time)))


header = ["kod1||firm1", "kod2||firm2"]
header2 = ["kod1", "firm1", "kod2", "firm2", "score"]
file1 = 'C:\_out\custname1.csv'
file2 = 'C:\_out\custname2.csv'

print("Time Elapsed 1 :" + str(time.time() - start_time))

print("Time Elapsed 2 :" + str(time.time() - start_time))

with open(file2, 'w', newline='', encoding="utf-8") as outfile2:
    writer2 = csv.writer(outfile2)

    # writer = csv.DictWriter(outfile, fieldnames=["kod1", "firm1", "kod2", "firm2"])
    # writer.writeheader()
    writer2.writerow(header2)

    f = open(file1)

    # data = []
    # dfr = pd.DataFrame()
    next(f, None)
    i = 0
    for line in f:
        i = i + 1
        data_line = line.rstrip().split(',')
        ele1 = data_line[0].split('||')
        ele2 = data_line[1].split('||')
        kod1 = ele1[0]
        firm1 = ele1[1]
        kod2 = ele2[0]
        firm2 = ele2[1]
        score = fuzz.token_set_ratio(firm1, firm2)

        # print('kod1:' + kod1)
        # print('firm1:' + firm1)
        # print('kod2:' + kod2)
        # print('firm2:' + firm2)
        # print('score:' + str(score))

        if score > 90:
            temp2 = (kod1, firm1, kod2, firm2, score)
            writer2.writerow(temp2)

        if i % 10000000 == 0:
            print("Time Elapsed:" + str(i) + " - " + str(time.time() - start_time))

f.close()

# dfr2.to_csv('C:\_out\custname2.csv', index=False, encoding='utf-8')

# os.remove(file1)

print("Time Elapsed 3 :" + str(time.time() - start_time))

print("Ends:" + time.asctime(time.localtime(time.time())))
