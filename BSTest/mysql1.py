import pymysql
import configparser

config = configparser.ConfigParser()
config.read('dbconfig.ini')


def query_mysql(query):
    cnx = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                          password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                          use_unicode=True)
    cursor = cnx.cursor()
    cursor.execute(query)
    # get header and rows
    header = [i[0] for i in cursor.description]
    rows = [list(i) for i in cursor.fetchall()]
    # append header to rows
    rows.insert(0, header)
    cursor.close()
    cnx.close()
    return rows


# take list of lists as argument
def nlist_to_html(list2d):
    # bold header
    htable = u'<table border="1" bordercolor=000000 cellspacing="0" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:13px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
    list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]]
    for row in list2d:
        newrow = u'<tr>'
        newrow += u'<td align="left" style="padding:1px 4px">' + str(row[0]) + u'</td>'
        row.remove(row[0])
        newrow = newrow + ''.join([u'<td align="right" style="padding:1px 4px">' + str(x) + u'</td>' for x in row])
        newrow += '</tr>'
        htable += newrow
    htable += '</table>'
    return htable


def sql_html(query):
    return nlist_to_html(query_mysql(query))


# usage example
query = 'call sp_activenumber(22,10,2017,"N","Y")'

#print(query_mysql(query))

print(sql_html(query))
