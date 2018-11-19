from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = 'C:/Users/rahul/Downloads/chromedriver_win32/chromedriver.exe'

browser = webdriver.Chrome(chromedriver)
browser.get('https://rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill')
#browser.get('https://rcboss.intelvision.sc/RCBill/')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys('rahul')
password.send_keys('iv0917')

browser.find_element_by_id("LoginSubmit").click()