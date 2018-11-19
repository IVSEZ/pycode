from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\Workspace-Non\\Apps\\geckodriver-v0.11.1-win64\\geckodriver.exe")
print("Firefox Headless Browser Invoked")
driver.get('https://duckduckgo.com/')
searchform = driver.find_element_by_id('search_form_input_homepage')
searchform.send_keys('intelvision')
searchform.submit()
results = driver.fin
driver.quit()