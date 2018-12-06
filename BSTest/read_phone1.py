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
from tqdm import tqdm

start_time = time.time()
print("Starts:" + time.asctime(time.localtime(start_time)))

header = ["kod1||firm1||phone1", "kod2||firm2||phone2"]
header2 = ["kod1", "firm1", "phone1", "kod2", "firm2", "phone2", "score_tser"]
header3 = ["kod1", "firm1", "phone1", "kod2", "firm2", "phone2", "score_r", "score_pr", "score_tsor", "score_tser", "score_ptsor",
           "score_ptser", "score_qr", "score_uqr", "score_wr", "score_uwr"]

file1 = 'C:\_out\custphone11.csv'
file2 = 'C:\_out\custphone2.csv'
file3 = 'C:\_out\custphone3.csv'


print("Time Elapsed 1 :" + str(time.time() - start_time))

print("Time Elapsed 2 :" + str(time.time() - start_time))


class fragile(object):
    class Break(Exception):
        """Break out of the with statement"""

    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self.value.__enter__()

    def __exit__(self, etype, value, traceback):
        error = self.value.__exit__(etype, value, traceback)
        if etype == self.Break:
            return True
        return error


with open(file3, 'w', newline='', encoding="utf-8") as outfile3:
    writer3 = csv.writer(outfile3)

    # writer3.writerow(header3)
    writer3.writerow(header2)

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
        phone1 = ele1[2]
        kod2 = ele2[0]
        firm2 = ele2[1]
        phone2 = ele2[2]

        # score_r = fuzz.ratio(phone1, phone2)
        # score_pr = fuzz.partial_ratio(phone1, phone2)
        # score_tsor = fuzz.token_sort_ratio(phone1, phone2)
        score_tser = fuzz.token_set_ratio(phone1, phone2)
        # score_ptsor = fuzz.partial_token_sort_ratio(phone1, phone2)
        # score_ptser = fuzz.partial_token_set_ratio(phone1, phone2)
        # score_qr = fuzz.QRatio(phone1, phone2)
        # score_uqr = fuzz.UQRatio(phone1, phone2)
        # score_wr = fuzz.WRatio(phone1, phone2)
        # score_uwr = fuzz.UWRatio(phone1, phone2)

        # print('ROW:' + str(i) + ' - kod1:' + kod1 + ' firm1:' + firm1 + ' phone1:' + phone1 + ' - kod2:'
        #       + kod2 + ' firm2:' + firm2 + ' phone1:' + phone1 + ' - score:' + str(score_tser))
        # print('kod1:' + kod1)
        # print('firm1:' + firm1)
        # print('kod2:' + kod2)
        # print('firm2:' + firm2)
        # print('score:' + str(score_tser))

        # if score_r > 90 or score_pr > 90 or score_tsor > 90 or score_tser > 90 or score_ptsor > 90 or score_ptser > 90 \
        #         or score_qr > 90 or score_uqr > 90 or score_wr > 90 or score_uwr > 90:

        if score_tser >= 99:
            # temp3 = (
            #     kod1, firm1, phone1, kod2, firm2, phone2, score_r, score_pr, score_tsor, score_tser, score_ptsor,
            #     score_ptser, score_qr,
            #     score_uqr, score_wr, score_uwr)
            temp3 = (kod1, firm1, phone1, kod2, firm2, phone2, score_tser)
            writer3.writerow(temp3)

        if i % 10000000 == 0:
            print("Time Elapsed:" + str(i) + " - " + str(time.time() - start_time))

        # if i > 10000000:
        #     print("Breaking loop: " + str(i) + " - " + str(time.time() - start_time))
        #     outfile3.close()
        #     # fragile.Break
        #     break


f.close()

# os.remove(file1)

print("Total records: " + str(i))
print("Time Elapsed 3 :" + str(time.time() - start_time))

print("Ends:" + time.asctime(time.localtime(time.time())))

