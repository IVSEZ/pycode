# import requests
#
#
# s = requests.Session()
# site_url = 'https://rcboss.intelvision.sc/rcbill/default.asp'
#
# s.get(site_url)
#
# s.post(site_url, data={'username': 'rahul', 'password': 'iv0917'})
#
# reppage = 'https://rcboss.intelvision.sc/RCBill/wflow/common/' \
#           'report.asp?SalesReport=&preset=296a3a13402420e525790ec44cf7028b'
#
# report = s.get(reppage)
#
# print(report.text)

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup, SoupStrainer
import requests
from lxml import html
from urllib.request import urlopen, urlretrieve, quote
from requests_html import HTMLSession

BASE_URL = 'http://rcboss.intelvision.sc/RCBill/menu1.asp'
REPORT_URL = "https://rcboss.intelvision.sc/RCBill/wflow/common/report.asp?SalesReport=&preset=296a3a13402420e525790ec44cf7028b"
BASE_ACCESS_URL = 'https://rcboss.intelvision.sc/rcbill/'

FILE_URL = 'https://rcboss.intelvision.sc/rcbill/wflow/common/download-report.asp'




# start session
# session = requests.Session()
session = HTMLSession()
response = session.get(BASE_URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

# session.post(menu_link, data={'username': 'rahul', 'password': 'iv0917'})
session.post(BASE_URL, data={'username': 'rahul', 'password': 'iv0917'})

# soup = BeautifulSoup(response.text, "lxml")

# response = session.get(REPORT_URL, headers={'Referer': REPORT_URL})
response = session.get(REPORT_URL)

print(response.content)
# soup = BeautifulSoup(response.content, "lxml")

# links = []
# for link in soup.findAll('a'):
#     links.append(link.get('href'))
#     if "download-report.asp" in link.get('href'):
#         # links.append(link.get('href'))
#         # file = session.get()
#         print(link.get('href'))
#         print(link.get('href').split("download-report.asp")[1])
#         NEW_REPORT_URL = FILE_URL + link.get('href').split("download-report.asp")[1]
#         print(NEW_REPORT_URL)
#         resp = session.get(NEW_REPORT_URL)
#         # print(resp.text)
#
#         # output = open('sales_report.xls', 'wb')
#         # output.write(resp.content)
#         # output.close()
#
# print(links)

print(response.html.absolute_links)
links = []
for link in response.html.absolute_links:
    if "download-report.asp" in link:
        print(link)
        resp = session.get(link)

        # print(resp.text)

        # output = open('sales_report.xls', 'wb')
        # output.write(resp.content)
        # output.close()
# print(links)


