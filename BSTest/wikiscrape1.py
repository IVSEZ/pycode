import requests
import pandas as pd

website_url=requests.get('https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
# print(soup.prettify())

my_table = soup.find('table',{'class' : 'sortable wikitable'})

# print(my_table)

# links = my_table.findAll('a')
# print(links)

# tr = my_table.findAll('tr')
# print(tr)

ths = my_table.findAll('th')
# print(ths)

# for th in ths:
    # print(th.text)

trs = my_table.findAll('tr')

for tr in trs:
    print(tr.text)


df = pd.DataFrame()

df