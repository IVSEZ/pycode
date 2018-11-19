import pymysql
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Open database connection
db = pymysql.connect("localhost","webuser","webuser","rcbill" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print ("Database version : %s " % data)


# Prepare SQL query to INSERT a record into the database.
sql = "select a.CL_CLIENTNAME as CL_CLIENTNAME1, b.CL_CLIENTNAME as CL_CLIENTNAME2 \
        from \
        clientname a \
        cross join \
        clientsoundex b  \
        order by 1 asc "


try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print(cursor.rowcount)
   print("c1,c2,fr,fpr,fsor,fser")

   # with open('C://Workspace//IV//Work//Reports//Clients//names.csv', 'w') as csvfile:
   #     fieldnames = ['c1','c2','fr','fpr','fsor','fser']
   #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   #
   #     writer.writeheader()

   with open('C://Workspace//IV//Work//Reports//Clients//names.csv', 'w', newline='') as csvfile:
       field_names = ['c1','c2','fr','fpr','fsor','fser']
       csvwriter = csv.writer(csvfile, delimiter=',')
       # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

       csvwriter.writerow(['c1','c2','fr','fpr','fsor','fser'])

       for row in results:
           CL_CLIENTNAME1 = row[0]
           CL_CLIENTNAME2 = row[1]
           # Now print fetched result
           fr=fuzz.ratio(CL_CLIENTNAME1,CL_CLIENTNAME2)
           fpr=fuzz.partial_ratio(CL_CLIENTNAME1,CL_CLIENTNAME2)
           ftsor=fuzz.token_sort_ratio(CL_CLIENTNAME1,CL_CLIENTNAME2)
           ftser=fuzz.token_set_ratio(CL_CLIENTNAME1,CL_CLIENTNAME2)

           #print ("c1=%s,c2=%s,fr=%d,fpr=%d,ftsor=%d,ftser=%d" % (CL_CLIENTNAME1, CL_CLIENTNAME2,fr,fpr,ftsor,ftser))
           #if fr>70 or fpr>70 or ftsor>70 or ftser>70:
           if fr>64 and fpr > 70 and ftsor>64 and ftser > 70:
                #print("%s,%s,%d,%d,%d,%d" % (CL_CLIENTNAME1.strip(), CL_CLIENTNAME2.strip(), fr, fpr, ftsor, ftser))
                #print(fpr)
                #writer.writerow(CL_CLIENTNAME1.strip(),CL_CLIENTNAME2.strip(), fr, fpr, ftsor, ftser)
                csvwriter.writerow([CL_CLIENTNAME1.strip(),CL_CLIENTNAME2.strip(), fr, fpr, ftsor, ftser])
           #print(CL_CLIENTNAME1, CL_CLIENTNAME2,fr,fpr,ftsor,ftser)

except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()




# disconnect from server
db.close()