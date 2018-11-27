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

file1 = 'C:\_out\custname1.csv'
file2 = 'C:\_out\custname2.csv'


with open(file1) as csvfile:
    row_count = sum(1 for row in csvfile)
    print(row_count if row_count else 'Empty')

print("Time Elapsed 1 :" + str(time.time() - start_time))


print("Time Elapsed 2 :" + str(time.time() - start_time))

print("Ends:" + time.asctime(time.localtime(time.time())))
