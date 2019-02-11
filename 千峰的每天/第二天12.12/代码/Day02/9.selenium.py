import time

from selenium import webdriver
import requests

path = "E:\chromedriver.exe"
chrom = webdriver.Chrome(executable_path=path)

url = "http://www.iqiyi.com"
chrom.get(url=url)

time.sleep(3)
input_text = chrom.find_elements_by_id('//input[@id="kw"]')
input_text.send_keys("美女")
time.sleep(3)
btn_search = chrom.find_elements_by_id('//input[@id="su"]')
btn_search.click()

time.sleep(5)
chrom.quit()
