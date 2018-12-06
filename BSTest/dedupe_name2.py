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

config = configparser.ConfigParser()
config.read('dbconfig.ini')

cnx = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True)

q1 = 'select a.kod as kod1, a.firm as  firm1 ' \
     ' from ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" order by firm) a ' \

q2 = 'select a.kod as kod2, a.firm as  firm2 ' \
     ' from ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" order by firm) a ' \

df = pd.read_sql(q1, con=cnx)
df2 = pd.read_sql(q2, con=cnx)

header = ["kod1||firm1", "kod2||firm2"]
header2 = ["kod1", "firm1", "kod2", "firm2", "score"]
file1 = 'C:\_out\custname1.csv'
file2 = 'C:\_out\custname2.csv'

print("Time Elapsed 1 :" + str(time.time() - start_time))

i = 0
with open(file1, 'w', newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    # writer = csv.DictWriter(outfile, fieldnames=["kod1", "firm1", "kod2", "firm2"])
    # writer.writeheader()
    writer.writerow(header)

    for a, b in itertools.product(df['kod1'].str.replace(',', '').str.strip() + '||' + (
                            df['firm1'].str.replace(',', '').str.strip()).str.upper(),
                                  df2['kod2'].str.replace(',', '').str.strip() + '||' + (
                                          df2['firm2'].str.replace(',', '').str.strip()).str.upper()):
        i = i + 1
        if i % 10000000 == 0:
            print("Time Elapsed:" + str(i) + " - " + str(time.time() - start_time))

        if a != b:
            temp = (a, b)
            # print(temp)
            writer.writerow(temp)

print("Total records: " + str(i))
# print("Time Elapsed 2 :" + str(time.time() - start_time))

# with open(file2, 'w', newline='', encoding="utf-8") as outfile2:
#     writer2 = csv.writer(outfile2)
#
#     # writer = csv.DictWriter(outfile, fieldnames=["kod1", "firm1", "kod2", "firm2"])
#     # writer.writeheader()
#     writer2.writerow(header2)
#
#     f = open(file1)
#
#     # data = []
#     # dfr = pd.DataFrame()
#     next(f, None)
#     i = 0
#     for line in f:
#         i = i + 1
#         data_line = line.rstrip().split(',')
#         ele1 = data_line[0].split('||')
#         ele2 = data_line[1].split('||')
#         kod1 = ele1[0]
#         firm1 = ele1[1]
#         kod2 = ele2[0]
#         firm2 = ele2[1]
#         score = fuzz.token_set_ratio(firm1, firm2)
#
#         # print('kod1:' + kod1)
#         # print('firm1:' + firm1)
#         # print('kod2:' + kod2)
#         # print('firm2:' + firm2)
#         # print('score:' + str(score))
#
#         if score > 90:
#             temp2 = (kod1, firm1, kod2, firm2, score)
#             writer2.writerow(temp2)
#
#         if i % 10000000 == 0:
#             print("Time Elapsed:" + str(i) + " - " + str(time.time() - start_time))
#
# f.close()

# dfr2.to_csv('C:\_out\custname2.csv', index=False, encoding='utf-8')

# os.remove(file1)

print("Time Elapsed 3 :" + str(time.time() - start_time))

print("Ends:" + time.asctime(time.localtime(time.time())))
