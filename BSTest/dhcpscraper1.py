# import pandas as pd
# fof_url = "http://192.168.100.139:8067/hosts.html"
# fof = pd.read_html(fof_url)[0]
# fof.to_csv("dhcphosts1.csv", header = False, index = False)

import requests
import csv
from bs4 import BeautifulSoup

r=requests.get('http://192.168.100.139:8067/hosts.html')

data = r.text
soup = BeautifulSoup(data, "html.parser")

# print(data)

#select a specific table from the html page
#loop through rows of the table
#loop through the cells of a row
#results in 14 lines of text per symbol

table = soup.find( "table" )

for row in table.findAll("tr"):
    for cell in row("td"):
        print (cell.get_text().strip())