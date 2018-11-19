import pymysql
##import pymysql.cursor

#conn= pymysql.connect(host='localhost',user='phpuser',password='phpuser',db='rcbill_my',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
#a=conn.cursor()
## sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'

#sql='call sp_activenumber(1,11,2016,"N","Y")'
#a.execute(sql)

#print(a.description)
#print()

def query_mysql(query):
	cnx = pymysql.connect(host='localhost',user='phpuser',password='phpuser',db='rcbill_my',charset="utf8", use_unicode = True)
	cursor = cnx.cursor()
	cursor.execute(query)
	#get header and rows
	header = [i[0] for i in cursor.description]
	rows = [list(i) for i in cursor.fetchall()]
	#append header to rows
	rows.insert(0,header)
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


#usage example
query = 'call sp_activenumber(1,11,2016,"N","Y")'
print(sql_html(query))