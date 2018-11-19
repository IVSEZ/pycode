#import the library used to query a website
import urllib

import urllib.request
import mechanize


#specify the url
#reppage = "http://app.rcboss.intelvision.sc/rcbill/wflow/common/report_view.asp?id=0000000000000000000000000000000d&preset=6aac706c4a742cb85e48042f57a16f09"
#reppage = "http://app.rcboss.intelvision.sc/rcbill/wflow/common/report.asp?rbSubscribtionStatistics1V3"
reppage = "http://app.rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill"

#Query the website and return the html to the variable 'page'
#page = urllib. .request(reppage)

with urllib.request.urlopen(reppage) as response:
   html = response.read()
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(html)

print(soup)