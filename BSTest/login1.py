import requests
from lxml import html

session_requests = requests.session()

login_url = "http://rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill"
result = session_requests.get(login_url)

print(result)