import re
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://192.168.100.139:8067/hosts.html')
soup = BeautifulSoup(html,"lxml")
data = soup.findAll(text=True)


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


result = filter(visible, data)

print(list(result))