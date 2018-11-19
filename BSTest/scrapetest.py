import requests
from bs4 import BeautifulSoup

pageurl = "http://192.168.100.139:8067/leases.txt"
#pageurl = "http://192.168.100.139:8067/leases.html"
page = requests.get(pageurl)

#print(page.status_code)

#print(page.content)

#soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

#soup.find_all('th')


lines = str(page.content).split('\\n')
#print(lines)

#for l in lines[0:4]:
for l in lines[1:]:
    print(l.replace("\\r","").replace("\\'","\'").replace("b'","").replace(" ","|"))


#if you want to split the html into lines, use the split command like below
#lines = page.content.split('\n')
#print(lines)