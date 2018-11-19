import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://192.168.100.139:8067/leases.html"

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


