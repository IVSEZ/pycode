from __future__ import print_function

import os
import itertools
import time
import logging
import optparse
import locale
import pickle
import multiprocessing

import pymysql
import pymysql.cursors

# import MySQLdb
# import MySQLdb.cursors

import dedupe


import configparser



optp = optparse.OptionParser()
optp.add_option('-v', '--verbose', dest='verbose', action='count',
                help='Increase verbosity (specify multiple times for more)'
                )
(opts, args) = optp.parse_args()
log_level = logging.WARNING
if opts.verbose :
    if opts.verbose == 1:
        log_level = logging.INFO
    elif opts.verbose >= 2:
        log_level = logging.DEBUG
logging.getLogger().setLevel(log_level)

MYSQL_CNF = os.path.abspath('.') + '/mysql.cnf'

settings_file = 'mysql_example1_settings'
training_file = 'mysql_example1_training.json'

start_time = time.time()



# connect to mysql
config = configparser.ConfigParser()
config.read('dbconfig.ini')

c1 = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True, cursorclass=pymysql.cursors.DictCursor)


c2 = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True, cursorclass=pymysql.cursors.DictCursor)


DONOR_SELECT = "select id, firm, moladdress, danno, mphone from rcbill.rcb_tclients " \
                "where firm not in ('PREPAID CARDS') "

if os.path.exists(settings_file):
    print('reading from ', settings_file)
    with open(settings_file, 'rb') as sf :
        deduper = dedupe.StaticDedupe(sf, num_cores=4)
else:

    fields = [
        {'field' : 'firm', 'type': 'String'},
        {'field' : 'moladdress', 'type': 'String'},
        {'field' : 'danno', 'type': 'String', 'has missing' : True},
        {'field' : 'mphone', 'type': 'String', 'has missing' : True},
        ]

    # deduper = dedupe.Dedupe(fields)
    deduper = dedupe.Dedupe(fields, num_cores=4)

    c1.execute(DONOR_SELECT)
    temp_d = dict((i, row) for i, row in enumerate(c))

    deduper.sample(temp_d, 10000)
    del temp_d

    if os.path.exists(training_file):
        print('reading labeled examples from ', training_file)
        with open(training_file) as tf :
            deduper.readTraining(tf)

    print('starting active labeling...')

    dedupe.convenience.consoleLabel(deduper)

    with open(training_file, 'w') as tf:
        deduper.writeTraining(tf)

    deduper.train(recall=0.90)

    with open(settings_file, 'wb') as sf:
        deduper.writeSettings(sf)

    deduper.cleanupTraining()

print('blocking...')

print('creating blocking_map database')
c.execute("DROP TABLE IF EXISTS blocking_map")
c.execute("CREATE TABLE blocking_map "
          "(block_key VARCHAR(200), donor_id INTEGER) "
          "CHARACTER SET utf8 COLLATE utf8_unicode_ci")