from selenium import webdriver
from time import sleep

driver = webdriver.Edge(r'C:\Users\mepg1\Desktop\Archivos\Driver\msedgedriver.exe')

driver.get('https://www.google.com')
sleep(1)
driver.find_element_by_name("q").send_keys("We are the champions")
sleep(1)
driver.find_element_by_name("btnK").click()
sleep(1)
driver.close()