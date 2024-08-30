import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://books.toscrape.com/")

title_tag = browser.find_element(By.XPATH,"/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a")

print(title_tag.text)
time.sleep(10)

browser.quit()
