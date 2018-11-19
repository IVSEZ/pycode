from bs4 import BeautifulSoup

import requests
import os

r = requests.get("http://pplaaf.in/gleaks/")
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

    # href = link['href']

    if '.zip' in link['href']:
        response = requests.get(link['href'])
        with open(os.path.join("file"), 'wb') as f:
            f.write(response.content)
        # remoteZip = urlopen(Request(href))
        # file_name = href.rpartition('/')[-1]
        # local_file = open(file_name, 'wb')
        # local_file.write(remoteZip.read())
        # local_file.close()



