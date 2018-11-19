import pymysql
import configparser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import csv


config = configparser.ConfigParser()
config.read('dbconfig.ini')

cnx = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True)

# q1 = 'select * from rcbill_my.anreport where period="2017-10-22" and decommissioned="N" and reported="Y"'

# q1 = 'select period, periodday, periodmth, periodyear, service, servicecategory, servicecategory2, servicesubcategory, package, ' \
#      'clientclass, region, sum(open_s) as activenos, sum(totopn_s) as openednos, sum(totcld_s) as closednos ' \
#      'from rcbill_my.anreport ' \
#      'where reported="Y" and decommissioned="N" and clientclass in ("Residential","Corporate Bundle","Corporate Bulk") ' \
#      'group by period, periodday, periodmth, periodyear, service, servicecategory, servicecategory2, servicesubcategory, package, clientclass, region'

# q1 = 'select kod, firm as firm1, firm as firm2 from rcbill.rcb_tclients order by firm limit 10'
q1 = 'select a.kod as kod1, a.firm as  firm1, b.kod as kod2, ' \
     ' b.firm as firm2 ' \
     ' from ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" ' \
     ' order by firm) a ' \
     ' cross join ' \
     ' ( select kod, firm from rcbill.rcb_tclients  where firm not like "%?%" ' \
     ' and firm not like "%close%" and firm not like "%PREPAID CARDS%" ' \
     ' order by firm) b'

df = pd.read_sql(q1, con=cnx)

header = ["kod1", "firm1", "kod2", "firm2"]
# df.to_csv('cust1.csv', columns=header, index=False, encoding='utf-8')
df.to_csv('cust1.csv', index=False, encoding='utf-8')
# df.to_csv('cust2.csv', columns=header, index=False, encoding='utf-8')

print(df.head(5))


from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def fuzzy_match(x, choices, scorer, cutoff):
    return process.extractOne(x, choices=choices, scorer=scorer, score_cutoff=cutoff)


df1 = pd.read_csv('cust1.csv')
print(df1.head())
# df2 = pd.read_csv('cust2.csv')


def get_ratio(row):
    name1 = row['firm1']
    name2 = row['firm2']
    return fuzz.token_set_ratio(name1, name2)


df1['score'] = df1.apply(get_ratio, axis=1)
df2 = df1[df1['score']>81]
df2.to_csv('cust2.csv', index=False, encoding='utf-8')
# print(get_ratio())


# FuzzyWuzzyResults = df1.loc[:, 'firm'].apply(
#     fuzzy_match,
#     args=(
#         df2.loc[:, 'firm'],
#         fuzz.token_set_ratio,
#         90
#     )
# )

# print(FuzzyWuzzyResults)

# print(df1.head(5))
# print(df2.head(5))

# print(fuzz.ratio('ABDUL AZIZ EBRAHIM','ABDUL AZIZ EBRAHIM'))
# print(fuzz.partial_ratio('ABDUL AZIZ EBRAHIM','ABDUL AZIZ EBRAHIM'))
# print(fuzz.token_sort_ratio('ABDUL AZIZ EBRAHIM','ABDUL AZIZ EBRAHIM'))
# print(fuzz.token_set_ratio('ABDUL AZIZ EBRAHIM','ABDUL AZIZ EBRAHIM'))



