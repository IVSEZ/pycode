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

config = configparser.ConfigParser()
config.read('dbconfig.ini')

cnx = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True)


def get_ratio(row):
    name1 = row['firm1']
    name2 = row['firm2']
    return fuzz.token_set_ratio(name1, name2)


q1 = 'select a.kod as kod1, a.firm as  firm1 ' \
     ' from ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" order by firm limit 100) a ' \

q2 = 'select a.kod as kod2, a.firm as  firm2 ' \
     ' from ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" order by firm limit 100) a ' \

df = pd.read_sql(q1, con=cnx)
df2 = pd.read_sql(q2, con=cnx)

# dfr = pd.DataFrame()
dfr = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=["kod1", "firm1", "firm2", "kod2"])
# print(dfr.head())
dfs = pd.DataFrame(np.nan, index=[0, 1, 2, 3, 4], columns=["kod1", "firm1", "firm2", "kod2", "score"])

for index, row in df.iterrows():
    # print(row['kod1'], row['firm1'])
    for index2, row2 in df2.iterrows():
        # print(row['kod1'], row['firm1'], row2['kod2'], row2['firm2'])
        dfr.append(pd.Series([row['kod1'], row['firm1'], row2['kod2'], row2['firm2']], index=dfr.columns),
                   ignore_index=True)
        # dfr['kod1'] = row['kod1']
        # dfr['firm1'] = row['firm1']
        # dfr['kod2'] = row2['kod2']
        # dfr['firm2'] = row2['firm2']

        dfs.append(pd.Series([row['kod1'], row['firm1'], row2['kod2'], row2['firm2'], dfr.apply(get_ratio, axis=1)],
                             index=dfs.columns), ignore_index=True)
        # dfr['score'] = dfr.apply(get_ratio, axis=1)

# dfr2 = dfr[dfr['score'] > 81]

print(dfs.head())
# for index3, row3 in dfs.iterrows():
#     print(row3['kod1'], row3['firm1'], row3['kod2'], row3['firm2'], row3['score'])

#
# # header = ["kod1", "firm1", "kod2", "firm2"]
# # header = ["kod1", "firm1", "firm2", "kod2"]
# header = ["firm1", "firm2"]
#
# # df.to_csv('cust1.csv', index=False, encoding='utf-8')
#
# # df3 = pd.DataFrame({'kod1': [], 'firm1': [], 'kod2': [], 'firm2': []})
#
#
# # od = OrderedDict(sorted())
#
# # d = defaultdict(list)
#
# # df3 = pd.DataFrame()
#
# # df3 = (DataFrame)(itertools.product(df['kod1'], df['firm1'], df2['kod2'], df2['firm2']))
#
# # print(df3)
#
#
# with open('C:\_out\custname1.csv', 'w', newline='', encoding="utf-8") as outfile:
#     writer = csv.writer(outfile)
#
#     # writer = csv.DictWriter(outfile, fieldnames=["kod1", "firm1", "kod2", "firm2"])
#     # writer.writeheader()
#     writer.writerow(header)
#     # for row in data:
#     #     writer.writerow(row + (url1,))
#
#     # for i, j, k, l in itertools.product(df['kod1'], df['firm1'], df2['kod2'], df2['firm2']):
#     for i, j in itertools.product(df['firm1'], df2['firm2']):
#         # d[0].append(i)
#         # d[1].append(j)
#         # d[2].append(k)
#         # d[3].append(l)
#         # d[j].append(i[0],i[1],i[2],i[3])
#         # d[0].append(i)
#         # print(i[1])
#         # df3.append(i[0])
#         # print(j)
#         # print(d)
#         # temp = (i, j, k, l)
#         # temp = (df['kod1'], i, j, df2['kod2'])
#         temp = (i, j)
#         # print(temp)
#         # df3.append(temp)
#         # df3.append(pd.DataFrame(list(temp)))
#         writer.writerow(temp)
#
#     # print(df3.head(5))
#     # df3.to_csv('C:\_out\custname1.csv', index=False)
#
#
#
#
#
# def fuzzy_match(x, choices, scorer, cutoff):
#     return process.extractOne(x, choices=choices, scorer=scorer, score_cutoff=cutoff)
#
#
# # dfr = pd.read_csv('C:\_out\custname1.csv')
# # print(dfr.head(5))
# # df2 = pd.read_csv('cust2.csv')
#
#
# def get_ratio(row):
#     name1 = row['firm1']
#     name2 = row['firm2']
#     return fuzz.token_set_ratio(name1, name2)
#
#
# dfr['score'] = dfr.apply(get_ratio, axis=1)
# dfr2 = dfr[dfr['score'] > 81]
#
# print(dfr2.head(5))
#
# dfr2.to_csv('C:\_out\custname2.csv', index=False, encoding='utf-8')
#
#
#
# os.remove('C:\_out\custname1.csv')
