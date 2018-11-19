import bs4 as bs

import mechanicalsoup

import robobrowser
from robobrowser import RoboBrowser

#import urllib.request

import requests

browser = RoboBrowser()
browser.open('http://app.rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill')

# Get the signup form
signup_form = browser.get_form('frmLogin', "lxml")


# Fill it out
signup_form['username'].value = 'rahul'
signup_form['password'].value = 'iv0916'

# Serialize it to JSON
signup_form.serialize()


# And submit
browser.submit_form(signup_form)
# print page
#print(browser.parsed)

#reppage = "http://rcboss.intelvision.sc/RCBill/wflow/common/report.asp?rbSubscribtionStatistics1V3=&preset=6aac706c4a742cb85e48042f57a16f09"
#reppage = "http://rcboss.intelvision.sc/rcbill/wflow/common/report_view.asp?id=00000000000000000000000000000008"
#reppage ="http://rcboss.intelvision.sc/rcbill/wflow/common/drill-report.asp?r=rbSubscribtionStatisticsV3_List&rowslimit=2000&periodics=1&period=2016-07-01;2016-07-01&region=&clienttype=&clientclass=&baseservice=&service=&servicerate=&promotion=&validity=&RegionsLevel3=&RegionsLevel2=&RegionsLevel1=&distributor=&state=open&u=00000000000000000000000000000008&"
reppage="http://rcboss.intelvision.sc/RCBill/wflow/common/report.asp?rbSubscribtionStatistics1V3"
import requests
res = requests.get(reppage)
res.raise_for_status()
playFile = open('activelist.xls', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()
# loginpage = "http://rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill"
# reppage ="http://rcboss.intelvision.sc/rcbill/wflow/common/report_view.asp?id=00000000000000000000000000000001&preset=100749097c8560f627a565806c6773b8"
# reppage = "https://pythonprogramming.net/parsememcparseface/"


#browser.open(reppage)

# source = urllib.request.urlopen(reppage).read()

# soup = bs.BeautifulSoup(source,'lxml')

# title of the page
# print(soup.title)

# get attributes:
# print(soup.title.name)

# get values:
# print(soup.title.string)

# beginning navigation:
# print(soup.title.parent.name)

# getting specific values:
#print(soup.p)

# print(soup.find_all('p'))


# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
#     print(str(paragraph.text))

# for url in soup.find_all('a'):
#     print(url.get('href'))

# print(soup.get_text())

# nav = soup.nav
#
# for url in nav.find_all('a'):
#     print(url.get('href'))


# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# for div in soup.find_all('div', class_='body'):
#     print(div.text)

# table = soup.table

# or

# table = soup.find('table')

# table_rows = table.find_all('tr')
#
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)