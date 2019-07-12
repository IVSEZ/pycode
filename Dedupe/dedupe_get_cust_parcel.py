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

cnx = pymysql.connect(host=config['rcbill']['host'], user=config['rcbill']['user'],
                      password=config['rcbill']['pass'], db=config['rcbill']['db'], charset="utf8",
                      use_unicode=True)

q1 = 'select clientcode as kod1, clientname as firm1, greatest(a1_parcel, a2_parcel, a3_parcel) as g_parcel1 ' \
     ' from rcbill.rcb_clientparcels ' \

q2 = 'select clientcode as kod2, clientname as firm2, greatest(a1_parcel, a2_parcel, a3_parcel) as g_parcel2 ' \
     ' from rcbill.rcb_clientparcels ' \

df = pd.read_sql(q1, con=cnx)
df2 = pd.read_sql(q2, con=cnx)

header = ["kod1||firm1||parcel1", "kod2||firm2||parcel2"]
header2 = ["kod1", "firm1", "parcel1", "kod2", "firm2", "parcel2", "score"]

file1 = 'C:\_out\custparcel1.csv'
file2 = 'C:\_out\custparcel2.csv'

print("Time Elapsed 1 :" + str(time.time() - start_time))

i = 0
with open(file1, 'w', newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    writer.writerow(header)

    for a, b in itertools.product(df['kod1'].str.replace(',', '').str.strip() + '||' + (
            df['firm1'].str.replace(',', '').str.strip()).str.upper() + '||' + df['g_parcel1']
                                ,
                                  df2['kod2'].str.replace(',', '').str.strip() + '||' + (
                                          df2['firm2'].str.replace(',', '').str.strip()).str.upper() + '||' + df2[
                                      'g_parcel2']
                                  ):
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
# os.remove(file1)

print("Time Elapsed 3 :" + str(time.time() - start_time))

print("Ends:" + time.asctime(time.localtime(time.time())))

