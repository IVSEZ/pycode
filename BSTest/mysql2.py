import pymysql
import configparser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

q1 = 'select firm from rcbill.rcb_tclients'
df = pd.read_sql(q1, con=cnx)

print(df.head())




