from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from   selenium.common.exceptions import TimeoutException

user="rahul"
pwd="iv0916"


#from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)


#driver=webdriver.Ie()
#driver = webdriver.Firefox()
#driver.get("http://app.rcboss.intelvision.sc/RCBill/menu1.asp?op=RCBill")
driver.get("http://rcboss.intelvision.sc/")
assert "RC Billing" in driver.title
#driver.switch_to(driver.find_element_by_tag_name("contents"))

frame_modal = driver.find_element_by_class_name("menu")
driver.switch_to_frame(frame_modal)

elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()
#webdriver.wait

#driver = webdriver.Firefox(firefox_binary=binary)
#wait = webdriver.wait(driver,5)
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.get("http://rcboss.intelvision.sc/rcbill/wflow/common/report_view.asp?id=00000000000000000000000000000002&preset=6aac706c4a742cb85e48042f57a16f09")
assert "Menu" in driver.title
#driver.get("http://rcboss.intelvision.sc/RCBill/wflow/common/report.asp?rbSubscribtionStatistics1V3")

#driver.close()
